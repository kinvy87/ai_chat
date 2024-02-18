import openai
from utils.tts_modeule import answer2voice
from conf.config import answer_len
import openai


if 0:
    openai.api_key = OpenAI_key
    openai.organization = OpenAI_org

    def gpt_qa(content):
        # Get my answer
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": content}]
        )

        try:
            ans = response["choices"][0].message['content']
        except Exception as e:
            ans = "不知道"
        return ans
else:
    openai.api_type = "azure"
    openai.api_base = "https://bjzkjuk.openai.azure.com/"
    openai.api_version = "2023-08-01-preview"
    openai.api_key = "c2dd7174b09044f0b693f9b8a893af3d"

    def gpt_qa(content):
        response = openai.ChatCompletion.create(
            engine="gpt35_16k",
            # engine="gpt4_turbo",
            messages=[
                {"role": "system", "content": "你是一个对话助手.请用中文回复,尽量简短回答"},
                {"role": "user", "content": content},
            ]
        )

        res = response['choices'][0]['message']['content']
        return res[:answer_len]  #输出字符串长度限制


def answer_by_gpt(query):
    answer = gpt_qa(query)  # chatGPT问答

    if "我是一个" in answer:
        answer = "我叫小宝"
    print("answer:", answer)
    answer2voice(answer,sleep_time=len(answer)*0.225)