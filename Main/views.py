from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from Main.forms import NameFileForm
from Main.models import NameFile

from Main.models import ExcelDate
from Main.forms import ExcelDateForm

from django.http import FileResponse

from ReviewComposerV2.settings import MEDIA_ROOT
import mimetypes
import os
import sys
HttpResponseRedirect.allowed_schemes.append('e')
#from pythonCollection.FINAL import XeroRequestsBoth
from pythonCollection.formatter import file_asker, delete_rows_below_net_profit, director_renumeration
from pythonCollection.ACCOUNTCODES import MakeSheet

import pandas as pd 
import numpy as np


# Create your views here.
def index(request):
    return render(request,'home.html')

def uploaded(request):
    if request.method == "POST":
        global NAME
        global WHOLE
        print('akidhkasd')
        form = NameFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            name = str(file)
            NAME = name
            modelObj = NameFile(file=file, name=name)
            modelObj.save()
            print(NAME)
            print(MEDIA_ROOT)
            #XeroRequestsBoth()
            #p = os.path.abspath("pythonCollection")
            #sys.path.append(p)
            #from formatter import file_asker
            print(NAME.replace(' ','_').replace('&',''))
            NAME = NAME.replace(' ','_').replace('&','')
            try:
                f = open(os.path.join(os.getcwd(),'media','output',NAME.replace('PDF','xlsx').replace('pdf','xlsx')), "x")
                WHOLE = os.path.join(os.getcwd(),'media','output',NAME.replace('PDF','xlsx').replace('pdf','xlsx'))
            except : 
                print('okay')
                WHOLE = os.path.join(os.getcwd(),'media','output',NAME.replace('PDF','xlsx').replace('pdf','xlsx'))
            print(WHOLE)
            nn = os.path.join(os.getcwd(),'media','docs',NAME)
            file_asker(nn,NAME.replace('PDF','xlsx').replace('pdf','xlsx'))
            print(os.path.join(os.getcwd(),'media','output',NAME.replace('PDF','xlsx').replace('pdf','xlsx')))
            delete_rows_below_net_profit(os.path.join(os.getcwd(),'media','output',NAME.replace('PDF','xlsx').replace('pdf','xlsx')))
            director_renumeration()

            return HttpResponseRedirect('download',)
        else:
            return HttpResponse('FORM INVALID!!')
    else:
        return HttpResponse('Hiya')  
    
def download(request):

    if request.method == 'POST':
        
        print('HAHAHAHA GOT IT!')
        print(WHOLE)
        return FileResponse(open(WHOLE, 'rb'), as_attachment=True)

    context = {
         'path' : WHOLE
    }
    return render(request, 'download.html',context)


def goats(request):
    return render(request,'goats.html')

def accmaker(request):
    return render(request,'accmaker.html')





def uploadedacc(request):
    if request.method == "POST":
        global NAMEacc
        global WHOLEacc
        form = ExcelDateForm(request.POST,request.FILES)
        print(form.is_valid())
        if form.is_valid():
            print('Its Valid!')
            file = form.cleaned_data['excel_sheet']
            date = form.cleaned_data['end_date']
            NAMEacc = str(file)
            modelObj = ExcelDate(end_date=date,excel_sheet=file)
            modelObj.save()
            print(NAMEacc)
            print(MEDIA_ROOT)

            OPPATHacc = os.path.join(os.getcwd(),'media','excel',NAMEacc)
            WHOLEacc = os.path.join(os.getcwd(),'media','acc_output',NAMEacc)
            print(WHOLEacc)
            sheet = MakeSheet(DATE=date,PATH_OPEN=OPPATHacc,PATH_SAVE=WHOLEacc)
            sheet.to_csv(WHOLEacc.replace('xlsx','csv'), header=False, index=False)
            return HttpResponseRedirect("/downloadacc")
        else:
            print(form.errors)
            return HttpResponse("Form Invalid!!")
        return HttpResponse('Hey Man!!')
    else:
        return HttpResponse('Hiya')  
    
def downloadacc(request):

    if request.method == 'POST':
        
        print('HAHAHAHA GOT IT!')
        print(WHOLEacc)
        return FileResponse(open(WHOLEacc.replace('xlsx','csv'), 'rb'), as_attachment=True)

    context = {
         'path' : WHOLEacc.replace('xlsx','csv')
    }
    return render(request, 'downloadacc.html',context)