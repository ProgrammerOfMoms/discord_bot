from django.db import models

class ScenarioModel(models.Model):
    name = models.CharField(verbose_name="Название сценария", max_length=256) 

    def __str__(self):
        return self.name 

class QuestionModel(models.Model):
    q = models.TextField(verbose_name="Вопрос")
    scenario = models.ForeignKey(to=ScenarioModel,
                                 on_delete=models.CASCADE,
                                 related_name="questions",
                                 verbose_name="Сценарий")
    is_last = models.BooleanField(verbose_name="Последний вопрос?", default=False)
