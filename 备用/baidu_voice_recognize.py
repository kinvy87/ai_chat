# -*- coding: UTF-8 -*-
import base64
import requests
import urllib
import json
import wave
from conf.config import BaiDu_API_Key_GetVoi, BaiDu_Secret_Key_GetVoi,Baidu_Asr_Url


# 获取百度API调用的认证，实时生成，因为有时间限制
def getToken():
    # token认证的url
    api_url = "https://openapi.baidu.com/oauth/2.0/token?" \
                     "grant_type=client_credentials&client_id=%s&client_secret=%s"
    token_url = api_url % (BaiDu_API_Key_GetVoi, BaiDu_Secret_Key_GetVoi)
    r_str = urllib.request.urlopen(token_url).read()
    token_data = json.loads(r_str)
    token_str = token_data['access_token']
    return token_str



# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def wav_to_text(wav_file):
    try:
        speech_data= get_file_content(wav_file)
        speech_base64=base64.b64encode(speech_data).decode('utf-8')
        speech_length=len(speech_data)

    except IOError:
        print(u'文件错误!')
        return
    data = {"format": "wav",
            "token": getToken(),
            "len": speech_length,
            "rate": 8000,
            "speech": speech_base64,
            "cuid": '24057753', # 随意
            "channel": 1}
    data = json.dumps(data)
    headers = {
        'Content-Type': 'application/json',
    }
    r = requests.post(url=Baidu_Asr_Url, json=data, headers=headers)
    r = r.json()
    print(r)

if __name__ == '__main__':
    wav_to_text('/voice_say/say_voice.wav')













if 0:
    # -*- coding: utf-8 -*-
    # @Time : 2021/4/24 20:50
    # @File : baidu_voice_service.py
    # @Author : Rocky C@www.30daydo.com

    import os
    import time

    import requests
    import sys
    import pickle
    sys.path.append('..')
    from conf.config import BaiDu_API_Key,BaiDu_Secret_Key
    from base64 import b64encode
    from pathlib import PurePath
    import subprocess

    BASE = PurePath(__file__).parent

    # 需要识别的文件
    # 文件格式
    # 文件后缀只支持 pcm/wav/amr 格式，极速版额外支持m4a 格式

    CUID = '24057753' # 随意
    # 采样率
    RATE = 16000  # 固定值


    ASR_URL = 'http://vop.baidu.com/server_api'

    #测试自训练平台需要打开以下信息， 自训练平台模型上线后，您会看见 第二步：“”获取专属模型参数pid:8001，modelid:1234”，按照这个信息获取 dev_pid=8001，lm_id=1234
    '''
    http://vop.baidu.com/server_api
    1537	普通话(纯中文识别)	输入法模型	有标点	支持自定义词库
    1737	英语	英语模型	无标点	不支持自定义词库
    1637	粤语	粤语模型	有标点	不支持自定义词库
    1837	四川话	四川话模型	有标点	不支持自定义词库
    1936	普通话远场
    '''
    DEV_PID = 1737

    SCOPE = 'brain_enhanced_asr'  # 有此scope表示有asr能力，没有请在网页里开通极速版


    class DemoError(Exception):
        pass


    TOKEN_URL = 'http://openapi.baidu.com/oauth/2.0/token'

    def fetch_token():

        params = {'grant_type': 'client_credentials',
                  'client_id': BaiDu_API_Key,
                  'client_secret': BaiDu_Secret_Key}
        r = requests.post(
            url=TOKEN_URL,
            data=params
        )

        result = r.json()
        if ('access_token' in result.keys() and 'scope' in result.keys()):
            if SCOPE and (not SCOPE in result['scope'].split(' ')):  # SCOPE = False 忽略检查
                raise DemoError('scope is not correct')

            return result['access_token']

        else:
            raise DemoError('MAYBE API_KEY or SECRET_KEY not correct: access_token or scope not found in token response')


    """  TOKEN end """

    def dump_token(token):
        with open(os.path.join(BASE,'token.pkl'),'wb') as fp:
            pickle.dump({'token':token},fp)

    def load_token(filename):

        if not os.path.exists(filename):
            token=fetch_token()
            dump_token(token)
            return token
        else:
            with open(filename,'rb') as fp:
                token = pickle.load(fp)
                return token['token']

    def recognize_service(token,filename):
        FORMAT = filename[-3:]
        with open(filename, 'rb') as speech_file:
            speech_data = speech_file.read()

        length = len(speech_data)
        if length == 0:
            raise DemoError('file %s length read 0 bytes' % filename)

        b64_data = b64encode(speech_data)
        params = {'cuid': CUID, 'token': token, 'dev_pid': DEV_PID,'speech':b64_data,'len':length,'format':FORMAT,'rate':RATE,'channel':1}

        headers = {
            'Content-Type':'application/json',
        }
        r = requests.post(url=ASR_URL,json=params,headers=headers)
        return r.json()

    def rate_convertor(filename):
        filename = filename.split('.')[0]
        CMD=f'ffmpeg.exe -y -i {filename}.mp3 -ac 1 -ar 16000 {filename}.wav'
        try:
            p=subprocess.Popen(CMD, stdin=subprocess.PIPE)
            p.communicate()
            time.sleep(1)
        except Exception as e:
            print(e)
            return False,None
        else:
            return True,f'{filename}.wav'

    def clear(file):
        try:
            os.remove(file)
        except Exception as e:
            print(e)

    def get_voice_text(audio_file):

        filename = 'token.pkl'
        token = load_token(filename)
        convert_status,file = rate_convertor(audio_file)
        clear(file)
        if not convert_status:
            return None

        result = recognize_service(token,file)

        return result['result'][0]

    if __name__ == '__main__':
        get_voice_text('/voice_say/say_voice.wav')