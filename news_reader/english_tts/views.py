# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader

# >>> Baidu TTS
import requests
import sys
import json
import regex

IS_PY3 = sys.version_info.major == 3
if IS_PY3:
    from urllib.request import urlopen
    from urllib.request import Request
    from urllib.error import URLError
    from urllib.parse import urlencode
    from urllib.parse import quote_plus
else:
    import urllib2
    from urllib import quote_plus
    from urllib2 import urlopen
    from urllib2 import Request
    from urllib2 import URLError
    from urllib import urlencode

# API_KEY = '4E1BG9lTnlSeIf1NQFlrSq6h'
API_KEY = 'XWRTt6KfulGHpZNVky1Q2yjQ'
# SECRET_KEY = '544ca4657ba8002e3dea3ac2f5fdd241'
SECRET_KEY = 'dGww9QOXLrHZHuVc6P5lpDewlj9Arf0B'


def fetch_token(TOKEN_URL, SCOPE):
    '''
    TOKEN_URL = 'http://openapi.baidu.com/oauth/2.0/token'
    SCOPE = 'audio_tts_post'  # 有此scope表示有tts能力，没有请在网页里勾选
    '''
    # print("fetch token begin")
    params = {'grant_type': 'client_credentials',
              'client_id': API_KEY,
              'client_secret': SECRET_KEY}
    post_data = urlencode(params)
    if (IS_PY3):
        post_data = post_data.encode('utf-8')
    req = Request(TOKEN_URL, post_data)
    try:
        f = urlopen(req, timeout=5)
        result_str = f.read()
    except URLError as err:
        print('token http response http code : ' + str(err.code))
        result_str = err.read()
    if (IS_PY3):
        result_str = result_str.decode()

    # print(result_str)
    result = json.loads(result_str)
    # print(result)
    if ('access_token' in result.keys() and 'scope' in result.keys()):
        if not SCOPE in result['scope'].split(' '):
            raise Exception('scope is not correct')
        print('SUCCESS WITH TOKEN: %s ; EXPIRES IN SECONDS: %s' % (
            result['access_token'], result['expires_in']))
        return result['access_token']
    else:
        raise Exception(
            'MAYBE API_KEY or SECRET_KEY not correct: access_token or scope not found in token response')


# <<< Baidu TTS


def index(request):
    template = loader.get_template('tts.html')


    sentence_1 = 'President Bush meets with Russian President Putin in Moscow'
    sentence_2 = "Baidu started a business 18 years ago and caught up with the Internet."

    sentence_3 = "Baidu started a business 18 years ago and caught up with the Internet. In 2000, there were only 10 million Internet users in China. Today, internet users in China are over 800 million. The impact of AI on society, will be far more than the Internet, over the past 20 years, we all feel the Internet brings convenience to us. In the next few decades, we'll experience AI's impact on society more deeply."


    # auido urls

    # Baidu started a business
    url1 = 'http://tsn.baidu.com/text2audio?tex=Baidu%2Bstarted%2Ba%2Bbusiness&tok=24.960c66ace78789a9a389649a5e936bc9.2592000.1543099285.282335-14336126&lan=zh&aue=3&ctp=1&cuid=123456PYTHON&vol=5&pit=5&spd=7&per=0'

    # 18 years ago
    url2 = 'http://tsn.baidu.com/text2audio?tex=18%2Byears%2Bago&tok=24.960c66ace78789a9a389649a5e936bc9.2592000.1543099285.282335-14336126&lan=zh&aue=3&ctp=1&cuid=123456PYTHON&vol=5&pit=5&spd=7&per=0###'

    # and caught up with the Internet
    url3 = 'http://tsn.baidu.com/text2audio?tex=and%2Bcaught%2Bup%2Bwith%2Bthe%2BInternet.&tok=24.960c66ace78789a9a389649a5e936bc9.2592000.1543099285.282335-14336126&lan=zh&aue=3&ctp=1&cuid=123456PYTHON&vol=5&pit=5&spd=7&per=0'


    context = {
        # 'english_sentence': 'this is an English sentence!'
        'english_sentence': sentence_2,
        'audio_array': [url1, url2, url3]
    }

    # >>> Baidu TTS

    # 发音人选择, 0为普通女声，1为普通男生，3为情感合成-度逍遥，4为情感合成-度丫丫，默认为普通女声
    # PER = 4
    PER = 0
    # 语速，取值0-15，默认为5中语速
    SPD = 7
    # 音调，取值0-15，默认为5中语调
    PIT = 5
    # 音量，取值0-9，默认为5中音量
    VOL = 5
    # 下载的文件格式, 3：mp3(default) 4： pcm-16k 5： pcm-8k 6. wav
    AUE = 3
    FORMATS = {3: "mp3", 4: "pcm", 5: "pcm", 6: "wav"}
    FORMAT = FORMATS[AUE]

    CUID = "123456PYTHON"

    TTS_URL = 'http://tsn.baidu.com/text2audio'

    TOKEN_URL = 'http://openapi.baidu.com/oauth/2.0/token'
    SCOPE = 'audio_tts_post'  # 有此scope表示有tts能力，没有请在网页里勾选

    try:
        TEXT = sentence_2
        good = TEXT.encode('utf-8')
        token = fetch_token(TOKEN_URL, SCOPE)
        tex = quote_plus(good)
        params = {'tok': token, 'tex': tex, 'per': PER, 'spd': SPD, 'pit': PIT, 'vol': VOL,
                  'aue': AUE, 'cuid': CUID,
                  'lan': 'en', 'ctp': 1}
        data = urlencode(params)
        cur_audio_url = TTS_URL + '?' + data
        # print 'TEXT'
        # print TEXT
        print 'cur_audio_url'
        print cur_audio_url
        # context['top_five_cards'].append(
        #     {
        #         'text': TEXT,
        #         'pic_url': top_five[i]['mblog']['pics'][0]['url'],
        #         'width': top_five[i]['mblog']['pics'][0]['geo']['width'],
        #         'height': top_five[i]['mblog']['pics'][0]['geo']['height'],
        #         'tts_url': cur_audio_url
        #     }
        # )
        # count += 1
        # context['count'] = count
        # if count == 5:
        #     # context['count'] = 5
        #     break
    except Exception as e:
        print 'Exception'
        print e

    # <<< Baidu TTS

    return HttpResponse(template.render(context, request))
