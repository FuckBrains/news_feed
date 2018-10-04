# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

# def index(request):
#     return HttpResponse("Hello, world. You're at the 'aggregate and read' index.")


def index(request):
    template = loader.get_template('row.html')
    context = {
        'pass_in': "Daming",
    }
    print 'haha'
    return HttpResponse(template.render(context, request))

