from django.contrib import admin
from news.models import News

class NewsAdmin(admin.ModelAdmin):
    list_display=('title','details')

# Register your models here.
admin.site.register(News,NewsAdmin)