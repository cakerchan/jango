# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from jk.models import Content,Contenten
from django.core.paginator import Paginator
from django.core.cache import cache
from django.db.models import Q
from django.views.decorators.cache import cache_page
import re
#@cache_page(60 * 172800)
def index(request):
    a = Content.objects.order_by('-datime')
    p = Paginator(a,15)
    pagenr = p.page(1)
    pagens =  int('1')
    pagern =xrange(1,10)
    allpage = p.num_pages
    context = {
        'allpage': allpage,
        'pagens': pagens,
        'pagenr':pagenr,
        'pagern':pagern,
    }
    return render(request,'index.html',context)
#@cache_page(60 * 172800)
def pageindex(request,pagen):
    a = Content.objects.order_by('-datime')
    p = Paginator(a, 15)
    allpage = p.num_pages
    if pagen == '':
        pagen = '1'
    pagens =  int(pagen)
    pagenr = p.page(pagens)
    front = 5
    back = 4
    if pagens > front:
        if pagens+back<allpage:
            ranl = xrange(pagens - front, pagens + back)
        else:
            ranl = xrange(allpage-9, allpage+1)
    else:
        ranl = xrange(1,back+pagens)
    pagern = ranl
    context = {
        'allpage':allpage,
        'pagens':pagens,
        'pagenr':pagenr,
        'pagern':pagern
    }
    return render(request,'pageindex.html',context)
#@cache_page(60 * 172800)
def IdeesG(request):
    c = Content.objects.order_by('-datime').filter(category='idees')
    p = Paginator(c,15)
    pagenr = p.page(1)
    pagens =  int('1')
    pagern =xrange(1,10)
    allpage = p.num_pages
    context = {
        'allpage': allpage,
        'pagens': pagens,
        'pagenr':pagenr,
        'pagern':pagern,

    }

    return render(request, 'idees/idees.html', context)
#@cache_page(60 * 172800)
def Ideespage(request,pagen):
    a = Content.objects.order_by('-datime').filter(category='idees')
    p = Paginator(a, 15)
    allpage = p.num_pages
    if pagen == '':
        pagen = '1'
    pagens =  int(pagen)
    pagenr = p.page(pagens)
    front = 4
    back = 5
    if pagens > front:
        if pagens+back<allpage:
            ranl = xrange(pagens - front, pagens + back)
        else:
            ranl = xrange(allpage-9, allpage+1)
    else:
        ranl = xrange(1,back+pagens)

    pagern = ranl

    context = {
        'allpage':allpage,
        'pagens':pagens,
        'pagenr':pagenr,
        'pagern':pagern
    }
    return render(request,'idees/ideespage.html',context)
#@cache_page(60 * 172800)
def Ideesw(request,id):
    a = Content.objects.get(id=id)#通过url传入值
    b = Content.objects.order_by('?').filter(category='idees')[:10]
    abc =  a.article
    aaa = abc
    bd = a.img
    name = bd
    contexts = {
        'name':name,
        'b':b,
        'a':a,
        'aaa':aaa,
    }
    return render(request,'idees/ideesw.html',contexts)
#@cache_page(60 * 172800)
def SportG(request):
    c = Content.objects.order_by('-datime').filter(category='sport')
    p = Paginator(c,15)
    pagenr = p.page(1)
    pagens =  int('1')
    pagern =xrange(1,10)
    allpage = p.num_pages
    context = {
        'allpage': allpage,
        'pagens': pagens,
        'pagenr':pagenr,
        'pagern':pagern,

    }
    return render(request, 'sport/sport.html', context)
#@cache_page(60 * 172800)
def Sportpage(request,pagen):
    a = Content.objects.order_by('-datime').filter(category='sport')
    p = Paginator(a, 15)
    allpage = p.num_pages
    if pagen == '':
        pagen = '1'
    pagens =  int(pagen)
    pagenr = p.page(pagens)
    front = 4
    back = 5
    if pagens > front:
        if pagens+back<allpage:
            ranl = xrange(pagens - front, pagens + back)
        else:
            ranl = xrange(allpage-9, allpage+1)
    else:
        ranl = xrange(1,back+pagens)
    pagern = ranl
    context = {
        'allpage':allpage,
        'pagens':pagens,
        'pagenr':pagenr,
        'pagern':pagern
    }
    return render(request,'sport/sportpage.html',context)
