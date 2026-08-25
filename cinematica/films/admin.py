from django.contrib import admin

# Register your models here.
from .models import Film, Director
admin.site.register(Film)
admin.site.register(Director)