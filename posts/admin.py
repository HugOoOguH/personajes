from django.contrib import admin

# Register your models here.
from .models import Post, Comentario

class PostAdmin(admin.ModelAdmin):
	list_display = (
		'titulo',
		'slug',
		'status',
		'creado',
		)

	list_filter = ('status','creado','actualizado')
	search_fields = ('titulo','cuerpo','creado','slug')
	prepopulated_fields = {'slug':('titulo',)}
	date_hierchy = 'creado'
	ordering = ['creado','status']

class ComentarioAdmin(admin.ModelAdmin):
	list_display = (
		'cuerpo',
		'fecha',
		)

	list_filter = ('autor','cuerpo','fecha')
	search_fields = ('autor','cuerpo')
	date_hierchy = 'fecha'
		


admin.site.register(Post, PostAdmin)
admin.site.register(Comentario, ComentarioAdmin)
#admin.site.register(Post)