#@cache_page(60 * 172800)
def Sportw(request,id):
    a = Content.objects.get(id=id)
    b = Content.objects.order_by('?').filter(category='sport')[:10]
    abc =  a.article
    aaa = abc
    bd = a.img
    name = bd
    contexts = {
        'name':name,
        'b':b,
        'a':a,
        'aaa':aaa,
    }
    return render(request,'sport/sportw.html',contexts)
#@cache_page(60 * 172800)
def SocieteG(request):
    c = Content.objects.order_by('-datime').filter(category='societe')
    p = Paginator(c,15)
    pagenr = p.page(1)
    pagens =  int('1')
    pagern =xrange(1,10)
    allpage = p.num_pages
    context = {
        'allpage': allpage,
        'pagens': pagens,
        'pagenr':pagenr,
        'pagern':pagern,

    }

    return render(request, 'societe/societe.html', context)
#@cache_page(60 * 172800)
def Societepage(request,pagen):
    a = Content.objects.order_by('-datime').filter(category='societe')
    p = Paginator(a, 15)
    allpage = p.num_pages
    if pagen == '':
        pagen = '1'
    pagens =  int(pagen)
    pagenr = p.page(pagens)
    front = 4
    back = 5
    if pagens > front:
        if pagens+back<allpage:
            ranl = xrange(pagens - front, pagens + back)
        else:
            ranl = xrange(allpage-9, allpage+1)
    else:
        ranl = xrange(1,back+pagens)

    pagern = ranl
    context = {
        'allpage':allpage,
        'pagens':pagens,
        'pagenr':pagenr,
        'pagern':pagern
    }
    return render(request,'societe/societepage.html',context)
#@cache_page(60 * 172800)
def Societew(request,id):
    a = Content.objects.get(id=id)
    b = Content.objects.order_by('?').filter(category='societe')[:10]
    abc =  a.article
    aaa = abc
    bd = a.img
    name = bd
    contexts = {
        'name':name,
        'b':b,
        'a':a,
        'aaa':aaa,
    }
    return render(request,'societe/societew.html',contexts)
#@cache_page(60 * 172800)
def CultureG(request):
    c = Content.objects.order_by('-datime').filter(category='culture')
    p = Paginator(c,15)
    pagenr = p.page(1)
    pagens =  int('1')
    pagern =xrange(1,10)
    allpage = p.num_pages
    context = {
        'allpage': allpage,
        'pagens': pagens,
        'pagenr':pagenr,
        'pagern':pagern,
    }
    return render(request, 'culture/culture.html', context)
#@cache_page(60 * 172800)
def Culturepage(request,pagen):
    a = Content.objects.order_by('-datime').filter(category='culture')
    p = Paginator(a, 15)
    allpage = p.num_pages
    if pagen == '':
        pagen = '1'
    pagens =  int(pagen)
    pagenr = p.page(pagens)
    front = 4
    back = 5
    if pagens > front:
        if pagens+back<allpage:
            ranl = xrange(pagens - front, pagens + back)
        else:
            ranl = xrange(allpage-9, allpage+1)
    else:
        ranl = xrange(1,back+pagens)

    pagern = ranl
    context = {
        'allpage':allpage,
        'pagens':pagens,
        'pagenr':pagenr,
        'pagern':pagern
    }
    return render(request,'culture/culturepage.html',context)
#@cache_page(60 * 172800)
def Culturew(request,id):
    a = Content.objects.get(id=id)#通过url传入值
    b = Content.objects.order_by('?').filter(category='culture')[:10]
    abc =  a.article
    aaa = abc
    bd = a.img
    name = bd
    contexts = {
        'name':name,
        'b':b,
        'a':a,
        'aaa':aaa,
    }
    return render(request,'culture/culturew.html',contexts)
#@cache_page(60 * 172800)
def EconomieG(request):
    c = Content.objects.order_by('-datime').filter(category='economie')
    p = Paginator(c,15)
    pagenr = p.page(1)
    pagens =  int('1')
    pagern =xrange(1,10)
    allpage = p.num_pages
    context = {
        'allpage': allpage,
        'pagens': pagens,
        'pagenr':pagenr,
        'pagern':pagern,
    }
    return render(request, 'economie/economie.html', context)
