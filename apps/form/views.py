from django.shortcuts import render, HttpResponse, redirect
from django.db import models
from models import Form


# Create your views here.
def index(request):
	spring = Form.objects.all()
	context = {'spring':spring}

	if 'like' in request.session:
		return render(request, "form/index.html",context)
	else:
		request.session['like'] = 0
		return render(request, "form/index.html")

def process(request, methods='POST'):

	if request.method == "POST":
		Form.objects.create(secret = request.POST['secret'])

	return redirect ('/')

def remove(request, id):

	this = Form.objects.get(id=id)
	if request.method == "GET":
		context = {'spring':this}
		return render(request, "form/index.html", context)

	this.delete()	
	return redirect ('/')

def like(request, id):
	this = Form.objects.get(id=id)
	if request.POST['action'] == 'like':
		request.session['like'] = request.session['like'] + 1
	
	return redirect ('/')