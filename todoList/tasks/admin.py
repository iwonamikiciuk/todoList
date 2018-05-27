from django.contrib import admin
from .models import Category,Task



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (            #daje kolory
        'name',
        'color'
    )
    search_fields = (
        'name',             #daje pole wyszzukiwania
    )



@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass