#encoding: utf-8

from django.conf.urls import include, url, patterns

urlpatterns = patterns('movies.views',
	url(r'^$','index', name='home'),
	url(r'^agendar/(?P<pk>\d+)$','add_scheduled_movie', name='scheduled_movie'),
	url(r'^apagar_filme/(?P<pk>\d+)$','movie_delete', name='delete_movie'),
	url(r'^editar_filme/(?P<pk>\d+)$', 'update_movie', name='edit_movie'),
	url(r'^novo_filme/$','add_movie', name='create_movie'),
)