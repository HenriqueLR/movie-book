#encoding: utf-8

from django.template import Library

register = Library()

@register.filter(name='addcss')
def addcss(value, arg):
	return value.as_widget(attrs={'class': arg})


@register.filter(name='placeholder')
def placeholder(value, token):
	value.field.widget.attrs["placeholder"] = token
	return value

@register.filter(name='textar')
def textar(value, arg):
	value.field.widget.attrs["rows"] = arg
	return value	