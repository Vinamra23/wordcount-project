"""wordcount URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
	return render(request,'home.html')


def count(request):
	fulltext = request.GET['fulltext']
	wordlist = fulltext.split()

	worddictionary = {}

	for word in wordlist:
		if word in worddictionary:
			worddictionary[word] += 1
		else:
			worddictionary[word] = 1
			
	return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist),'worddictionary':worddictionary.items()})	
 
def about(request):
	return render(request,'about.html')



