import pygame
from chatterbot import ChatBot
import requests
import json
from conf.config import *
import time
import os
import random
import urllib.request
import base64
import sys
import synonyms


# 初始化百度返回的音频文件地址，后面会变为全局变量，随需改变
mp3_url = DIR_PATH + r'voice_answer\voice_ss.mp3'

cat = 0


# 播放Mp3文件
def play_mp3():
    # 接受服务器的消息
    pygame.mixer.init()
    if cat == 0:
        pygame.mixer.music.load(mp3_url)  #使用本地文件(文字生成语音文件的路径,然后再播放该路径的文件)
    elif cat == 1:
        pygame.mixer.music.load(mp3_url.replace("voices", "voice_answer"))  # 使用本地预先存储的猫叫文件,路径是自己设置的
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(1)
    pygame.mixer.music.stop()
    pygame.mixer.quit()


# 删除声音文件
def remove_voice():
    # path = DIR_PATH + "voice_answer"
#     # for i in os.listdir(path):
#     #     path_file = os.path.join(path, i)
#     #     try:
#     #         os.remove(path_file)
#     #     except:
#     #         continue
    pass


# 图灵自动回复
def tuling(info):
    url = tuling_url + "?key=%s&info=%s" % (tuling_app_key, info)
    content = requests.get(url, headers=headers)
    answer = json.loads(content.text)
    return answer['text']


# 聊天机器人回复
def chatbot(info):
    my_bot = ChatBot("", read_only=True,
                     database="./db.sqlite3")
    score_max = 0
    n = len(conversation)
    for i in range(n):
        if i%2 == 0:
            con = conversation[i]
            score = synonyms.compare(con, info)
            if score > score_max:
                score_max = score
                info = con
            else:
                score_max = score_max
                info = info

    if score_max ==0 or info == "invalid audio length":
        info = "小喵你给我撒个娇。"

    res = my_bot.get_response(info)
    return str(res)


# 百度讲文本转为声音文件保存在本地 tts地址，无需token实时认证
def baidu_api(answer):
    api_url = '{11}?idx={0}&tex={1}&cuid={2}&cod={3}&lan={4}&ctp={5}&pdt={6}&spd={7}&per={8}&vol={9}&pit={10}'\
        .format(baidu_api_set["idx"], answer, baidu_api_set["cuid"], baidu_api_set["cod"], baidu_api_set["lan"],
                baidu_api_set["ctp"], baidu_api_set["pdt"], baidu_api_set["spd"], baidu_api_set["per"],
                baidu_api_set["vol"], baidu_api_set["pit"], baidu_api_url)
    res = requests.get(api_url, headers=headers2)
    # 本地Mp3语音文件保存位置
    iname = random.randrange(1, 99999)
    global mp3_url,cat

    # n = len(conversation)
    # for i in range(n):
    #     con = conversation[i]
    #     similarity = synonyms.compare(con, answer, seg=True)
    #     if similarity >0.6:
    #         answer = con

    if answer in conversation and conversation.index(answer)%2 !=0:
        time.sleep(1)  #延迟恢复，减弱机器人的感觉
        cat = 1         #激活预先保存的猫叫文件

        mp3_url = DIR_PATH + r'voices\voice_tts' + answer + '.mp3'

    else:
        cat = 0
        # mp3_url = DIR_PATH + r'voices\voice_tts' + str(iname) + '.mp3'
        mp3_url = DIR_PATH + r'voices\voice_tts' + "喵呜" + '.mp3'  #表示没听懂
    with open(mp3_url, 'wb') as f:
        f.write(res.content)


# 百度讲文本转为声音文件保存在本地 方法2 tsn地址
def baidu_api2(answer):
    # 获取access_token
    token = getToken()
    get_url = baidu_api_url2 % (urllib.parse.quote(answer), "test", token)
    voice_data = urllib.request.urlopen(get_url).read()
    # 本地Mp3语音文件保存位置
    name = random.randrange(1, 99999)
    global mp3_url
    mp3_url = DIR_PATH + r'voice_answer\voice_tsn' + str(name) + '.mp3'
    voice_fp = open(mp3_url, 'wb+')
    voice_fp.write(voice_data)
    voice_fp.close()
    return


# 百度语音转文本
def getText(filename):
    # 获取access_token
    token = getToken()
    data = {}
    data['format'] = 'wav'
    # data['rate'] = 16000
    data['rate'] = 800
    data['channel'] = 1
    data['cuid'] = str(random.randrange(123456, 999999))
    data['token'] = token
    wav_fp = open(filename, 'rb')
    voice_data = wav_fp.read()
    data['len'] = len(voice_data)
    data['speech'] = base64.b64encode(voice_data).decode('utf-8')
    post_data = json.dumps(data)
    # 语音识别的api url
    upvoice_url = 'http://vop.baidu.com/server_api'
    r_data = requests.post(url=upvoice_url, json=data, headers=headers)
    err = json.loads(r_data)['err_no']
    if err == 0:
        return json.loads(r_data)['result'][0]
    else:
        return json.loads(r_data)['err_msg']


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


