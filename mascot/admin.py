from django.contrib import admin
from mascot.models import Character


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "updated_at"]
    list_display_links = ["name"]
    list_filter = ["region", "city"]
    search_fields = ["name", "region", "city"]