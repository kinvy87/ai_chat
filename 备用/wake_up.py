import struct
import pyaudio
import pvporcupine

#porcupine = pvporcupine.create(keywords=['porcupine', 'ok google', "picovoice", "blueberry"])
porcupine = pvporcupine.create(access_key="y2dlDmQSvdu2BlOnq6L5nLsyDwZ+pjUiyhTch2fk5yu+NlVO22t4pA==",
                               keyword_paths=[r'data/picovoice/shell-ball_en_windows_v2_1_0.ppn'])

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
        print("唤醒成功")
