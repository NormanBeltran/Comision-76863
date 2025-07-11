from django.contrib import admin

from .models import *

class GenderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    readonly_fields = ('created', 'updated')

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    readonly_fields = ('created', 'updated')

class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'pelicula', 'premiere', 'estrellas', 'sinopsis')
    readonly_fields = ('created', 'updated')
    list_filter = ('genders', 'rating')
    ordering = ('-rating',)


# Register your models here.
admin.site.register(Company, CompanyAdmin)
admin.site.register(Gender, GenderAdmin)
admin.site.register(Movie, MovieAdmin)