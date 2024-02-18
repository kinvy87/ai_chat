#!/usr/bin/python
# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from conf.config import conversation
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer


my_bot = ChatBot("Training demo",
                 database="./db.sqlite3")

#######################################
# 使用自定义语句训练它
# 直接写语句训练
# conversation = [
#     "小喵你好",
#     "你好!",
#     "小喵你怎么了？",
#     "我饿了",
#     "小喵你想干嘛？",
#     "我要你陪我玩！",
#     "小喵你到底想干嘛？",
#     "我要啪啪！",
#     "小喵你给我撒个娇",
#     "喵喵！"
#     "拜拜小喵",
#     "拜拜！"
# ]
trainer = ListTrainer(my_bot)
trainer.train(conversation)

#######################################
# 使用chatterbot_corpus 内嵌语料库
# trainer = ChatterBotCorpusTrainer(my_bot)
# trainer.train("chatterbot.corpus.chinese")
# trainer.train("chatterbot.corpus.chinese","chatterbot.corpus.english")


# while True:
#     print(my_bot.get_response(input("user:")))


#####################################################

