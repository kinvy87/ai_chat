##@Kinvy 2019.09.11
import math
import jieba
import requests
import time
import pygame
from datetime import datetime
from aip import AipSpeech
from pyaudio import PyAudio, paInt16
import wave
# import os
# import synonyms
from conf.config import *

framerate = 7000
NUM_SAMPLES = 1500
channels = 1
sampwidth = 2
TIME = 2

import sys
import random
import synonyms

from conf.config import DIR_PATH


def save_wave_file(filename, data):
    '''save the date to the wavfile'''
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(sampwidth)
    wf.setframerate(framerate)
    wf.writeframes(b"".join(data))
    wf.close()


def my_record():
    pa = PyAudio()
    stream = pa.open(format=paInt16, channels=1,
                     rate=framerate, input=True,
                     frames_per_buffer=NUM_SAMPLES)
    my_buf = []
    count = 0
    while count < TIME * 6:  # 控制录音时间
        string_audio_data = stream.read(NUM_SAMPLES)
        my_buf.append(string_audio_data)
        count += 1
        print('.')
    save_wave_file('0001.wav', my_buf)
    stream.close()


##def play():
##    wf=wave.open(r"D:/41125.mp3",'rb')
##    p=PyAudio()
##    stream=p.open(format=p.get_format_from_width(wf.getsampwidth()),channels=
##    wf.getnchannels(),rate=wf.getframerate(),output=True)
##    while True:
##        data=wf.readframes(chunk)
##        if data=="":break
##        stream.write(data)
##    stream.close()
##    p.terminate()
#

APP_ID = '17160989'
API_KEY = 'G65EjCBPKcDP1tgILd00GN1c'

SECRET_KEY = 'Yx0GGtuz64Mj1wrQcWqdXLzWk8Is5OBe'
aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


def getText(url):
    text = requests.post(url).json()
    return text['text']


##图灵
##key = '6ddc57c5761a4c62a30ea840e5ae163f'
# api = 'http://www.tuling123.com/openapi/api?key=' + key +'&info ='
key = '7d99d7037ce3481cb895079b265a6b64'
api = 'http://www.tuling123.com/openapi/api?key=' + key + '&info=1d828ab4a31580e7'


#初始启动提示
pygame.mixer.init()
track = pygame.mixer.music.load(r"../voice_answer/喵喵.mp3")
pygame.mixer.music.play()


k = 0
while k <= 2:

    #录音启动提示
    pygame.mixer.init()
    track = pygame.mixer.music.load(r"../voice_answer/叮零.mp3")
    pygame.mixer.music.play()
    time.sleep(1)

    my_record()
    print("录音完成")


    def get_file_content(filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()

    content = get_file_content('0001.wav ')
    try:
        a = aipSpeech.asr(content,'wav', 8000, {})
    except:
        a = ""
    print(a)
    try:
        b = str(a['result'])
    except:
        b = ""
        k += 1 #连续3次不回应就停止

    # 每次都要重置info
    info = ""
    info = b

    if info !="":
        j=0
        score_max = 0
        n = len(conversation)
        for i in range(n):
            if i % 2 == 0:
                con = conversation[i]
                score = synonyms.compare(con + "?", info)
                if score >= score_max:
                    score_max = score
                    j = i + 1
                    k = 0  # 重置为0
        if score_max == 0:
            j = 1

    elif info == "":
        j = 1


    #图灵机器人
    # url = api + info
    # # print(url)
    #
    # text_01 = getText(url)
    # print("机器人回\n", text_01)
    #
    # now = datetime.now().strftime("%Y-%m-%d_%H_%M_%S")
    # filename_01 = "./record/" + now + ".mp3"
    #
    # result = aipSpeech.synthesis(text_01, 'zh', 1, {'vol': 5, 'per': 2})
    #
    # if not isinstance(result, dict):
    #     with open(filename_01, 'wb') as f:
    #         f.write(result)
    # print("--------------------------------------")
    # time.sleep(1)

    # print("语音1")
    # file = filename_01



    #使用本地录音文件
    if k <= 2:
        answer = conversation[j]
    else:
        answer = conversation[-1]

    if answer in ("孤独","舒服","求抱抱","睡觉中"):
        code = str(random.randint(0,2))
        answer = answer + code

    file = DIR_PATH + r'voice_answer\\' + answer + '.mp3'

    track = pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    time.sleep(3)
    pygame.mixer.music.stop()
    pygame.quit()
    if answer =="拜拜":
        break