#@cache_page(60 * 172800)
def Economiepage(request,pagen):
    a = Content.objects.order_by('-datime').filter(category='economie')
    p = Paginator(a, 15)
    allpage = p.num_pages
    if pagen == '':
        pagen = '1'
    pagens =  int(pagen)
    pagenr = p.page(pagens)
    front = 4
    back = 5
    if pagens > front:
        if pagens+back<allpage:
            ranl = xrange(pagens - front, pagens + back)
        else:
            ranl = xrange(allpage-9, allpage+1)
    else:
        ranl = xrange(1,back+pagens)
    pagern = ranl
    context = {
        'allpage':allpage,
        'pagens':pagens,
        'pagenr':pagenr,
        'pagern':pagern
    }
    return render(request,'economie/economiepage.html',context)
#@cache_page(60 * 172800)
def Economiew(request,id):
    a = Content.objects.get(id=id)#通过url传入值
    b = Content.objects.order_by('?').filter(category='economie')[:10]
    abc =  a.article
    aaa = abc
    bd = a.img
    name = bd
    contexts = {
        'name':name,
        'b':b,
        'a':a,
        'aaa':aaa,
    }
    return render(request,'economie/economiew.html',contexts)
#@cache_page(60 * 172800)
def EditorialG(request):
    c = Content.objects.order_by('-datime').filter(category='editorial')
    p = Paginator(c,15)
    pagenr = p.page(1)
    pagens =  int('1')
    pagern =xrange(1,10)
    allpage = p.num_pages
    context = {
        'allpage': allpage,
        'pagens': pagens,
        'pagenr':pagenr,
        'pagern':pagern,
    }
    return render(request, 'editorial/editorial.html', context)
#@cache_page(60 * 172800)
def Editorialpage(request,pagen):
    a = Content.objects.order_by('-datime').filter(category='editorial')
    p = Paginator(a, 15)
    allpage = p.num_pages
    if pagen == '':
        pagen = '1'
    pagens =  int(pagen)
    pagenr = p.page(pagens)
    front = 4
    back = 5
    if pagens > front:
        if pagens+back<allpage:
            ranl = xrange(pagens - front, pagens + back)
        else:
            ranl = xrange(allpage-9, allpage+1)
    else:
        ranl = xrange(1,back+pagens)
    pagern = ranl
    context = {
        'allpage':allpage,
        'pagens':pagens,
        'pagenr':pagenr,
        'pagern':pagern
    }
    return render(request,'editorial/editorialpage.html',context)
#@cache_page(60 * 172800)
def Editorialw(request,id):
    a = Content.objects.get(id=id)
    b = Content.objects.order_by('?').filter(category='editorial')[:10]
    abc =  a.article
    aaa = abc
    bd = a.img
    name = bd
    contexts = {
        'name':name,
        'b':b,
        'a':a,
        'aaa':aaa,
    }
    return render(request,'editorial/editorialw.html',contexts)
#@cache_page(60 * 172800)
def NationalG(request):
    c = Content.objects.order_by('-datime').filter(category='national')
    p = Paginator(c,15)
    pagenr = p.page(1)
    pagens =  int('1')
    pagern =xrange(1,10)
    allpage = p.num_pages
    context = {
        'allpage': allpage,
        'pagens': pagens,
        'pagenr':pagenr,
        'pagern':pagern,
    }
    return render(request, 'national/national.html', context)
#@cache_page(60 * 172800)
def Nationalpage(request,pagen):
    a = Content.objects.order_by('-datime').filter(category='national')
    p = Paginator(a, 15)
    allpage = p.num_pages
    if pagen == '':
        pagen = '1'
    pagens =  int(pagen)
    pagenr = p.page(pagens)
    front = 4
    back = 5
    if pagens > front:
        if pagens+back<allpage:
            ranl = xrange(pagens - front, pagens + back)
        else:
            ranl = xrange(allpage-9, allpage+1)
    else:
        ranl = xrange(1,back+pagens)
    pagern = ranl
    context = {
        'allpage':allpage,
        'pagens':pagens,
        'pagenr':pagenr,
        'pagern':pagern
    }
    return render(request,'national/nationalpage.html',context)
