
from django.urls import path , include
from . import views

urlpatterns = [
	path('' , views.productlist , name = 'productspage'),
	path('register/' , views.register , name = 'register')

]
