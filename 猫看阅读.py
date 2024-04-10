#   --------------------------------注释&变量区--------------------------------
#   入口 http://7de2d9041017129bdf.quljo.shop/mauth/ccf882295d8f9ab71845a90f1f4f4040
#   变量:yuanshen_mmyd 多号新建变量或&分割
#   抓取Cookie填入即可
#    corn: 看你心情
#    作者:Huaji 仅做交流
#   =====推送配置=====
#  wxpusher的apptoken填入yuanshen_apptoken
#  wxpusher的主题ID 填入 yuanshen_topicid
#  不懂看 https://wxpusher.zjiecode.com/docs
#  因被狗必举报 本脚本不做版本处理 自行Github更新
#  当前版本1.0.3
#   --------------------------------一般不动区--------------------------------
#                     _ooOoo_
#                    o8888888o
#                    88" . "88
#                    (| -_- |)
#                     O\ = /O
#                 ____/`---'\____
#               .   ' \\| |// `.
#                / \\||| : |||// \
#              / _||||| -:- |||||- \
#                | | \\\ - /// | |
#              | \_| ''\---/'' | |
#               \ .-\__ `-` ___/-. /
#            ___`. .' /--.--\ `. . __
#         ."" '< `.___\_<|>_/___.' >'"".
#        | | : `- \`.;`\ _ /`;.`/ - ` : | |
#          \ \ `-. \_ __\ /__ _/ .-` / /
#  ======`-.____`-.___\_____/___.-`____.-'======
#                     `=---='
# 
#  .............................................
#           佛祖保佑             永无BUG
#           佛祖镇楼             BUG辟邪
#佛曰:  
#        写字楼里写字间，写字间里程序员；  
#        程序人员写程序，又拿程序换酒钱。  
#        酒醒只在网上坐，酒醉还来网下眠；  
#        酒醉酒醒日复日，网上网下年复年。  
#        但愿老死电脑间，不愿鞠躬老板前；  
#        奔驰宝马贵者趣，公交自行程序员。  
#        别人笑我忒疯癫，我笑自己命太贱；  
#        不见满街漂亮妹，哪个归得程序员？
#
#   --------------------------------代码区--------------------------------

import requests
import requests
import json
import time
import os
from urllib.parse import urlparse
import urllib.parse
import random
from urllib.parse import quote
requests.packages.urllib3.disable_warnings()
def version():
     txt = requests.get("https://gitee.com/HuaJiB/yuanshen34/raw/master/pubilc.txt").text
     print(txt)


