from django.db import models
from tournament.models import TournamentModel

class EmbedModel(models.Model):
    title = models.CharField(verbose_name="Заголовок", max_length=256, blank=True, null=True)
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    url = models.URLField(verbose_name="url", blank=True, null=True)
    thumbnail = models.ImageField(verbose_name="Thumbnail", upload_to="thimbnail_img/", blank=True, null = True)
    author_name = models.CharField(verbose_name="Имя автора", max_length=256, blank=True, null = True)
    author_link = models.URLField(verbose_name="Ссылка автора", blank=True, null = True)
    author_icon = models.ImageField(verbose_name="Картинка автора", upload_to="author_img/", blank=True, null = True)
    footer  = models.CharField(verbose_name="Футер", max_length=256, blank=True, null=True)

    message_id = models.BigIntegerField(blank=True, null=True)
    tournament = models.ForeignKey(to=TournamentModel,
                                   on_delete=models.CASCADE,
                                   related_name="embeds",
                                   verbose_name="Турнир",
                                   blank=True,
                                   null=True)
    

    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        verbose_name = "Embeded Message"
        verbose_name_plural = "Embeded Messages"


class EmbedPlannerModel(models.Model):
    start_in = models.DateTimeField(verbose_name="Начать в")
    is_active = models.BooleanField(verbose_name="Активно", default=True)
    is_done = models.BooleanField(verbose_name="Выполнено", default=False)
    embed = models.ForeignKey(to=EmbedModel, on_delete=models.CASCADE, related_name="planners")

    def save(self, *args, **kwargs):
        super(EmbedPlannerModel, self).save(*args, **kwargs)
        #add some behavior
