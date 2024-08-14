from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import City

@admin.register(City)
class CityAdmin(TranslationAdmin):
    list_display = ('name', 'description')