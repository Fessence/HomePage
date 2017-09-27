# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from HPAdmin import models

def index(request):

    ret = {'movie':models.IndexMovieInfo.objects.all(),'banner':models.IndexBanerInfo.objects.filter(status=1)}
    return render(request, 'index.html',ret)

def information(request):
    return render(request,'information.html')

def case(request):
    return render(request,'case.html')

def about(request):
    return render(request,'about.html')