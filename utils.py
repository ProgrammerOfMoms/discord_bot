import requests
from datetime import datetime, timezone, timedelta
from settings import HOST
from const import *

import pytz
utc = pytz.utc

def get_embed_planners():
    response = requests.get(HOST+"embed/")
    if response.status_code != 200:
        pass
        #handle bad request
    return response.json()

def check_embed_planner(embed):
    #django server on UTC+3
    offset = timezone(timedelta(hours=3))
    now = datetime.now(offset).replace(tzinfo=utc)
    t = datetime.strptime(embed["start_in"], "%Y-%m-%dT%H:%M:%S+03:00").replace(tzinfo=utc)
    if now > t and embed["is_active"] and not embed["is_done"]:
        return True
    return False

def update_embed_planner(embed_id, is_done=None, message_id = None):
    URL = HOST+"embed/update/"
    body = {
        "id": embed_id
        }
    if is_done is not None:
        body["is_done"] = is_done
    if message_id is not None:
        body["message_id"] = message_id
    resp = requests.post(URL, data=body)
    if resp.status_code == 200:
        print("is true")
        return True
    return False

def get_all_users():
    URL = HOST + "user/"
    users = requests.get(URL).json()
    return users

def balance_users(discord_us, django_us):
    pass

def create_reaction(user_id, message_id, guild_id):
    URL = HOST+'user/reaction/'
    body = {
        "user_id": user_id,
        "message_id": message_id,
        "guild_id": guild_id
    }
    reaction = requests.post(URL, data=body).json()
    return reaction

def get_tournament_by_msg(id):
    URL = HOST+f'tournament/by_message/?message_id={id}'
    resp = requests.get(URL)
    return resp.json()

def get_tournament_participants(id):
    URL = HOST+"tournament/participants/"
    body = {"id": id}
    participants = requests.post(URL, data=body).json()
    return participants

def register_user(user_id, tour_id):
    URL = HOST + "user/register/"
    body = {"user_id": user_id, "tournament_id": tour_id}
    resp = requests.post(URL, data=body)

def get_scenario(name):
    URL = HOST+"scenario/by_name/"
    body = {"name": FIRST_REGISTARTION}
    resp = requests.post(URL, data=body)
    return resp.json()

def bind_scenario(user_id, scenario_id):
    URL = HOST+"user/bind_scenario/"
    body={'user_id': user_id, 'scenario_id': scenario_id}
    resp = requests.post(URL, data=body)

def get_next_msg(user_id):
    URL = HOST + "user/scenario/next/"
    body = {"user_id": user_id}
    resp = requests.post(URL, data=body).json()
    if resp["q"] is not None:
        return resp["q"]
    return DEFAULT_MSG

def process_msg(user_id, content):
    try:
        URL = HOST + "user/process/"
        body = {"user_id": user_id, "content": content}
        resp = requests.post(URL, body)
        if resp.status_code == 200:
            return True
        return False
    except:
        return False
    




    



