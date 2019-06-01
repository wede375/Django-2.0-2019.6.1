#from django.http import HttpResponse

from django.shortcuts import render

def abc(request):
	return render(request,'abc.html')