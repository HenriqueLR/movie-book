#encoding: utf-8

from django.db import models
from core.tasks import async_email



class Directors(models.Model):
	'''
	This class is responsible for mapping the directors table.
	'''	
	id_director = models.AutoField(primary_key=True, verbose_name=u'Cod Diretor', db_column='id_director')
	name = models.CharField(max_length=100, verbose_name=u'Nome', db_column='name', unique=True)
	description = models.TextField(verbose_name=u'Descrição', db_column='description',blank=True,
		null=True, default='')
	created_at = models.DateTimeField(auto_now_add=True, db_column='created_at', blank=False, verbose_name=u'Criado em')
	updated_at = models.DateTimeField(verbose_name=u'Atualizado em', auto_now=True, db_column='updated_at')

	def __unicode__(self):
		return u'%s' % self.name

	class Meta:
		verbose_name=u'Diretor'
		verbose_name_plural=u'Diretores'
		db_table='director'
		ordering=['id_director']



class Movies(models.Model):
	'''
	This class is responsible for mapping the movies table.
	'''
	id_movie = models.AutoField(primary_key=True, verbose_name=u'Cod Filme', db_column='id_movie')
	name = models.CharField(max_length=100, verbose_name=u'Nome', db_column='name', unique=True)
	director = models.ForeignKey(Directors, verbose_name=u'Diretor', related_name='movies_director', 
		on_delete=models.PROTECT)
	note = models.IntegerField(verbose_name='Nota', db_column='note', blank=True, null=True,
		default=0)
	img = models.ImageField(upload_to='img/movies')
	description = models.TextField(verbose_name=u'Descrição', db_column='description',blank=True,
		null=True, default='')
	status = models.BooleanField(verbose_name=u'Status', db_column='status', default=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True, db_column='created_at', blank=False, verbose_name=u'Criado em')
	updated_at = models.DateTimeField(verbose_name=u'Atualizado em', auto_now=True, db_column='updated_at')


	def __unicode__(self):
		return u'%s' % self.name

	@models.permalink
	def get_delete_url(self):
		return ('movies:delete_movie', [int(self.pk)], {})

	@models.permalink
	def get_update_url(self):
		return ('movies:edit_movie', [int(self.pk)], {})		


	class Meta:
		verbose_name=u'Filme'
		verbose_name_plural=u'Filmes'
		db_table='movies'
		ordering=['id_movie']



class ScheduledMovies(models.Model):
	'''
	This class is responsible for mapping the ScheduledMovies table.
	'''
	id_scheduled_movie = models.AutoField(primary_key=True, verbose_name=u'Cod Agendamento', db_column='id_scheduled_movie')
	name = models.CharField(max_length=100, verbose_name=u'Nome', db_column='name')
	movie = models.ForeignKey(Movies, verbose_name=u'Filme', related_name='scheduled_movies', 
		on_delete=models.PROTECT)
	created_at = models.DateTimeField(db_column='created_at', blank=False, verbose_name=u'Data')

	def __unicode__(self):
		return u'%s' % self.name

	class Meta:
		verbose_name=u'Agendamento'
		verbose_name_plural=u'Agendamentos'
		db_table='scheduled_movies'
		ordering=['id_scheduled_movie']



def post_save_reply(created, instance, **kwargs):
	async_email.delay(instance)
	
models.signals.post_save.connect(
	post_save_reply, sender=ScheduledMovies, dispatch_uid='post_save_reply'
)			