# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('tts.html')


    sentence_1 = 'President Bush meets with Russian President Putin in Moscow'
    sentence_2 = "Baidu started a business 18 years ago and caught up with the Internet. In 2000, there were only 10 million Internet users in China. Today, internet users in China are over 800 million. The impact of AI on society, will be far more than the Internet, over the past 20 years, we all feel the Internet brings convenience to us. In the next few decades, we'll experience AI's impact on society more deeply."

    context = {
        # 'english_sentence': 'this is an English sentence!'
        'english_sentence': sentence_2
    }

    return HttpResponse(template.render(context, request))
