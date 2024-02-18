import json
import requests
from utils.tts_modeule import answer2voice

#定义获取天气数据函数
def getWeather_data(city_code="101010100"):
  print('------天气查询------')
  url = 'http://t.weather.sojson.com/api/weather/city/%s' % city_code
  weather_data = requests.get(url=url)
  # 读取网页数据
  weather_data = weather_data.content
  # #解压网页数据
  weather_dict = json.loads(weather_data)
  return weather_dict

#定义当天天气输出格式
def parse_weather_data(weather_data,i=0,city_name="北京"):
    weather_forcast = weather_data["data"]["forecast"]
    if i == 0: #今天天气
        weather_info = weather_forcast[0]
    else: #明天天天气
        weather_info = weather_forcast[1]
    weather_forecast_txt = '您好，您所在的城市%s，%s日，%s，天气%s，最低温度%s，最高温度%s，风向%s，风力%s，%s' % \
                           (city_name,
                            weather_info['date'],
                            weather_info['week'],
                            weather_info['type'],
                            weather_info['low'],
                            weather_info['high'],
                            weather_info['fx'],
                            weather_info['fl'],
                            weather_info['notice'] )

    return weather_forecast_txt

#定义语音播报今天天气状况
def broadcast_broadcast(weather_forcast_txt):
  weather_forecast_txt = weather_forcast_txt
  print('语音提醒：', weather_forecast_txt)
  #百度语音合成
  answer2voice(weather_forecast_txt,r'voice_broadcast/weather_forecast.mp3',sleep_time=20)


def weather_run(i):
    weather_data = getWeather_data()
    weather_forecast_txt = parse_weather_data(weather_data, i)
    broadcast_broadcast(weather_forecast_txt)