import pvporcupine
import struct
import pyaudio
import pvcobra
import speech_recognition as sr
from utils.chatGPT_module import chat_qa

porcupine = None
pa = None
audio_stream = None
r = sr.Recognizer()


def picovoice():
    access_key = 'your key'
    porcupine = pvporcupine.create(
        access_key=access_key,
        keyword_paths=['your path']
    )
    pa = pyaudio.PyAudio()
    cobra = pvcobra.create(access_key)
    audio_stream = pa.open(
        rate=porcupine.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=porcupine.frame_length)
    while True:
        pcm = audio_stream.read(porcupine.frame_length, exception_on_overflow=False)
        #
        _pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)
        keyword_index = porcupine.process(_pcm)
        if keyword_index >= 0:
            res = chat_qa(query)
            print(query, "\n", res)