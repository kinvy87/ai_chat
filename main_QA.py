from utils.chatGPT_module import gpt_qa


prompt = input("Q:")

while len(prompt) != 0:
    res = gpt_qa(prompt)
    print(prompt,"\n",res)




