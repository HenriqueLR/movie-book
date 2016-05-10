#encoding: utf-8

from django import forms
from core.models import Movies, ScheduledMovies



class MovieForm(forms.ModelForm):
    '''
    This class is responsible generator form MovieForm.
    '''
    class Meta:
        model = Movies

class ScheduledMoviesForm(forms.ModelForm):
    '''
    This class is responsible generator form ScheduledMoviesForm.
    '''
    class Meta:
        model = ScheduledMovies