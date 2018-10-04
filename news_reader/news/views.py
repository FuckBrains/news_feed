# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

# def index(request):
#     return HttpResponse("Hello, world. You're at the 'aggregate and read' index.")

import requests

def index(request):
    template = loader.get_template('row.html')
    context = {
        'top_five_cards': [],
        'count': 0
    }
    print 'haha'
    import pdb;pdb.set_trace()
    renminribao_url = 'https://m.weibo.cn/api/container/getIndex?containerid=1076032803301701'
    # response = urllib2.urlopen(renminribao_url)
    # response = urllib2.urlopen('http://python.org/')
    #
    # html = response.read()
    r = requests.get(url=renminribao_url)
    data = r.json()
    top_five = data['data']['cards'][0:50]

    count = 0
    for i in range(0, len(top_five)):
        print 'i: ', i
        try:
            context['top_five_cards'].append(
                {
                    'text': top_five[i]['mblog']['text'],
                    'pic_url': top_five[i]['mblog']['pics'][0]['url'],
                    'width': top_five[i]['mblog']['pics'][0]['geo']['width'],
                    'height': top_five[i]['mblog']['pics'][0]['geo']['height'],
                }
            )
            count += 1
            context['count'] = count
            if count == 5:
                # context['count'] = 5
                break
        except Exception as e:
            print 'Exception'
            print e
            continue
    print 'to render'
    print context
    return HttpResponse(template.render(context, request))

