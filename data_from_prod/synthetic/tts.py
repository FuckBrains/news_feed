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
DEFAULT_DEMO_TEXT = "美国加利福尼亚州北部山火确认遇难人数12日升至42人，成为这个西部州致死人数最多的山火，甚至可能是一个世纪以来美国最夺命的山火。最致命.这场山火8日开始，所获命名为“坎普”。加州比尤特县治安官科里·哈尼亚12日说，新确认13人遇难，“坎普”火灾遇难者总数因而升至42人。“这是加州历史上死者最多的山火”，他说，“史无前例”。加州先前致死人数最多的单一山火发生在1933年，29人在洛杉矶格里菲斯公园火灾中遇难。去年秋季，加州北部一系列山火致死44人，烧毁超过5000座房屋。"
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