#@cache_page(60 * 172800)
def Nationalw(request,id):
    a = Content.objects.get(id=id)#通过url传入值
    b = Content.objects.order_by('?').filter(category='national')[:10]
    abc =  a.article
    aaa = abc
    bd = a.img
    name = bd
    contexts = {
        'name':name,
        'b':b,
        'a':a,
        'aaa':aaa,
    }
    return render(request,'national/nationalw.html',contexts)
#@cache_page(60 * 172800)
def SanteG(request):
    c = Content.objects.order_by('-datime').filter(category='sante')
    p = Paginator(c,15)
    pagenr = p.page(1)
    pagens =  int('1')
    pagern =xrange(1,10)
    allpage = p.num_pages
    context = {
        'allpage': allpage,
        'pagens': pagens,
        'pagenr':pagenr,
        'pagern':pagern,
    }
    return render(request, 'sante/sante.html', context)
#@cache_page(60 * 172800)
def Santepage(request,pagen):
    a = Content.objects.order_by('-datime').filter(category='sante')
    p = Paginator(a, 15)
    allpage = p.num_pages
    if pagen == '':
        pagen = '1'
    pagens =  int(pagen)
    pagenr = p.page(pagens)
    front = 4
    back = 5
    if pagens > front:
        if pagens+back<allpage:
            ranl = xrange(pagens - front, pagens + back)
        else:
            ranl = xrange(allpage-9, allpage+1)
    else:
        ranl = xrange(1,back+pagens)
    pagern = ranl
    context = {
        'allpage':allpage,
        'pagens':pagens,
        'pagenr':pagenr,
        'pagern':pagern
    }
    return render(request,'sante/santepage.html',context)
#@cache_page(60 * 172800)
def Santew(request,id):
    a = Content.objects.get(id=id)
    b = Content.objects.order_by('?').filter(category='sante')[:10]
    abc =  a.article
    aaa = abc
    bd = a.img
    name = bd
    contexts = {
        'name':name,
        'b':b,
        'a':a,
        'aaa':aaa,
    }
    return render(request,'sante/santew.html',contexts)
#@cache_page(60 * 172800)
def TicketmagG(request):
    c = Content.objects.order_by('-datime').filter(category='ticketmag')
    p = Paginator(c,15)
    pagenr = p.page(1)
    pagens =  int('1')
    pagern =xrange(1,10)
    allpage = p.num_pages
    context = {
        'allpage': allpage,
        'pagens': pagens,
        'pagenr':pagenr,
        'pagern':pagern,
    }
    return render(request, 'ticketmag/ticketmag.html', context)
#@cache_page(60 * 172800)
def Ticketmagpage(request,pagen):
    a = Content.objects.order_by('-datime').filter(category='ticketmag')
    p = Paginator(a, 15)
    allpage = p.num_pages
    if pagen == '':
        pagen = '1'
    pagens =  int(pagen)
    pagenr = p.page(pagens)
    front = 4
    back = 5
    if pagens > front:
        if pagens+back<allpage:
            ranl = xrange(pagens - front, pagens + back)
        else:
            ranl = xrange(allpage-9, allpage+1)
    else:
        ranl = xrange(1,back+pagens)
    pagern = ranl
    context = {
        'allpage':allpage,
        'pagens':pagens,
        'pagenr':pagenr,
        'pagern':pagern
    }
    return render(request,'ticketmag/ticketmagpage.html',context)
#@cache_page(60 * 172800)
def Ticketmagw(request,id):
    a = Content.objects.get(id=id)
    b = Content.objects.order_by('?').filter(category='ticketmag')[:10]
    abc =  a.article
    aaa = abc
    bd = a.img
    name = bd
    contexts = {
        'name':name,
        'b':b,
        'a':a,
        'aaa':aaa,
    }
    return render(request,'ticketmag/ticketmagw.html',contexts)






##@cache_page(60 * 172800)
def indexen(request):
    a = Contenten.objects.order_by('-datime')
    p = Paginator(a,15)
    pagenr = p.page(1)
    cache.clear()
    pagens =  int('1')
    pagern =xrange(1,10)
    allpage = p.num_pages
    context = {
        'allpage': allpage,
        'pagens': pagens,
        'pagenr':pagenr,
        'pagern':pagern,
    }
    return render(request,'indexen.html',context)
