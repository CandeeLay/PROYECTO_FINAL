from django.http import HttpResponse
from django.template import Template, Context

def saludo(request):
	return HttpResponse('Hola Django - Coder')

def segunda_vista(request):
	return HttpResponse('<br><br>Ya entendimos')


