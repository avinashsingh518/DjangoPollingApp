from django.contrib import admin
from . models import Question, Choice

# Register your models here.

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('question', 'option', 'vote')
    search_fields = ('option',)
    list_filter = ('vote',)

admin.site.register(Question)
admin.site.register(Choice,ChoiceAdmin)