class yuanshen():
    def __init__(self,cookie):
        self.get_sm()
        self.cookie = cookie
        self.time1 = int(time.time())
        self.time2 = int(time.time()) + random.randint(10, 50)
        self.url = f"http://{self.time1}.zmxshop.top"
        self.header = {
    "Host": f"{self.time1}.zmxshop.top/haobaobao/user",
    "Connection": "keep-alive",
    "Content-Length": "0",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "User-Agent": "Mozilla/5.0 (Linux; Android 13; 23054RA19C Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 XWEB/1160117 MMWEBSDK/20240301 MMWEBID/98 MicroMessenger/8.0.48.2580(0x28003036) WeChat/arm64 Weixin NetType/5G Language/zh_CN ABI/arm64",
    "X-Requested-With": "XMLHttpRequest",
    "Origin": f"http://{self.time1}.zmxshop.top",
    "Referer": f"http://{self.time1}.zmxshop.top/haobaobao/home?v={self.time2}",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cookie": f"{self.cookie}"
}


        self.header_3={
  "User-Agent": "Mozilla/5.0 (Linux; Android 13; 23054RA19C Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 MMWEBID/98 MicroMessenger/8.0.48.2580(0x28003036) WeChat/arm64 Weixin NetType/5G Language/zh_CN ABI/arm64",
  "Cookie": f"{self.cookie}"
        }

        self.header_2 = {
    "Host": f"{self.time1}.zmxshop.top",
    "Connection": "keep-alive",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "User-Agent": "Mozilla/5.0 (Linux; Android 13; 23054RA19C Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 MMWEBID/98 MicroMessenger/8.0.48.2580(0x28003036) WeChat/arm64 Weixin NetType/5G Language/zh_CN ABI/arm64",
    "X-Requested-With": "XMLHttpRequest",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
}
        #self.check()
        self.get_url()
        print("===========================")
    def get_url(self):
        url = f"{self.url}/mwtmpdomain"
        r = requests.post(url,headers=self.header_3).json()
        if r['msg'] == 'success':
            urldata = urlparse(r['data']['domain'])
            urldata_2 = urllib.parse.urlparse(r['data']['domain'])
            query_params = urllib.parse.parse_qs(urldata_2.query)

            self.domain = f"{urldata.netloc}"
            self.uk = query_params.get('uk', [None])[0]

            print(f"✅获取域名成功:[{self.domain}][{self.uk}]")
        else:
            print(f"❌获取域名失败:[{r['data']['msg']}]")

    
    def get_sm(self):
        url = "http://101.132.127.171/api/huaji/txt/sm.txt"
        r = requests.get(url)
        if r.status_code == 200:
            print(f"✅获取检测文章列表成功")
            self.sm = r.text.split(",")
        else:
            print("联网获取检测文章列表失败！")

    
    def task(self):
        v = "7.0"
        mysign = "168"
        url = f"http://{self.domain}/wenzjks?time={int(time.time())* 1000}&mysign={mysign}&v={v}&uk={self.uk}"
        r = requests.get(url,headers=self.header_2).json()
        if r['msg'] == 'success':
            self.read_link = (r['data']['link']).replace("\\", "")

            parsed_url = urllib.parse.urlparse(self.read_link)
            query_params = urllib.parse.parse_qs(parsed_url.query)
            __biz = query_params.get('__biz', [None])[0]
            print(f"✅获取文章成功:[{self.read_link}]")

            if __biz in self.sm:
                print(f"❌该文章为检测文章:[{self.read_link}]")
                self.tuisong()
                spt = 20
                time.sleep(spt)
            else:
                spt = (random.randint(8, 12))
                time.sleep(spt)
    
            psign = random.randint(1, 1000)
            url = f"http://{self.domain}/jiajinbimao?time={spt}&psign={psign}&uk={self.uk}"
            r = requests.get(url,headers=self.header_2).json()
            if r['msg'] == 'success':
                print(f"🎉️阅读成功,已阅读:{r['data']['day_read']}篇,获得:{r['data']['gold']}金币")
            else:
                print(f"❌阅读失败:[{r['data']['msg']}]")
                return True
        else:
            print(f"❌获取文章失败:[{r}]")
            return True
        
    def tuisong(self):
        # 发送消息到wxpusher
        url = f"https://wxpusher.zjiecode.com/api/send/message/?appToken={appToken}&topicId={topicIds}&content=检测文章%0A请在20秒内完成验证!%0A%3Cbody+onload%3D%22window.location.href%3D%27{quote(self.read_link)}%27%22%3E"
        r = requests.get(url).json()
        print("🎉️检测文章推送结果",r)

    def read(self):
        while True:
            if self.task():
                break


        
    

if __name__ == '__main__':
    appToken = ""
    topicIds = ""
    version()
    if not appToken:
        appToken = os.getenv("yuanshen_apptoken")
        if not appToken:
            print("❌你还没有设置推送,请设置环境变量:yuanshen_apptoken")
            exit()
    if not topicIds:
        topicIds = os.getenv("yuanshen_topicid")
        if not topicIds:
            print("❌你还没有设置推送,请设置环境变量:yuanshen_topicid")
            exit()

    cookie = ''
    if not cookie:
        cookie = os.getenv("yuanshen_mmyd")
        if not cookie:
            print("❌你还没有设置阅读ck,请设置环境变量:yuanshen_mmyd")
            exit()
    cookies = cookie.split("&")
    print(f"一共获取到{len(cookies)}个账号")
    i = 1
    for cookie in cookies:
     print(f"\n--------开始第{i}个账号--------")
     main = yuanshen(cookie)
     main.read()
     print(f"--------第{i}个账号执行完毕--------")
     i += 1
    

