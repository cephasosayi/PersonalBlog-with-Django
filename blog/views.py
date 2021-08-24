from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
# from django.contrib.auth.decorators import login_required, permission_required

from blog.models import Article, Author
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

# Create your views here.

class BlogListView(generic.ListView):
	model = Article
	paginate_by = 10

	def get_context_data(self, **kwaegs):
		context = super(BlogListView, self).get_context_data(**kwaegs)
		context['some_data'] = 'This is just some data'

		return context

class BlogDetailView(generic.DetailView):
	model = Article


class AuthorListView(generic.ListView):
	model = Author
	paginate_by = 10


	def get_context_data(self, **kwaegs):
		context = super(AuthorListView, self).get_context_data(**kwaegs)
		context['now'] = 'this is just some data'
		return context

class AuthorDetailView(generic.DetailView):
	models = Author
	context_object_name = 'author'
	queryset = Author.objects.all()
	# template_name = 'author_detail.html'


from django.views.generic.edit import CreateView, UpdateView, DeleteView
# @login_required
# @permission_required('blog.can_mark_returned', raise_exception=True)

class ArticleCreate(PermissionRequiredMixin, CreateView):
	Permission_required = 'blog.can_mark_returned'
	model = Article
	fields = ['title', 'description','author','category','photo','post_date']


class ArticleUpdate(PermissionRequiredMixin, UpdateView):
	Permission_required = 'blog.can_mark_returned'
	model = Article
	success_url = reverse_lazy('blog')

class ArticleDelete(PermissionRequiredMixin,DeleteView):
	permission_required = ('blog.can_mark_returned', 'blog.can_edit')
	model = Article
	success_url = reverse_lazy('blog')