#@cache_page(60 * 172800)
def pageindexen(request,pagen):
    a = Contenten.objects.order_by('-datime')
    p = Paginator(a, 15)
    cache.clear()
    allpage = p.num_pages
    if pagen == '':
        pagen = '1'
    pagens =  int(pagen)
    pagenr = p.page(pagens)
    front = 5
    back = 4
    if pagens > front:
        if pagens+back<allpage:
            ranl = xrange(pagens - front, pagens + back)
        else:
            ranl = xrange(allpage-9, allpage+1)
    else:
        ranl = xrange(1,back+pagens)
    pagern = ranl
    context = {
        'allpage':allpage,
        'pagens':pagens,
        'pagenr':pagenr,
        'pagern':pagern
    }
    return render(request,'pageindexen.html',context)
#@cache_page(60 * 172800)
def Newsen(request):
    c = Contenten.objects.order_by('-datime').filter(category='news')
    p = Paginator(c,15)
    pagenr = p.page(1)
    pagens =  int('1')
    pagern =xrange(1,10)
    allpage = p.num_pages
    context = {
        'allpage': allpage,
        'pagens': pagens,
        'pagenr':pagenr,
        'pagern':pagern,

    }

    return render(request, 'newsp/newsen.html', context)
#@cache_page(60 * 172800)
def Newsenpage(request,pagen):
    a = Contenten.objects.order_by('-datime').filter(category='news')
    p = Paginator(a, 15)
    allpage = p.num_pages
    if pagen == '':
        pagen = '1'
    pagens =  int(pagen)
    pagenr = p.page(pagens)
    front = 4
    back = 5
    if pagens > front:
        if pagens+back<allpage:
            ranl = xrange(pagens - front, pagens + back)
        else:
            ranl = xrange(allpage-9, allpage+1)
    else:
        ranl = xrange(1,back+pagens)

    pagern = ranl

    context = {
        'allpage':allpage,
        'pagens':pagens,
        'pagenr':pagenr,
        'pagern':pagern
    }
    return render(request,'newsp/newsenpage.html',context)
#@cache_page(60 * 172800)
def Newsenw(request,id):
    a = Contenten.objects.get(id=id)#通过url传入值
    b = Contenten.objects.order_by('?').filter(category='news')[:10]
    abc =  a.article
    aaa = abc
    bd = a.img
    name = bd
    contexts = {
        'name':name,
        'b':b,
        'a':a,
        'aaa':aaa,
    }
    return render(request,'newsp/newsenw.html',contexts)
#@cache_page(60 * 172800)
def Politicsen(request):
    c = Contenten.objects.order_by('-datime').filter(category='politics')
    p = Paginator(c,15)
    pagenr = p.page(1)
    pagens =  int('1')
    pagern =xrange(1,10)
    allpage = p.num_pages
    context = {
        'allpage': allpage,
        'pagens': pagens,
        'pagenr':pagenr,
        'pagern':pagern,

    }
    return render(request, 'politicsp/politicsen.html', context)
#@cache_page(60 * 172800)
def Politicsenpage(request,pagen):
    a = Contenten.objects.order_by('-datime').filter(category='politics')
    p = Paginator(a, 15)
    allpage = p.num_pages
    if pagen == '':
        pagen = '1'
    pagens =  int(pagen)
    pagenr = p.page(pagens)
    front = 4
    back = 5
    if pagens > front:
        if pagens+back<allpage:
            ranl = xrange(pagens - front, pagens + back)
        else:
            ranl = xrange(allpage-9, allpage+1)
    else:
        ranl = xrange(1,back+pagens)
    pagern = ranl
    context = {
        'allpage':allpage,
        'pagens':pagens,
        'pagenr':pagenr,
        'pagern':pagern
    }
    return render(request,'politicsp/politicsenpage.html',context)
#@cache_page(60 * 172800)
def Politicsenw(request,id):
    a = Contenten.objects.get(id=id)
    b = Contenten.objects.order_by('?').filter(category='politics')[:10]
    cache.clear()
    abc =  a.article
    aaa = abc
    bd = a.img
    name = bd
    contexts = {
        'name':name,
        'b':b,
        'a':a,
        'aaa':aaa,
    }
    return render(request,'politicsp/politicsenw.html',contexts)
