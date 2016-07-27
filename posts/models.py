from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class Post(models.Model):

	STATUS_CHOICES = (
			('draft','Draft'),
			('published','Published'),
		)

	autor = models.ForeignKey(User, related_name="blog_posts",blank=True,null=True)
	titulo = models.CharField(max_length=100,blank=True,null=True)
	cuerpo = models.TextField(blank=True,null=True)
	#fecha = models.DateTimeField(auto_now=True)
	#fecha = models.DateField(auto_now=True)
	creado = models.DateTimeField(auto_now=True,blank=True,null=True)
	actualizado = models.DateTimeField(auto_now_add=True,blank=True,null=True)
	status= models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft',blank=True,null=True)
	slug = models.SlugField(max_length=200, unique_for_date='creado',blank=True,null=True)

	class Meta:
		ordering = ('-creado',)

	def __str__(self):
		return self.titulo
 

	def get_absolute_url(self):
		return reverse('posts:detalle',args=[self.pk])

	def get_absolute_url2(self):
		return reverse('posts:detalle',args=[self.slug])

class Comentario(models.Model):
	autor = models.ForeignKey(User, related_name="comments")
	cuerpo = models.TextField()
	fecha= models.DateTimeField(auto_now=True)
	activo = models.BooleanField(default=True)
	tituloC = models.CharField(max_length=100,blank=True,null=True)
	slugC = models.CharField(max_length=200,blank=True,null=True)

	####Agregar formulario abajo de cada post 