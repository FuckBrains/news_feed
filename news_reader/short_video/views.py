# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# def index(request):
#     return HttpResponse("Hello, world. You're at the 'aggregate and read' index.")

import requests
import sys
import json
import regex


# Create your views here.
def index(request):
    template = loader.get_template('short_video_phone.html')
    context = {
        'name': 'Daming',
    }

    return HttpResponse(template.render(context, request))