#@cache_page(60 * 172800)
def Businessen(request):
    c = Contenten.objects.order_by('-datime').filter(category='business')
    p = Paginator(c,15)
    cache.clear()
    pagenr = p.page(1)
    pagens =  int('1')
    pagern =xrange(1,10)
    allpage = p.num_pages
    context = {
        'allpage': allpage,
        'pagens': pagens,
        'pagenr':pagenr,
        'pagern':pagern,

    }

    return render(request, 'businessp/businessen.html', context)
#@cache_page(60 * 172800)
def Businessenpage(request,pagen):
    a = Contenten.objects.order_by('-datime').filter(category='business')
    p = Paginator(a, 15)
    cache.clear()
    allpage = p.num_pages
    if pagen == '':
        pagen = '1'
    pagens =  int(pagen)
    pagenr = p.page(pagens)
    front = 4
    back = 5
    if pagens > front:
        if pagens+back<allpage:
            ranl = xrange(pagens - front, pagens + back)
        else:
            ranl = xrange(allpage-9, allpage+1)
    else:
        ranl = xrange(1,back+pagens)

    pagern = ranl
    context = {
        'allpage':allpage,
        'pagens':pagens,
        'pagenr':pagenr,
        'pagern':pagern
    }
    return render(request,'businessp/businessenpage.html',context)
#@cache_page(60 * 172800)
def Businessenw(request,id):
    a = Contenten.objects.get(id=id)
    b = Contenten.objects.order_by('?').filter(category='business')[:10]
    abc =  a.article
    aaa = abc
    bd = a.img
    name = bd
    contexts = {
        'name':name,
        'b':b,
        'a':a,
        'aaa':aaa,
    }
    return render(request,'businessp/businessenw.html',contexts)
#@cache_page(60 * 172800)
def Opinionen(request):
    c = Contenten.objects.order_by('-datime').filter(category='opinion')
    p = Paginator(c,15)
    pagenr = p.page(1)
    pagens =  int('1')
    pagern =xrange(1,10)
    allpage = p.num_pages
    context = {
        'allpage': allpage,
        'pagens': pagens,
        'pagenr':pagenr,
        'pagern':pagern,
    }
    return render(request, 'opinionp/opinionen.html', context)
#@cache_page(60 * 172800)
def Opinionenpage(request,pagen):
    a = Contenten.objects.order_by('-datime').filter(category='opinion')
    p = Paginator(a, 15)
    allpage = p.num_pages
    if pagen == '':
        pagen = '1'
    pagens =  int(pagen)
    pagenr = p.page(pagens)
    front = 4
    back = 5
    if pagens > front:
        if pagens+back<allpage:
            ranl = xrange(pagens - front, pagens + back)
        else:
            ranl = xrange(allpage-9, allpage+1)
    else:
        ranl = xrange(1,back+pagens)

    pagern = ranl
    context = {
        'allpage':allpage,
        'pagens':pagens,
        'pagenr':pagenr,
        'pagern':pagern
    }
    return render(request,'opinionp/opinionenpage.html',context)
#@cache_page(60 * 172800)
def Opinionenw(request,id):
    a = Contenten.objects.get(id=id)#通过url传入值
    b = Contenten.objects.order_by('?').filter(category='opinion')[:10]
    abc =  a.article
    aaa = abc
    bd = a.img
    name = bd
    contexts = {
        'name':name,
        'b':b,
        'a':a,
        'aaa':aaa,
    }
    return render(request,'opinionp/opinionenw.html',contexts)
#@cache_page(60 * 172800)
def Techen(request):
    c = Contenten.objects.order_by('-datime').filter(category='tech')
    p = Paginator(c,15)
    pagenr = p.page(1)
    pagens =  int('1')
    pagern =xrange(1,10)
    allpage = p.num_pages
    context = {
        'allpage': allpage,
        'pagens': pagens,
        'pagenr':pagenr,
        'pagern':pagern,
    }
    return render(request, 'techp/techen.html', context)
