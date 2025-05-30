from django.contrib import admin

from . import models

class NotesAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'created_at', 'updated_at')



admin.site.register(models.Note, NotesAdmin)