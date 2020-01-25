from django.http import HttpResponse



def home(request,number):
	expression="The Number is pass "+str(number)
	return HttpResponse(expression)