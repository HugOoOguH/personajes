from django.shortcuts import render
from django.views.generic import View
from .models import Post, Comentario
from django.contrib.auth.models import User
from .forms import PostForm, ComentarioForm

# Create your views here.
class ListView(View):
	
	def get(self, request):
		template_name = 'blog.html'
		user = User.objects.get(username="alucard")
		posts = user.blog_posts.all()
		
		#posts = Post.objects.filter(status='draft')
		#posts = Post.objects.all()
		context = {
			'entradas':posts
		}
		return render(request,template_name,context)


class DetailView(View):
	def get(self,request,slug):
		template_name = "detalle.html"
		form = ComentarioForm()
		post = Post.objects.get(slug=slug)
		#######
		forms = Comentario.objects.filter(slugC=slug)
		#######
		context = {
		'post':post,
		'form':form,
		'entradas':forms
		}
		return render(request,template_name,context)

	def post (self,request,slug):
		postss = Post.objects.get(slug=slug)
		forms = Comentario.objects.filter(slugC=slug)
		form = ComentarioForm()
		form = ComentarioForm(request.POST)
		post = form.save(commit=False)
		post.autor = request.user
		post.slugC = slug
		post.tituloC = postss.titulo
		post.save()
		#form.save()

		template_name = 'detalle.html'
		context ={
		'post':postss,
		'form':form,
		'entradas':forms,
		'guardado':True,
		}
		return render(request,template_name,context)


class NuevoPost(View):
	def get(self,request):
		form = PostForm()
		template_name = 'nuevo.html'
		context = {
		'form':form
		}
		return render(request,template_name,context)

	def post (self,request):
		form = PostForm(request.POST)
		post = form.save(commit=False)
		post.autor = request.user
		post.save()
		#form.save()

		template_name = 'nuevo.html'
		context ={
		'guardado':True,
		}
		return render(request,template_name,context)
#		print(request.POST.get('titulo'))
#		titulo = request.POST.get('titulo')
#		cuerpo = request.POST.get('cuerpo')
#		post = Post()
#		post.titulo = titulo
#		post.cuerpo = cuerpo
#		try:
#			post.autor = request.user
#		except:
#			pass
#		post.save()
		

#		template_name = 'nuevo.html'
#		context = {'guardado':True}
#
#		return render(request,template_name,context)
#
#class Blog(View):
#	
#	def get(self, request):
#		template_name = 'blog.html'
#		user = User.objects.get(username="alucard")
#		posts = user.blog_posts.all()
#		
#		#posts = Post.objects.filter(status='draft')
#		#posts = Post.objects.all()
#		context = {
#			'entradas':posts
#		}
#		return render(request,template_name,context)
		