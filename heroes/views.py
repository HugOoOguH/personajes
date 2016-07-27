from django.shortcuts import render, HttpResponse
from django.views.generic import View


# Create your views here.
class Spider(View):
	def get(self, request):
		template_name = 'home.html'
		pers = marvel()
		img = pers['data']['results'][0]['thumbnail']['path']
		#ext = pers['data']['results'][0]['thumbnail']['extension']
		#img = img + "." + ext
		img = img + '.jpg'

		context = {
		'desc':pers['data']['results'][0]['description'],
		'name':pers['data']['results'][0]['name'],
		'imgs':img,
		}

		print(context['desc'])
		return render(request,template_name,context)
		#HttpResponse()
		#return HttpResponse(desc)

def marvel():
	import requests
	import hashlib
		#sup = input('Que superheroe te interesa?')
	ts = '1'
	public_key = 'ba76cf4bfef24ead8b24d96295110d32'
	private_key = '6b310f4dc243f0f7a472a95214665c57849d872b'
	ha = hashlib.md5((ts+private_key+public_key).encode()).hexdigest()
	url = 'http://gateway.marvel.com/v1/public/'
	personaje = requests.get(
		url+'characters',
	params = {
	'apikey': public_key,
	'ts':ts,
	'hash':ha,
	'name':'hulk'
	}).json()
	description = personaje['data']['results'][0]['description']
	#print(description)
	return personaje