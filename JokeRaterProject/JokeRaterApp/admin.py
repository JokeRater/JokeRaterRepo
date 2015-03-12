from django.contrib import admin
from JokeRaterApp.models import *

# class PageAdmin(admin.ModelAdmin):
    # list_display = ('title', 'category', 'url')

# class CategoryAdmin(admin.ModelAdmin):
    # prepopulated_fields = {'slug':('name',)}
        
admin.site.register(Category)
admin.site.register(Joke)
admin.site.register(UserProfile)
