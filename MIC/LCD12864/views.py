# coding: utf-8

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response

from LCD12864.models import *

import datetime

def index(request):
    c = {}
    c.update({'Words':LineWord.objects.all()})
    return render_to_response('LCD12864/index.html',c)

def search(request):
    line = request.GET.get('row','')
    #column = request.GET.get('col','')
    string = request.GET.get('string','')
    #如果不按字符串查找，则默认按行查找
    if string=='':
        tword = LineWord.objects.filter(index = line + ' ')
        if tword:
            tword=tword[0]
            return HttpResponse(tword.content)
        else:
            tword = LineWord.objects.filter(index = line + '0 ')
            if tword:
                tword=tword[0]
                return HttpResponse(tword.content[2:])
            else:
                return HttpResponse(u'没有此行')
    else:
        QueryResult = []
        UseResult = ''
        for x in string:
            tword = DetailWord.objects.filter(content=x)
            if tword:
                QueryResult.append(tword[0].index)
            else:
                QueryResult.append('XXXX')
        if 'XXXX' in QueryResult:
            UseResult = 'NOTFOUND, OR SOMETHING ERROR'
            return HttpResponse(UseResult)
        else:
            first = 1
            for x in QueryResult:
                if first == 1:
                    first = 0
                else:
                    UseResult = UseResult + ','
                UseResult = UseResult + '0x' + x[:2] + ',0x' + x[2:]
            return HttpResponse(UseResult)

def update_database(request):
    #f1 = open('12864LiquidCrystalIndex.txt','r')   
    #lines = f1.readlines()
    #for temp1 in lines:
    #    LineWord(vowel = "",edittime = datetime.datetime.now(),state=1,content=temp1[5:],
    #        index=temp1[:5],title="",ttype=0).save()
    #f1.close()

    AllLines = LineWord.objects.all()

    LocTable = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

    for Line in AllLines:
        TempLine = Line.content.split(' ')[1:-1]
        PreIndex = Line.index[:-2]
        Loc = 0
        #raise Exception(PreIndex + LocTable[Loc])
        for TempWord in TempLine:
            DetailWord(edittime = datetime.datetime.now(),state=1,content=TempWord,
                index=PreIndex + LocTable[Loc],keyword='',ttype=0).save()
            Loc = Loc + 1

    return HttpResponse('OK')