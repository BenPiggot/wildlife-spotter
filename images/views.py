from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect

# Create your views here.
def index(request):
  data = dict(
    username='ben'
  )
  print(data)
  return render(request, 'images/index.html', {'data': data} )