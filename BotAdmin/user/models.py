from django.db import models

from tournament.models import TournamentModel
from embed.models import EmbedModel
from scenario.models import ScenarioModel

class UserModel(models.Model):
    id = models.IntegerField(verbose_name="id", primary_key=True)
    discord_name = models.CharField(max_length=256, verbose_name="Ник в дискорде", blank=True, null=True)
    sc_name = models.CharField(max_length=256, verbose_name="Ник в SC", blank=True, null=True)
    challonge_account = models.CharField(max_length=256, verbose_name="Challonge аккаунт", blank=True, null=True)
    ranked_ftw = models.URLField(verbose_name="Ranked_ftw", blank=True, null=True)
    max_ranked = models.IntegerField(verbose_name = "Максимальный MMR", blank=True, null=True)
    rating_games_count = models.CharField(max_length=256, verbose_name="Количество рейтинговых игр", blank=True, null=True)
    rasa = models.CharField(max_length=256, verbose_name="Раса", blank=True, null=True)
    team = models.CharField(max_length=256, verbose_name="Название команды", blank=True, null=True)
    tournaments = models.ManyToManyField(verbose_name="Турниры", 
                                         to=TournamentModel,
                                         related_name="participants",
                                         blank=True)
    scenario = models.ForeignKey(to=ScenarioModel,
                             on_delete=models.CASCADE,
                             verbose_name = "Активный сценарий",
                             blank=True,
                             null=True)
    next_question = models.IntegerField(verbose_name="Следующий вопрос", blank=True, null=True)
                             

class UserReactionModel(models.Model):
    guild_id = models.BigIntegerField()
    user = models.ForeignKey(to=UserModel, on_delete=models.CASCADE, related_name="reactions")
    embed = models.ForeignKey(to=EmbedModel, on_delete=models.CASCADE, related_name="reactions")