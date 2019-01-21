from django.shortcuts import render
from django.http import HttpResponse
# from  import another
from helloutil.hello import hello
# from Farewell2016.Greet import farewell

# Create your views here.
def index(request):
  msg = hello('aaa')
  # msg = 'aaa'
  # msg = farewell()
  return HttpResponse(msg)
