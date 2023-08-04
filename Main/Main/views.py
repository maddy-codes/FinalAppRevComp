from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from Main.forms import NameFileForm
from Main.models import NameFile
from ReviewComposerV2.settings import MEDIA_ROOT
import mimetypes
import os
HttpResponseRedirect.allowed_schemes.append('e')

NAME = ''

# Create your views here.
def index(request):
    return render(request,'home.html')

def uploaded(request):
    if request.method == "POST":
        form = NameFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            name = str(file)
            NAME = name
            modelObj = NameFile(file=file, name=name)
            modelObj.save()
            print(NAME)
            print(MEDIA_ROOT)
            
            return HttpResponseRedirect('download')
        else:
            return HttpResponse('FORM INVALID!!')
    else:
        return HttpResponse('Hiya')  
    

def download(request):
    return render(request, 'download.html')