from .models import Review
from django.contrib import admin

# Register your models here.

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title']

admin.site.register(Review, ReviewAdmin)