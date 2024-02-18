### macos下不可用

import pyttsx3

# 初始化 TTS 引擎
engine = pyttsx3.init()
voices = engine.getProperty('voices')
# 设置要使用的声音
engine.setProperty('voice', voices[0].id)
# 可以根据需要选择声音

# 要转换为语音的文本
with open('./data/chat.txt', 'r', encoding='utf-8') as f:
    str_f = f.readlines()
    for s in str_f:
        s = s.replace('\n', '')
        label = s.split(",")[1]
        text = s.split(",")[0]
        output_file = f"../data/robot/{label}_robot_{text}.wav"

        # 生成语音并保存为音频文件
        engine.save_to_file(s, output_file)
        engine.runAndWait()
        print("语音文件已保存为", output_file)