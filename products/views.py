from django.shortcuts import render , redirect
from django.http import HttpResponse
import json
import requests
# Create your views here.


def productlist(request):
	data = requests.get('https://dummyjson.com/products')
	products = data.json()
	print(products["products"] , end='\n')

	return render(request , 'productspage.html' , {'products':products["products"]})


def register(request):
	return render(request , 'productspage.html')

def buynow(request , id):
	if request.method == 'POST':
		print("Controll is here")
		return redirect('sucesspage')
	else:
		return redirect('sucesspage')

def sucess(request):
	return render(request , 'sucess.html')
