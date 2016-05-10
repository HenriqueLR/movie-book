#encoding: utf-8

from core.models import Movies
from movies.forms import MovieForm, ScheduledMoviesForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.db.models.deletion import ProtectedError



def add_scheduled_movie(request, pk):
	'''
	This function responsive tratament create new scheduled movie.
	'''	
	template = 'movies/scheduled_movie.html'
	movie = get_object_or_404(Movies, pk=pk)
	form = ScheduledMoviesForm(request.POST or None)

	if form.is_valid():
		form.save()
		form = ScheduledMoviesForm()
		messages.success(request, 'Agendado com sucesso.')
	context = {'movie': movie,'form': form,}

	return render(request,template, context)



class MoviesListView(ListView):
	'''
	this class is responsible for returning the lists of Movies.
	'''
	model = Movies
	paginate_by = 12
	template_name = 'movies/list_movies.html'

	def get_queryset(self):
		qs = Movies.objects.filter(status=True)
		search = self.request.GET.get('search', '')
		if search != '':
			qs = qs.filter(name__icontains=search)
		return qs		



class MovieAddView(CreateView):
	'''
	This class responsive tratament create new Movie.
	'''
	model = Movies
	form_class = MovieForm
	template_name = 'movies/create_movie.html'
	success_url = reverse_lazy('movies:create_movie')

	def get_context_data(self, **kwargs):
		context = super(MovieAddView, self).get_context_data(**kwargs)
		contact_list = self.get_queryset()

		paginator = Paginator(contact_list, 12)
		try: 
			page = self.request.GET.get("page",'1')
		except ValueError: 
			page = 1

		try:
			contact_list = paginator.page(page)
		except (InvalidPage, EmptyPage):
			contact_list = paginator.page(paginator.num_pages)

		context.update({'object_list':contact_list,'page_obj': contact_list}) 
		return context    



class MovieEditView(UpdateView):
	'''
	This class is responsible treatment edit Movie.
	'''
	model = Movies
	form_class = MovieForm
	template_name = 'movies/edit_movie.html'
	success_url = reverse_lazy('movies:create_movie')

	def form_valid(self, form):
		self.object = form.save()
		messages.success(self.request, 'Alterado com sucesso.')
		return HttpResponseRedirect(self.object.get_update_url())



class MovieDeleteView(DeleteView):
	'''
	This class is responsible for making treatment to exclude a single object
	Movies.
	'''
	model = Movies
	template_name = 'movies/movie_confirm_delete.html'
	success_url = reverse_lazy('movies:create_movie')

	def delete(self, request, *args, **kwargs):
		self.object = self.get_object()
		try:
			self.object.delete()
			messages.success(self.request, 'Filme apagado.')
		except ProtectedError:
			messages.error(self.request, 'Você não pode apagar este Filme, foi agendado para assistir')
		return HttpResponseRedirect(self.success_url)


index = MoviesListView.as_view()
add_movie = MovieAddView.as_view()
update_movie = MovieEditView.as_view()
movie_delete = MovieDeleteView.as_view()