#@cache_page(60 * 172800)
def Techenpage(request,pagen):
    a = Contenten.objects.order_by('-datime').filter(category='tech')
    p = Paginator(a, 15)
    allpage = p.num_pages
    if pagen == '':
        pagen = '1'
    pagens =  int(pagen)
    pagenr = p.page(pagens)
    front = 4
    back = 5
    if pagens > front:
        if pagens+back<allpage:
            ranl = xrange(pagens - front, pagens + back)
        else:
            ranl = xrange(allpage-9, allpage+1)
    else:
        ranl = xrange(1,back+pagens)
    pagern = ranl
    context = {
        'allpage':allpage,
        'pagens':pagens,
        'pagenr':pagenr,
        'pagern':pagern
    }
    return render(request,'techp/techenpage.html',context)
#@cache_page(60 * 172800)
def Techenw(request,id):
    a = Contenten.objects.get(id=id)#通过url传入值
    b = Contenten.objects.order_by('?').filter(category='tech')[:10]
    abc =  a.article
    aaa = abc
    bd = a.img
    name = bd
    contexts = {
        'name':name,
        'b':b,
        'a':a,
        'aaa':aaa,
    }
    return render(request,'techp/techenw.html',contexts)
#@cache_page(60 * 172800)
def Scienceen(request):
    c = Contenten.objects.order_by('-datime').filter(category='science')
    p = Paginator(c,15)
    pagenr = p.page(1)
    pagens =  int('1')
    pagern =xrange(1,10)
    allpage = p.num_pages
    context = {
        'allpage': allpage,
        'pagens': pagens,
        'pagenr':pagenr,
        'pagern':pagern,
    }
    return render(request, 'sciencep/scienceen.html', context)
#@cache_page(60 * 172800)
def Scienceenpage(request,pagen):
    a = Contenten.objects.order_by('-datime').filter(category='science')
    p = Paginator(a, 15)
    allpage = p.num_pages
    if pagen == '':
        pagen = '1'
    pagens =  int(pagen)
    pagenr = p.page(pagens)
    front = 4
    back = 5
    if pagens > front:
        if pagens+back<allpage:
            ranl = xrange(pagens - front, pagens + back)
        else:
            ranl = xrange(allpage-9, allpage+1)
    else:
        ranl = xrange(1,back+pagens)
    pagern = ranl
    context = {
        'allpage':allpage,
        'pagens':pagens,
        'pagenr':pagenr,
        'pagern':pagern
    }
    return render(request,'sciencep/scienceenpage.html',context)
#@cache_page(60 * 172800)
def Scienceenw(request,id):
    a = Contenten.objects.get(id=id)
    b = Contenten.objects.order_by('?').filter(category='science')[:10]
    abc =  a.article
    aaa = abc
    bd = a.img
    name = bd
    contexts = {
        'name':name,
        'b':b,
        'a':a,
        'aaa':aaa,
    }
    return render(request,'sciencep/scienceenw.html',contexts)
#@cache_page(60 * 172800)
def Healthen(request):
    c = Contenten.objects.order_by('-datime').filter(category='health')
    p = Paginator(c,15)
    pagenr = p.page(1)
    pagens =  int('1')
    pagern =xrange(1,10)
    allpage = p.num_pages
    context = {
        'allpage': allpage,
        'pagens': pagens,
        'pagenr':pagenr,
        'pagern':pagern,
    }
    return render(request, 'healthp/healthen.html', context)
#@cache_page(60 * 172800)
def Healthenpage(request,pagen):
    a = Contenten.objects.order_by('-datime').filter(category='health')
    p = Paginator(a, 15)
    allpage = p.num_pages
    if pagen == '':
        pagen = '1'
    pagens =  int(pagen)
    pagenr = p.page(pagens)
    front = 4
    back = 5
    if pagens > front:
        if pagens+back<allpage:
            ranl = xrange(pagens - front, pagens + back)
        else:
            ranl = xrange(allpage-9, allpage+1)
    else:
        ranl = xrange(1,back+pagens)
    pagern = ranl
    context = {
        'allpage':allpage,
        'pagens':pagens,
        'pagenr':pagenr,
        'pagern':pagern
    }
    return render(request,'healthp/healthenpage.html',context)
#@cache_page(60 * 172800)
def Healthenw(request,id):
    a = Contenten.objects.get(id=id)#通过url传入值
    b = Contenten.objects.order_by('?').filter(category='health')[:10]
    abc =  a.article
    aaa = abc
    bd = a.img
    name = bd
    contexts = {
        'name':name,
        'b':b,
        'a':a,
        'aaa':aaa,
    }
    return render(request,'healthp/healthenw.html',contexts)