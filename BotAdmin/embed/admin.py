from django.contrib import admin

from .models import *

# class EmbedsInline(admin.TabularInline):
#     model = ImageEmbed
#     extra = 1

# class EmbedPlannerAdmin(admin.ModelAdmin):
#     inlines = [ EmbedImageInline, ]

admin.site.register(EmbedModel)
admin.site.register(EmbedPlannerModel)