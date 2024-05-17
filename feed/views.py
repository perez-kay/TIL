from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

class HomePageView(ListView):
	template_name = 'feed/home.html'
	model = Post
	http_method_names = ['get']
	context_object_name = 'posts'
	queryset = Post.objects.all().order_by('-id')[0:30]

class PostDetailView(DetailView):
	template_name = "feed/detail.html"
	model = Post
	context_object_name = "post"

class CreateNewPost(LoginRequiredMixin, CreateView):
	model = Post
	template_name = 'feed/create.html'
	fields = ['text']
	success_url = "/"


	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.author = self.request.user
		obj.save()
		return super().form_valid(form)
	
	def post(self, request, *args, **kwargs):
		post = Post.objects.create(
			text=request.POST.get("text"),
			author=request.user
		)
		return render(
			request,
			"includes/post.html",
			{
				"post": post,
				"show_detail_link": True
			},
			content_type="application/html"
		)
	