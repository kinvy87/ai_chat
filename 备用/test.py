import struct
import pyaudio
import pvporcupine

#porcupine = pvporcupine.create(ke/ywords=['porcupine', 'ok google', "picovoice", "blueberry"])
porcupine = pvporcupine.create(keyword_paths=['samel__en_windows_2021-10-26-utc_v1_9_0.c'])

pa = pyaudio.PyAudio()

audio_stream = pa.open(
                    rate=porcupine.sample_rate,
                    channels=1,
                    format=pyaudio.paInt16,
                    input=True,
                    frames_per_buffer=porcupine.frame_length)

#def get_next_audio_frame():
#  return


while True:
    pcm = audio_stream.read(porcupine.frame_length)
    pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)
    keyword_index = porcupine.process(pcm)
    if keyword_index >= 0:
        # Insert detection event callback here
        print("sdfsa")


# import playsound

# playsound.playsound(r'weather_forecast.mp3')
# playsound.playsound(r'if_continue.mp3')

# import re
#
#
# result = "的好机会继续"
# yes_word = re.findall(r"[继续|是|嗯]", result)
# yes_len = len(yes_word)
# if yes_len >= 1:
#     flag = 1


# !/usr/bin/env python
# -*- coding: utf-8 -*-

# import requests
# # import os
#
# def TTS(text, speed, lan, per):
#     """普通话-音色：
#           标准女音
#           标准男音
#           斯文男音
#           小萌萌
#           知性女音
#           老教授
#           葛平音
#           播音员
#           京腔
#           温柔大叔
#        英式英语-音色：
#           标准音
#        美式英语-音色：
#           标准音
#        粤语-音色：
#           标准音
#     """
#     convertTable = {  # 建立易读文本和音色码/语言码的关系表
#         '中文': ('ZH', {
#             '标准女音': 0,
#             '标准男音': 1,
#             '斯文男音': 3,
#             '小萌萌': 4,
#             '知性女音': 5,
#             '老教授': 6,
#             '葛平音': 8,
#             '播音员': 9,
#             '京腔': 10,
#             '温柔大叔': 11
#         }),
#         '英式英语': ('UK', {
#             '标准音': 0
#         }),
#         '美式英语': ('EN', {
#             '标准音': 0
#         }),
#         '粤语': ('CTE', {
#             '标准音': 0
#         })
#     }
#     data = {
#         'tex': text,
#         'spd': speed,
#         'lan': convertTable[lan][0],
#         'per': convertTable[lan][1][per],
#         'ctp': 1,
#         'cuid': 'baike',
#         'ie': 'UTF-8',
#         'pdt': 301,
#         'vol': 9,
#         'rate': 32
#     }
#     result = requests.get('https://tts.baidu.com/text2audio', params=data)
#     try:
#         result.json()
#     except:
#         return result.content
#     else:
#         raise ValueError
#
#
# if __name__ == '__main__':
#     try:
#         bindata = TTS('''测试一下，你好世界！''', 5, '中文', '小萌萌')
#     except:
#         print('Error')
#     else:
#         with open('result.mp3', 'wb+') as f:
#             f.write(bindata)  # 在同级目录写入为mp3文件
#         # os.startfile('result.mp3')     #自动运行生成的mp3