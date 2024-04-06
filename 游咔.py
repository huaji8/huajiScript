# app在这：http://yk0009.xyz/?invite=zkMTcxMzM1NQ
# 抓取token#uid 填入yuanshen_youka uid在请求体
# 没毛没利润没玩法


import os
import requests
import json

def headers(token):
   headers = {
  'Host': 'xin.hansilu.fun',
  'token': token,
  'content-type': 'application/x-www-form-urlencoded',
  'content-length': '11',
  'accept-encoding': 'gzip',
  'user-agent': 'okhttp/4.8.1'
   }
   return headers

def sign(header,uid):
   url = "https://xin.hansilu.fun/Api/Home/signIn"
   data = {
   "uid": uid
   }
   re = requests.post(url,headers=header,data=data)
   data = json.loads(re.text)
   print("签到结果：",data["state"]["msg"])
   
def video(header,uid):
   url = "https://xin.hansilu.fun/Api/Home/lookVideoAd"
   data = {
   "uid": uid
   }
   re = requests.post(url,headers=header,data=data)
   data = json.loads(re.text)
   print("看视频结果：",data["state"]["msg"])

def userinfo(header,uid):
   url = "https://xin.hansilu.fun/Api/User/getUserHome"
   data = {
   "uid": uid,
   "fuid": uid
   }
   re = requests.post(url,headers=header,data=data)
   data = json.loads(re.text)
   print("用户剩余积分：",data["data"]["user"]["integral"])
def main_task(cookies):
   token = cookies.split("#")[0]
   uid = cookies.split("#")[1]
   header = headers(token)
   sign(header,uid)
   video(header,uid)
   userinfo(header,uid)

if __name__ == "__main__":
 cookies = ''
 if not cookies:
    cookies = os.getenv('yuanshen_youka')
 if not cookies:  
    print('没有token')
 cookies = cookies.split("@")
 print(f"一共获取到{len(cookies)}个账号")
 i = 1
 for cookie in cookies:
    print(f"\n--------开始第{i}个账号--------")
    try:
     main_task(cookie)
    except Exception as e:
     print("发生错误：",e)
    print(f"--------第{i}个账号执行完毕--------")
    i += 1
