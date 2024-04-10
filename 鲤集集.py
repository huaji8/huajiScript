#   --------------------------------注释区--------------------------------
#   原作者:不知道谁 一天1+
#   入口:http://api.app.sp800.vip/h5/#/?id=14384
#   变量:yuanshen_ljj 多号@
#   抓取token的值填入
#   corn: 1小时一次 22 8-23/1 * * *
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
import requests,os,random
import json
import time

def version():
     txt = requests.get("https://gitee.com/HuaJiB/yuanshen34/raw/master/pubilc.txt").text
     print(txt)

class yuanshen:
    def __init__(self,cookie):

        self.url = "https://api.app.sp800.vip"
        self.cookie = cookie
        self.headers = {
    'token': f'{self.cookie}',
    'Host': 'api.app.sp800.vip',
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip',
    'User-Agent': 'okhttp/3.12.0',
}
        
    def box(self):
        r = requests.get(f'{self.url}/api/User/openBox', headers=self.headers).json()
        if r['code'] == 1:
            print(f"🎉️{r['msg']}获得金币:{r['data']['integral']},看视频金币:{r['data']['surf_ads_integral']}")
        else:
            print(r['msg'])
            return True

        r = requests.get(f'{self.url}/api/User/getSurfAds', headers=self.headers).json()
        if "ok" in r["msg"]:
            signid=r["data"]["signId"]
            data = {'signId': signid}
            time.sleep(random.randint(40,50))
            r = requests.post(f'{self.url}/api/User/setSurfAds', headers=self.headers, data=data).json()
            print(r["msg"])
            time.sleep(random.randint(80,200))

    def video(self):
        r = requests.get(f'{self.url}/api/User/surfAds', headers=self.headers).json()
        if r['code'] == 1:
            print("🎉️新手任务---看视频成功！")
            time.sleep(random.randint(40,50))
            return False
        else:
            print(f"❌️新手任务看视频----{r['msg']}")
            return True
    def sign(self):
        r = requests.get(f'{self.url}/api/User/sign_v2', headers=self.headers).json()
        if r['code'] == 1:
            print(f"🎉️签到成功！获得金币{r['data']['integral']}")
        else:
            print(f"❌️签到失败！{r['msg']}")

    def userinfo(self):
        r = requests.get(f'{self.url}/api/User/myuserinfo', headers=self.headers).json()
        print(f"🎉️当前账号剩余金币：{r['data']['score']}\n🎉️剩余余额:{r['data']['money']}\n")
        if r['data']['surf_ads_task_count'] >= 10:
            print("🎉️当前账号已完成新手任务")
        else:
            for i in (range(10)):
                if self.video():
                    break
            
        
    def main(self):
        self.sign()
        while True:
            if self.box():
                break
        self.userinfo()


if __name__ == '__main__':
    version()
    cookie = ''
    if not cookie:
        cookie = os.getenv("yuanshen_ljj")
        if not cookie:
            print("请设置环境变量:yuanshen_ljj")
            exit()
    cookies = cookie.split("@")
    print(f"一共获取到{len(cookies)}个账号")
    i = 1
    for cookie in cookies:
     print(f"\n--------开始第{i}个账号--------")
     main = yuanshen(cookie)
     main.main()
     print(f"--------第{i}个账号执行完毕--------")
     i += 1
    

