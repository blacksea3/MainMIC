# coding: utf-8

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response

from LCD12864.models import Word

import datetime

def index(request):
    c = {}
    c.update({'Words':Word.objects.all()})
    return render_to_response('LCD12864/index.html',c)

# Create your views here.
def search(request):
    line = request.GET.get('line','')
    column = request.GET.get('column','')
    tword = Word.objects.filter(index = line + ' ')
    if tword:
        tword=tword[0]
        return HttpResponse(tword.content)
    else:
        return HttpResponse('NONE')

def update_database(request):
    f1 = open('12864LiquidCrystalIndex.txt','r')   
    lines = f1.readlines()
    #for temp1 in lines:
    #    print temp1
    #    #temp1 = f1.readline()
    #    #if temp1 == '':
    #   #    break
    #    Word(vowel = "",edittime = datetime.datetime.now(),state=1,content=temp1[5:],
    #        index=temp1[:5],title="",ttype=0).save()
    f1.close()
    return HttpResponse('OK')