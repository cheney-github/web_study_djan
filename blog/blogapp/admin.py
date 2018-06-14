from django.contrib import admin
from .models import Page,Wenzhang
# Register your models here.

class date_show_type(admin.ModelAdmin):
    list_display = ('title','pic','update',)


class wen_show(admin.ModelAdmin):
    list_display = ('biaoti','zhengwen')


admin.site.register(Page,date_show_type,)
admin.site.register(Wenzhang,wen_show,)