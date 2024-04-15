#   --------------------------------注释&变量区--------------------------------
#   因被狗仔举报 本人下线已被全封 铭记 星星星星星er
#   入口 http://795a34041513117b20.kppjoru.cn/mauth/aaba9bd241473370a28bc1c78f0aee3e
#   以上入口请在微信打开，ok？
#   变量:yuanshen_mmyd 多号新建变量或&分割
#   抓取Cookie填入即可
#    corn: 看你心情
#    作者:Huaji 仅做交流 
ua = "" #抓包时的ua 切勿在群里问什么是ua 在哪里抓 不懂百度去
#   vernow = 2.2
#   =====推送配置=====
#  wxpusher的apptoken填入yuanshen_apptoken
#  wxpusher的主题ID 填入 yuanshen_topicid
#  不懂看 https://wxpusher.zjiecode.com/docs
#   ----------------------------------------------------------------------
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
import re
import json
import time
import os
import random
import urllib.parse
from urllib.parse import quote
from urllib.parse import urlparse
from functools import wraps
requests.packages.urllib3.disable_warnings()
print("=======当前版本：2.2=======")
def retry(exceptions, tries=5, delay=2, backoff=2):
    """
    简单的重试module 重试之后还不行直接抛出错误嘿嘿
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            _tries, _delay = tries, delay
            while _tries > 1:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    print(f"发生错误:[{e}], Retrying in {_delay} ...")
                    time.sleep(_delay)
                    _tries -= 1
                    _delay *= backoff
            try:
                return func(*args, **kwargs)
            except:
                print("重试了还失败。重开得了")
                  # 最后一次尝试
        return wrapper
    return decorator

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
    "User-Agent": f"{ua}",
    "X-Requested-With": "XMLHttpRequest",
    "Origin": f"http://{self.time1}.zmxshop.top",
    "Referer": f"http://{self.time1}.zmxshop.top/haobaobao/home?v={self.time2}",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cookie": f"{self.cookie}"
}

        self.header_3={
  "User-Agent": f"{ua}",
  "Cookie": f"{self.cookie}"
        }
        self.get_url()
        self.header_2 = {
    "Host": f"{self.domain}",
    "Connection": "keep-alive",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "User-Agent": f"{ua}",
    "X-Requested-With": "XMLHttpRequest",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
}
        #self.check()
    
        print("===========================")
    
    @retry(exceptions=Exception, tries=5, delay=2, backoff=2)
    def get_url(self):
        url = f"{self.url}/mwtmpdomain"
        r = requests.post(url,headers=self.header_3).json()
        if r['msg'] == 'success':
            urldata = urlparse(r['data']['domain'])
            urldata_2 = urllib.parse.urlparse(r['data']['domain'])
            query_params = urllib.parse.parse_qs(urldata_2.query)

            self.domain = f"{urldata.netloc}"
            self.uk = query_params.get('uk', [None])[0]

            print(f"✅获取阅读域名成功:[{self.domain}][{self.uk}]")
        else:
            print(f"❌获取阅读域名失败:[{r}]")

    @retry(exceptions=Exception, tries=5, delay=2, backoff=2)
    def get_sm(self):
        url = "http://101.132.127.171/api/huaji/txt/sm.txt"
        r = requests.get(url)
        if r.status_code == 200:
            print(f"✅获取检测文章列表成功")
            self.sm = r.text.split(",")
        else:
            print("联网获取检测文章列表失败！")

    @retry(exceptions=Exception, tries=5, delay=2, backoff=2)
    def task(self):
        v = "8.0"
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
                spt = (random.randint(18, 22))
                time.sleep(spt)
            else:
                spt = (random.randint(7, 13))
                time.sleep(spt)
    
            psign = random.randint(1, 1000)
            url = f"http://{self.domain}/jiajinbimao?time={spt}&psign={psign}&uk={self.uk}"
            r = requests.get(url,headers=self.header_2).json()
            if r['msg'] == 'success':
                print(f"🎉️阅读成功,已阅读:{r['data']['day_read']}篇,获得:{r['data']['gold']}金币")
            else:
                print(f"❌阅读失败:[{r['data']}]")
                return True
        else:
            print(f"❌获取文章失败:[{r}]")
            return True
        
    def tuisong(self):
        # 发送消息到wxpusher
        url = f"https://wxpusher.zjiecode.com/api/send/message/?appToken={appToken}&topicId={topicIds}&content=检测文章%0A请在20秒内完成验证!%0A%3Cbody+onload%3D%22window.location.href%3D%27{quote(self.read_link)}%27%22%3E"
        r = requests.get(url).json()
        print("🎉️检测文章推送结果",r)

    @retry(exceptions=Exception, tries=5, delay=2, backoff=2)
    def withdraw(self):
        url = f'{self.url}/haobaobao/workinfo'
        r = requests.get(url,headers=self.header_3).json()
        if r['msg'] == 'success':
            print(f"🎉️用户总金币:[{r['data']['remain_gold']}],今日已阅读:[{r['data']['dayreads']}]")
            if int(r['data']['remain_gold']) >= 10000:
                url = f'{self.url}/haobaobao/getgold'
                if self.get_rqid():
                    print(f"获取request_id失败,无法提现")
                    return
                gold = int(r['data']['remain_gold']) // 1000 * 1000
                data = {"request_id": self.rqid, "gold": gold}
                r = requests.post(url,headers=self.header_3,data=data).json()
                if r['msg'] == 'success':
                    print(f"✅金币转余额,获得:[{r['data']['money']}]元")
                    url = f"{self.url}/haobaobao/getwithdraw"
                    #data = f"signid={self.rqid}&ua=2&ptype=0&paccount=&pname="
                    data = {"signid":self.rqid,
                            "ua":2,
                            "ptype":0,
                            "paccount":'',
                            "pname":''}
                    r = requests.post(url,headers=self.header_3,data=data).json()
                    if r['msg'] == 'success':
                        print(f"✅提现成功")
                    else:
                        print(f"❌提现失败:[{r}]")
                else:
                    print(f"❌金币转余额失败:[{r}]")
            else:
                print(f"❌金币不足,无法提现")
        else:
            print(f"❌查询用户信息失败:[{r}]")

    def get_rqid(self):
            header = {
    "Host": f"{self.time1}.zmxshop.top",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": f"{ua}",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/wxpic,image/tpg,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "X-Requested-With": "com.tencent.mm",
    "Referer": f"http://{self.time1}.zmxshop.top/haobaobao/home?v={self.time2}",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cookie": f"{self.cookie}"
            }
            url = f"{self.url}/haobaobao/withdraw"
            r = requests.get(url,headers=header)
            match = re.search(r'request_id\s*=\s*"([^"]+)"', r.text)
            if match:
                self.rqid = match.group(1)
                print(f"✅获取request_id成功:[{self.rqid}]")
            else:
                return True


    def read(self):
        while True:
            if self.task():
                print("======阅读完毕======")
                break
        self.withdraw()


        
    

if __name__ == '__main__':
    if not ua:
        print("❌你还没有设置ua,请在脚本内填写ua")
        exit()

    print("=======因被狗仔举报 本人包括下线已被全封 铭记 星星星星星er=====")
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
     time.sleep(10)
     print(f"--------第{i}个账号执行完毕--------")
     i += 1
    

