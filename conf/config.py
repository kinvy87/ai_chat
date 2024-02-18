# 默认输入的服务器地址，测试时候使用，避免登录总是输入地址麻烦
default_server = "127.0.0.1:1"

# 定义服务器端口，一个端口一个房间
PORT = range(1, 3)

import sys
# DIR_PATH = sys.path[0] + "\\"
DIR_PATH = ""

# 图灵Tuling机器人还是ChatBot聊天机器人选择
BOTS = ["TuLing", "ChatBot", "User"]
BOT = BOTS[2]

# 浏览器请求头文件
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 '
                         '(KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36', }
headers2 = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko)Chrome/62.0.3202.94 Safari/537.36'}

# 图灵密匙，自动回复地址，选择的key不同，tuling机器人的回答也各不相同
tuling_app_key = "7d99d7037ce3481cb895079b265a6b64"
# tuling_app_key2 = "4bc32d41c10be18627438ae45eb839ac"
tuling_url = "http://www.tuling123.com/openapi/api"

# 语音保存播放开关
VOICE_SWITCH = True

# 百度密钥
BaiDu_App_ID = '17160989'
BaiDu_API_Key = 'G65EjCBPKcDP1tgILd00GN1c'
BaiDu_Secret_Key = 'Yx0GGtuz64Mj1wrQcWqdXLzWk8Is5OBe'
BaiDu_OpenApi_Url = "https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=%s&client_secret=%s"

# 百度语音识别
BaiDu_Asr_Url = 'http://vop.baidu.com/server_api'


# 百度文本转语音地址和配置 tts地址
# BaiDu_tts_url = "http://tts.baidu.com/text2audio"
# BaiDu_tts_set = {"idx": 1, "cuid": "baidu_speech_demo", "cod": 2,
#                  "lan": "zh", "ctp": 1, "pdt": 1, "spd": 4, "per": 4, "vol": 5, "pit": 5}

# 百度文字转语音 tsn地址
# baidu_api_url2 = "http://tsn.baidu.com/text2audio?tex=%s&lan=zh&cuid=%s&ctp=1&tok=%s"
# BaiDu_API_Key_GetVoi = "2NagVAULCYCnOnamrc8MNUPc"
# BaiDu_Secret_Key_GetVoi = "af4860b64e77d187643db05ccdb060e4"



####唤醒词
Picovoice_key="4qu6j4jJhhdkOYzOoabMHVWbl4mQY0FgueYgkoqy2RneoJVehHyXDQ=="
# Picovoice_keyword_paths=[r'data/picovoice/小宝_zh_raspberry-pi_v3_0_0.ppn']
# Picovoice_keyword_paths=[r'data/picovoice/小宝_zh_windows_v3_0_0.ppn']
# Picovoice_keyword_paths=[r'data/picovoice/shell-ball_en_windows_v2_1_0.ppn']
Picovoice_keyword_paths=[r'data/picovoice/shell-ball_en_raspberry-pi_v2_1_0.ppn']
# Picovoice_keyword_paths=[r'data/picovoice/hi-bell_en_raspberry-pi_v2_1_0.ppn']


answer_len = 120

################
conversation = [
    "你好",
    "你好",

    "你好可爱哦",
    "我是小奶猫",

    "你能陪我玩么",
    "喵喵",

    "你怎么了",
    "我饿了",

    "好吃吗",
    "好吃",

    "你还要吗",
    "我还要",

    "你在干嘛",
    "睡觉中",

    "你在干什么",
    "睡觉中",

    "你怎么了",
    "我要你陪我玩",

    "你到底想干嘛",
    "我要啪啪",

    "你给我撒个娇",
    "求抱抱",

    "不听话就带你去割蛋蛋",
    "我害怕",

    "哈哈哈割蛋蛋",
    "你滚开",

    "拜拜",
    "拜拜"
]


# conversation = {
#     "你好": "你好",
#
#     "你好可爱哦":"我是小奶猫",
#
#     "你能陪我玩么":"喵喵",
#
#     "你怎么了":"我饿了",
#
#     "好吃吗": "好吃",
#
#     "你还要吗": "我还要",
#
#     "你在干嘛": "睡觉中",
#
#     "你在干什么": "睡觉中",
#
#     "你怎么了": "我要你陪我玩",
#
#     "你到底想干嘛": "我要啪啪",
#
#     "你给我撒个娇":"求抱抱",
#
#     "不听话就带你去割蛋蛋": "我害怕",
#
#     "哈哈哈割蛋蛋": "你滚开",
#
#     "拜拜":"拜拜"
# }
