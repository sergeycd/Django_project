from django.http import HttpResponse
# from django.template import loader
from django.shortcuts import render

# Create your views here.
def index(request):
    # template = loader.get_template('about/index.html')
    # return HttpResponse(template.render({},request))
    return render(request,'about/index.html')
