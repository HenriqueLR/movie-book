#encoding: utf-8

from django.contrib import admin
from .models import Movies, Directors, ScheduledMovies

admin.site.register(Movies)
admin.site.register(Directors)
admin.site.register(ScheduledMovies)
