from django.contrib import admin
from JokeRaterApp.models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name')

class JokeAdmin(admin.ModelAdmin):
    list_display = ('content','rating','datePosted','reportFlag')

# class CategoryAdmin(admin.ModelAdmin):
    # prepopulated_fields = {'slug':('name',)}
        
admin.site.register(Category)
admin.site.register(Joke)
admin.site.register(UserProfile)
