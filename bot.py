import discord
from discord.ext import commands, tasks

from settings import BOT_TOKEN, BOT_ID_CHANNEL, APP_ID
from utils import *
from const import *
from env_variables import set_all

set_all()

bot = commands.Bot(command_prefix="!") #init bot with ! command_prefix

@bot.command(pass_contex=True)
async def test(ctx, arg):
    await ctx.send(arg)

@bot.event
async def on_raw_reaction_add(payload):
    if payload.user_id == APP_ID:
        return
    tournament = get_tournament_by_msg(payload.message_id)
    if tournament is not None:
        participants = get_tournament_participants(tournament["id"])
        already_registred = False
        for p in participants:
            if p['id'] == payload.user_id:
                already_registred = True
                break
        if already_registred:
            user = bot.get_user(payload.user_id)
            await user.send(ALREADY_REGISTRED)
        else:
            register_user(payload.user_id, tournament["id"])
            scenario = get_scenario(name = "first_registration")
            prefix = FIRST_REGISTARTION_PREFIX
            q = scenario['questions'][0]['q']
            user = bot.get_user(payload.user_id)
            await user.send(f"{prefix}\n{q}")
            bind_scenario(payload.user_id, scenario["id"])

@bot.event
async def on_message(message):
    if message.author.id == APP_ID:
        return 
    if str(message.channel.type) == "private":
        print("1")
        user_id = message.author.id
        try:
            print("2")
            process_msg(user_id, message.content)
        except:
            print(3)
        print("4")
        #sending next
        msg = get_next_msg(user_id)
        user = bot.get_user(user_id)
        await user.send(msg)

@bot.event
async def on_member_join(member):
    print(f'Recognised that a member called {member} joined')
    await member.send("Добро пожаловать на сервер!")
    add_new_user(member.id)




    













@tasks.loop(seconds=20)
async def send_embeds():
    temp_host = "https://1bacaa7ec549.ngrok.io"
    # test_link = "https://img2.akspic.ru/image/131890-ozero-voda-ozernyj_kraj-peyzash-prirodnyj_landshaft-2560x1600.jpg"
    channel = bot.get_channel(BOT_ID_CHANNEL)
    embed_planners = get_embed_planners()
    try:
        for embed_planner in embed_planners:
            if check_embed_planner(embed_planner):
                print("tut")
                embed = embed_planner["embed"]
                print(embed)
                embed_msg = discord.Embed(title=embed["title"], description=embed["description"])
                embed_msg.set_author(name=embed["author_name"],
                                    url=embed["author_link"],
                                    icon_url=temp_host+embed["author_icon"][21:])
                embed_msg.set_thumbnail(url=temp_host+embed["thumbnail"][21:])
                embed_msg.set_footer(text=embed["footer"])
                print("tut2")
                msg = await channel.send(embed = embed_msg)
                await msg.add_reaction(emoji="\U0001F44D")
                update_embed_planner(embed_planner["id"], is_done=True, message_id = msg.id)
    except:
        pass
@tasks.loop(hours=24)
async def check_users():
    discord_users = bot.get_all_members()
    django_users = get_all_users()
    
    balance_users(discord_users, django_users)

@send_embeds.before_loop
async def before_send_embed():
    await bot.wait_until_ready()
@check_users.before_loop
async def before_check_users():
    await bot.wait_until_ready()
 
send_embeds.start()
# check_users.start()
bot.run(BOT_TOKEN)
