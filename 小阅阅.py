#   --------------------------------注释&变量区--------------------------------
#   入口，微信打开：http://94b34e05121451.fxi3z.shop/mesauth/3885dd2e3833f9597b53927edcae23a5?u=2
#   在yuanshen_apptoken，yuanshen_topicid填入你的wxpusher的apptoken和topicid
#   在任意接口抓取请求头中的ysmuid和请求体中的unionid 填入yuanshen_xyy 多号@分割
#   格式 ysmuid=****@ysmuid=****   ysmuid=这个不要漏
#   接口变化会自动停止 默认多线程三线程执行
#   无自动提现 懒得写 就酱

MAX_gold = 10000 #最大阅读金币值
max_threads = 3 #执行线程数，改成1就是单线程了

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
import threading
import requests
import time
import os
import re
import random
from urllib.parse import urlparse, parse_qs,quote
import hashlib
from concurrent.futures import ThreadPoolExecutor
lock = threading.Lock()
def printf(m):
    with lock:
        print(m)
class yuanshen():
    def __init__(self,cookie):
        match = re.search(r'ysmuid=(.+)', cookie)
        self.ysmuid = match.group(1) if match else ''
        self.unionid = None

        self.vs = "110"
        self.list = "MzkxNTE3MzQ4MQ==,Mzg5MjM0MDEwNw==,MzUzODY4NzE2OQ==,MzkyMjE3MzYxMg==,MzkxNjMwNDIzOA==,Mzg4NTcwODE1NA==,MzIzMDczODg4Mw==,Mzg5ODUyMzYzMQ==,MzU0NzI5Mjc4OQ==,MzIzMDczODg4Mw==,MzkxNDU1NDEzNw==,MzkwMTYwNzcwMw==,MzkzNTYxOTgyMA==,MzkyNjY0MTExOA==,MzkxNDYzOTEyMw==,MzkyMjYxNzQ2NA==,MzkzNDYxODY5OA==,MzkzMTYyMDU0OQ==,MzkwNzYwNDYyMQ=="
        self.list_ = self.list.split(',')
        self.url = f"{int(time.time())}.dyrggt.cn"
        self.h = {
    "Host": f"{self.url}",
    "Connection": "keep-alive",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Linux; Android 13; 23054RA19C Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 MMWEBID/98 MicroMessenger/8.0.49.2600(0x28003133) WeChat/arm64 Weixin NetType/5G Language/zh_CN ABI/arm64",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": f"http://{self.url}",
    "Referer": f"http://{self.url}/",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cookie": f"ysmuid={self.ysmuid}; ejectCode=1"
}       
        


    def getunionid(self):
        def domain_url(url):
            parsed_url = urlparse(url)
            domain = parsed_url.netloc
            return domain
        url = "http://057c0b04032256d679.byexj.shop/yunonline/v1/auth/1ddf953f568a15fc1d498ae264bb6925?codeurl=byexj.shop&codeuserid=2&time=1712156161"
        headers = {
            "Host": "057c0b04032256d679.byexj.shop",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Linux; Android 13; 23054RA19C Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 MMWEBID/98 MicroMessenger/8.0.49.2600(0x28003133) WeChat/arm64 Weixin NetType/5G Language/zh_CN ABI/arm64",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/wxpic,image/tpg,image/webp,"
                    "image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "x-requested-with": "com.tencent.mm",
            "sec-fetch-site": "cross-site",
            "sec-fetch-mode": "navigate",
            "sec-fetch-user": "?1",
            "sec-fetch-dest": "document",
            "referer": "https://weixin110.qq.com/",
            "accept-encoding": "gzip, deflate",
            "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
        }
        response = requests.get(url, headers=headers, allow_redirects=False, verify=False).headers.get("location")
        headers = {
            "Host": domain_url(response),
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Linux; Android 13; 23054RA19C Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 MMWEBID/98 MicroMessenger/8.0.49.2600(0x28003133) WeChat/arm64 Weixin NetType/5G Language/zh_CN ABI/arm64",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/wxpic,image/tpg,image/webp,"
                    "image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "X-Requested-With": "com.tencent.mm",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            "Cookie": f"ysmuid={self.ysmuid}"
        }
        response = requests.get(response, headers=headers, allow_redirects=False).headers.get("location")
        response = requests.get(response, headers=headers).text
        unid = re.compile('websocket.send\("(.*?)"\);')
        self.unionid = unid.findall(response)[0]
        print("获取到unionid:",self.unionid)
        


    def tuisong(self):
        # 发送消息到wxpusher
        url = f"https://wxpusher.zjiecode.com/api/send/message/?appToken={appToken}&topicId={topicIds}&content=检测文章%0A请在20秒内完成验证!%0A%3Cbody+onload%3D%22window.location.href%3D%27{quote(self.readurl)}%27%22%3E"
        r = requests.get(url).json()
        printf(f"🎉️检测文章推送结果{r}")
    
    def fuck(self):
        headers = {
    "Host": f"{self.domain}",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Linux; Android 13; 23054RA19C Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.120 Mobile Safari/537.36 XWEB/1220053 MMWEBSDK/20240404 MMWEBID/98 MicroMessenger/8.0.49.2600(0x28003133) WeChat/arm64 Weixin NetType/5G Language/zh_CN ABI/arm64",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/wxpic,image/tpg,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "X-Requested-With": "com.tencent.mm",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
}
        url = f"http://{self.domain}/kdf.html?uk={self.uk}&t={self.t}"
        r = requests.get(url,headers=headers).text
        md5 = hashlib.md5()
        md5.update(r.encode('utf-8'))
        j = md5.hexdigest()
        printf(f"当前页面校准值:{j}")
        if j != "aedb13d0ef22ac41a8c2f5c34cf2d093":
            printf("当前页面校准值发生变化，疑似更改接口代码，马上跑路")
            exit()

    def getdomain(self):
        url = f"http://{self.url}/wtmpdomain2"
        data = {"unionid": f"{self.unionid}"}
        r = requests.post(url,headers=self.h,data=data).json()
        if r['errcode'] == 0:
            j = urlparse(r['data']['domain'].replace('\\','')); 
            self.domain, p = j.netloc, parse_qs(j.query); self.uk, self.t = p.get('uk')[0] if p.get('uk') else '', p.get('t')[0] if p.get('t') else ''
            printf(f"获取阅读域名成功[{self.domain}][{self.uk}][{self.t}]")
            self.h2 = {
    "Host": f"{self.domain}",
    "Connection": "keep-alive",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "User-Agent": "Mozilla/5.0 (Linux; Android 13; 23054RA19C Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 MMWEBID/98 MicroMessenger/8.0.49.2600(0x28003133) WeChat/arm64 Weixin NetType/5G Language/zh_CN ABI/arm64",
    "X-Requested-With": "XMLHttpRequest",
    "Referer": f"http://{self.domain}/kdf.html?uk={self.uk}&t={self.t}",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
}
            if self.fuck():exit()   
        else:
            printf(f"获取阅读域名失败---[{r['msg']}]")
            return True
    
    def read(self):
            url = f"http://{self.domain}/dresger4x?uk={self.uk}&time={int(time.time() * 1000)}&psgn=168&vs={self.vs}"
            r = requests.get(url,headers=self.h2).json()
            if r['errcode'] == 0:
                self.readurl = r['data']['link']
                printf(f"获取阅读文章成功[{self.readurl}]")
                j = urlparse(self.readurl.replace('\\',''))
                biz = parse_qs(j.query).get('__biz', [''])[0] if '__biz' in parse_qs(j.query) else ''
                if biz in self.list_:
                    printf("遇到检测文章，推送ing...")
                    self.tuisong()
                    k = random.randint(20,25)
                    time.sleep(k)
                else:
                    k = random.randint(8,16)
                    time.sleep(k)
                url = f"http://{self.domain}/jinbicp?uk={self.uk}&time={k}&timestamp={int(time.time() * 1000)}"
                r = requests.get(url,headers=self.h2).json()
                if r['errcode'] == 0:
                    printf(f"阅读成功,获得[{r['data']['gold']}]金币,今日共获得金币[{r['data']['day_gold']}]")
                    if r['data']['day_gold'] >= MAX_gold:
                        return True
                else:
                    printf(f"阅读失败---[{r['msg']}]")
                    return True
            else:
                printf(f"获取阅读文章失败---[{r['msg']}]")
                return True
            

    def userinfo(self):
        url = f"http://{self.url}/yunonline/v1/gold?unionid={self.unionid}&time={int(time.time() * 1000)}"
        r = requests.get(url,headers=self.h).json()
        if r['errcode'] == 0:
            printf(f"用户金币[{r['data']['last_gold']}],今日已阅读[{r['data']['day_read']}]")
            #提现部分 待补充
        else:
            printf(f"用户信息获取失败---[{r['msg']}]")


    
    def main(self):
        self.getunionid()
        if self.getdomain():exit()
        while True:
                if self.read():break
                time.sleep(3)
        self.userinfo()

if __name__ == '__main__':
    appToken = ""
    topicIds = ""

    if not appToken:
        appToken = os.getenv("yuanshen_apptoken")
        if not appToken:
            printf("❌你还没有设置推送,请设置环境变量:yuanshen_apptoken")
            exit()
    if not topicIds:
        topicIds = os.getenv("yuanshen_topicid")
        if not topicIds:
            printf("❌你还没有设置推送,请设置环境变量:yuanshen_topicid")
            exit()

    cookie = ''
    if not cookie:
        cookie = os.getenv("yuanshen_xyy")
        if not cookie:
            printf("❌你还没有设置阅读ck,请设置环境变量:yuanshen_xyy")
            exit()
    cookies = cookie.split("@")
    print(f"一共获取到{len(cookies)}个账号")
    tasks = []
    for ck in cookies:
        task = yuanshen(ck)
        tasks.append(task)

    

    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        time.sleep(3)
        results = executor.map(lambda task: task.main(), tasks)

    print("所有任务执行完毕")
