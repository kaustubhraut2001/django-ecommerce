
from django.urls import path , include
from . import views

urlpatterns = [
	path('' , views.productlist , name = 'home'),
	path('register/' , views.register , name = 'register')

]
