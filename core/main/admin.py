from django.contrib import admin
from .models import (User_Info, AboutMe, 
                     Content, Whats, Skill, 
                     Image_Protfolio, Contact)
# Register your models here.

admin.site.register(User_Info)
admin.site.register(AboutMe)
admin.site.register(Whats)
admin.site.register(Skill)
admin.site.register(Image_Protfolio)

@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'subject']
    list_display_links = ['id', 'name']
    search_fields = ['name']