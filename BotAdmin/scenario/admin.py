from django.contrib import admin

from .models import *

class QuestionInline(admin.TabularInline):
    model = QuestionModel
    extra = 3

class ScenarioAdmin(admin.ModelAdmin):
    inlines = [ QuestionInline, ]

admin.site.register(ScenarioModel, ScenarioAdmin)