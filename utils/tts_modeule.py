import pygame
import time
from aip import AipSpeech
from conf.config import BaiDu_App_ID, BaiDu_API_Key, BaiDu_Secret_Key

client = AipSpeech(BaiDu_App_ID, BaiDu_API_Key, BaiDu_Secret_Key)

def voice_play(audio_file, sleep_time=0.8):
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(audio_file)
        pygame.mixer.music.play()
        time.sleep(sleep_time)
    except:
        print("%s音频播放失败" % audio_file)

def answer2voice(answer,file_name='tts_voice/answer.mp3', sleep_time=8):
    # 百度语音合成
    result = client.synthesis(answer, 'zh', 3, {'vol': 5, 'spd': 5, 'pit': 5, 'per': 1})
    if not isinstance(result, dict):
        with open(file_name, 'wb') as f:
            f.write(result)
            f.close()

    # playsound模块播放语音
    voice_play(file_name, sleep_time=sleep_time)