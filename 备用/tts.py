import os
import time
import aip
import playsound
from conf.config import BaiDu_App_ID,BaiDu_API_Key,BaiDu_Secret_Key


def tts(text, sleep_time=3, audio_name="audio.mp3"):
    if os.path.exists(audio_name):
        os.remove(audio_name)  # 初始化环境
    a_obj = aip.AipSpeech(BaiDu_App_ID, BaiDu_API_Key, BaiDu_Secret_Key)
    audio_bin = a_obj.synthesis(text, 'zh', 1, {'vol': 4, 'spd': 5, 'pit': 5, 'per': 1})
    if not isinstance(audio_bin, dict):
        with open(audio_name, "wb") as hf:
            hf.write(audio_bin)
        play(audio_name, 1)
    else:
        print("文本：%s TTS失败，云服务返回异常" % text)
    time.sleep(sleep_time)


def play(audio_file, sleep_time=0.8):
    try:
        playsound.playsound(audio_file)
        time.sleep(sleep_time)
    except:
        print("%s音频播放失败" % audio_file)