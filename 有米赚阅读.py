#   --------------------------------注释区--------------------------------
#   入口:http://aciko1e3ow2hhn1do9n8efdadm.a6l6z56l.zhijianzzmm.cn/ttz/wechat/ttzScanCode?userShowId=3299走个头谢谢
#   变量:yuanshen_lgyd 多号方式: @分割 或 换行分割 或 新建同名变量
#   填入 你的用户id     自行点击提现设置密码
#   格式:用户id#备注#密码 备注可不填，不填格式为用户id##密码
#   无需增加任何依赖    调用第三方接口实现二维码识别
#   --------------------------------一般不动区-------------------------------
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
import json
import time
import os
import random
from urllib.parse import urlparse, parse_qs
import base64
from functools import wraps

requests.packages.urllib3.disable_warnings()

def version():
     txt = requests.get("https://gitee.com/HuaJiB/yuanshen34/raw/master/pubilc.txt").text
     print(txt)
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
                    print(f"发生错误:[{e}], Retrying in after{_delay} ...")
                    time.sleep(_delay)
                    _tries -= 1
                    _delay *= backoff
            try:
                return func(*args, **kwargs)
            except:
                print("重试了还失败。重开得了")
        return wrapper
    return decorator
class yuanshen():
    def __init__(self,bz,cookie,pwd):
        self.pwd = pwd
        self.number=0
        self.bz = bz
        self.url = "http://xingeds.3fexgd.zhijianzzmm.cn"
        self.cookie = cookie
        self.header={
    "Host": "xingeds.3fexgd.zhijianzzmm.cn",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Linux; Android 13; 23054RA19C Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 XWEB/1160117 MMWEBSDK/20240301 MMWEBID/98 MicroMessenger/8.0.48.2580(0x28003036) WeChat/arm64 Weixin NetType/5G Language/zh_CN ABI/arm64",
    "content-type": "application/x-www-form-urlencoded",
    "Accept": "*/*",
    "Origin": "http://gew.gewxg.234tr.zhijianzzmm.cn",
    "X-Requested-With": "com.tencent.mm",
    "Referer": "http://gew.gewxg.234tr.zhijianzzmm.cn/",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
}
        self.getdomain()

    def gettoken(self):
        data = { "data" :f"{self.picturedata}"}
        pst = json.dumps(data)
        req = requests.post(url="http://api.wer.plus/api/ymqr",data=pst).json()##调用三方接口
        if req["code"] == 200:
            self.readurl = req["data"]["text"]
        else:
            print(f"❌️[{self.bz}]获取token失败 [{req['message']}]")
            exit()

        data = parse_qs(urlparse(self.readurl).query)
        self.token1 = data.get('token', [None])[0]
        decoded_token = base64.b64decode(self.token1).decode('utf-8')
        new_token = f"{decoded_token}&startNumber={self.number}"
        self.token = base64.b64encode(new_token.encode('utf-8')).decode('utf-8')
        print(f"🎉️[{self.bz}]识别阅读二维码成功:[{self.token}]")
    
    def reftoken(self):#刷新token
        decoded_token = base64.b64decode(self.token1).decode('utf-8')
        new_token = f"{decoded_token}&startNumber={self.number}"
        self.token = base64.b64encode(new_token.encode('utf-8')).decode('utf-8')
            
    @retry(exceptions=Exception, tries=5, delay=2, backoff=2)
    def getdomain(self):
        url = f"{self.url}/ttz/api/queryActivityContentx?userShowId={self.cookie}&type=1"
        r = json.loads(requests.get(url,headers=self.header,timeout=15).text)
        if r["code"] == 200:
            self.picturedata = (r["data"]["twoMicrocodeUrl"])
            self.gettoken()

        else:
            print(f"❌️[{self.bz}]获取阅读域名失败 [{r}]")
            exit()
    @retry(exceptions=Exception, tries=5, delay=2, backoff=2)
    def getread(self):

        self.reftoken()
        url = f"http://xgcgmlige123.zhijianzzmm.cn/ttz/uaction/getArticleListxAuto?token={self.token}"
        r = requests.get(url,headers=self.header,timeout=15).json()
        if r["code"] == 200:
            print(f"🎉️[{self.bz}]阅读成功,当前已阅读:[{r['data']['startNum']}]")
            self.number=r["data"]["startNum"]
        else:
            print(f"❌️[{self.bz}]阅读失败 [{r['message']}]")
            return True
    @retry(exceptions=Exception, tries=5, delay=2, backoff=2)
    def userinfo(self):
        url = f"{self.url}/ttz/api/queryUserSumScoreById?userShowId={self.cookie}"
        r = json.loads(requests.get(url,headers=self.header,timeout=15).text)
        if r["code"] == 200:
            print(f"🎉️[{self.bz}]获取用户信息成功,当前余额:[{r['data']['cashMoney']}]")
            if  r["data"]["cashScore"] >= 5000:
                print(f"[{self.bz}]开始提现")
                url = f"{self.url}ttz/api/queryMoneyInfo?userShowId={self.cookie}"
                r=requests.get(url,headers=self.header,timeout=15).json()
                if r["code"] == 200:
                    self.id = r["data"][1]["cashMoney"]
                    url = f"{self.url}/ttz/pay/pocketMoney?userShowId={self.cookie}&money=5&wdPassword={self.pwd}&moneyId={self.id}"
                    r = json.loads(requests.get(url,headers=self.header,timeout=15).text)
                    if r["code"] == 200:
                        print(f"🎉️[{self.bz}]提现成功")
                    else:
                        print(f"❌️[{self.bz}]提现失败 [{r['message']}]")
                else:
                    print(f"❌️[{self.bz}]获取提现信息失败 [{r['message']}]")
            else:
                print(f"[{self.bz}]当前余额不足5,无法提现")
                
        else:
            print(f"❌️[{self.bz}]获取用户信息失败 [{r['message']}]")

    def read(self):
        self.userinfo()
        while True:
            if self.getread():
                break
            time.sleep(random.randint(8,16))
        self.userinfo()

   


if __name__ == '__main__':
    version()
    cookie = ''
    if not cookie:
        cookie = os.getenv("yuanshen_lgyd")
        if not cookie:
            print("请设置环境变量:yuanshen_lgyd")
            exit()
    cookies = cookie.split("@")#草拟吗
    if '@' in cookie:
        cookies = cookie.split("@")
    elif '\n' in cookie:
        cookies = cookie.split("\n")
    elif '&' in cookie:
        cookies = cookie.split("&")

    print(f"一共获取到{len(cookies)}个账号")
    i = 1
    for cookie in cookies:
            ck = cookie.split("#")[0]
            try:
               bz = cookie.split("#")[1]
            except:
               bz = f"账号{i}"
            pwd = cookie.split("#")[2]
            print(f"\n--------开始第{i}个账号--------")
            main = yuanshen(bz,ck,pwd)
            main.read()
            print(f"--------第{i}个账号执行完毕--------")
            i += 1
            time.sleep(random.randint(30,50))
