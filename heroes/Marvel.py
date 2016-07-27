import requests
import hashlib

class PachuMarvel(object):
	def __init__(self,public_key='ba76cf4bfef24ead8b24d96295110d32',private_key = '6b310f4dc243f0f7a472a95214665c57849d872b'):
		self.public_key = public_key
		self.private_key = private_key
		ts = '1'
		self.ha = hashlib.md5((ts+private_key+public_key).encode()).hexdigest()
		self.url = 'http://gateway.marvel.com/v1/public/'

		self.nombre = ''
		self.description = ''
		self.img = ''
		self.personaje = None
		self.ide = ''



	def get_personaje(self, nombre="hulk"):

		try:
			self.personaje = requests.get(
				self.url+'characters',
					params={
					'apikey':self.public_key,
					'ts':'1',
					'hash':self.ha,
					'name':nombre
					}).json()
			self.nombre = nombre
			self.description = self.personaje['data']['results'][0]['description']
			self.img = self.personaje['data']['results'][0]['thumbnail']['path']
			print("Bien")

		except Exception as e:
			print("Escribiste mal el personaje")
	
	def get_response(self):
		"""Este metodo puede ser llamado despues deget_personaje"""
		try:
			print(self.personaje)
		except:
			print("Algo salio mal")

	def get_id(self):
		try:
			self.ide = self.personaje['data']['results'][0]['id']
			print(self.ide)
		except:
			print("llama primero a get_personaje tonto")
	