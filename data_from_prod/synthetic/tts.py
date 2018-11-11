# coding=utf-8
"""
TTS service
"""
import sys
import json
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
API_KEY = 'n2sumqaNTdNzE0ihuGbTh2Q4'
SECRET_KEY = 'TONSBa9FdyYCGjIAzfiSaM9lGc1KyQqP'
# DEFAULT_DEMO_TEXT = "欢迎使用百度语音合成。"
DEFAULT_DEMO_TEXT = "英雄联盟：恭喜IG战队喜提冠军，网友：“7年了，我们回来了”！hello大家好，很高兴各位见面了，本期给大家带来《英雄联盟》总决赛的最新内容。北京时间11月3日下午，英雄联盟S8世界总决赛巅峰对决曲在韩国仁川体育场拉开帷幕。经过三个小时的激烈战斗，来自中国战区的IG级战队，最终以3:0的优势强力碾压了欧洲大佬Fnatic战队，荣获世界冠军!"
# 发音人选择, 0为普通女声，1为普通男生，3为情感合成-度逍遥，4为情感合成-度丫丫，默认为普通女声
PER = 3
# 语速，取值0-15，默认为5中语速
SPD = 5
# 音调，取值0-15，默认为5中语调
PIT = 5
# 音量，取值0-9，默认为5中音量
VOL = 5
# 下载的文件格式, 3：mp3(default) 4： pcm-16k 5： pcm-8k 6. wav
AUE = 3
# The default is mp3. If changed, we need to update the save file format
FORMATS = {3: "mp3", 4: "pcm", 5: "pcm", 6: "wav"}
FORMAT = FORMATS[AUE]
CUID = "123456PYTHON"
TTS_URL = 'http://tsn.baidu.com/text2audio'
class DemoError(Exception):
    """
    Demo Error: Used to identify API key or secret key error
    """
    pass
"""  TOKEN start """
TOKEN_URL = 'http://openapi.baidu.com/oauth/2.0/token'
SCOPE = 'audio_tts_post'  # 有此scope表示有tts能力，没有请在网页里勾选
def fetch_token():
    """
    Fetch the needed token to use Baidu AI services.
    :return:
    """
    print("fetch token begin")
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
    print(result_str)
    result = json.loads(result_str)
    print(result)
    if ('access_token' in result.keys() and 'scope' in result.keys()):
        if not SCOPE in result['scope'].split(' '):
            raise DemoError('scope is not correct')
        print('SUCCESS WITH TOKEN: %s' % result['access_token'])
        return result['access_token']
    else:
        raise DemoError('MAYBE API_KEY or SECRET_KEY not correct')
"""  TOKEN end """
def fetch_tts(text, destination):
    """
    Use Baidu AI service to compose an audio file from texts.
    :param text: Compose this string into an audio file
    :param destination: Save the audio file to this destination
    :return:
    """
    token = fetch_token()
    tex = quote_plus(text)  # 此处TEXT需要两次urlencode
    print(tex)
    params = {'tok': token, 'tex': tex, 'per': PER, 'spd': SPD, 'pit': PIT, 'vol': VOL,
              'aue': AUE, 'cuid': CUID, 'lan': 'zh', 'ctp': 1}  # lan ctp 固定参数
    data = urlencode(params)
    print('test on Web Browser: ' + TTS_URL + '?' + data)
    req = Request(TTS_URL, data.encode('utf-8'))
    has_error = False
    try:
        f = urlopen(req)
        result_str = f.read()
        has_error = ('Content-Type' not in f.headers or
                     f.headers['Content-Type'].find('audio/') < 0)
    except  URLError as err:
        print('asr http response http code : ' + str(err.code))
        result_str = err.read()
        has_error = True
    save_file = "error.txt" if has_error else destination
    with open(save_file, 'wb') as of:
        of.write(result_str)
    if has_error:
        if (IS_PY3):
            result_str = str(result_str, 'utf-8')
        print("tts api  error:" + result_str)
    print("result saved as :" + save_file)
if __name__ == '__main__':
    fetch_tts(DEFAULT_DEMO_TEXT, 'result.mp3')
