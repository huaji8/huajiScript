#   --------------------------------注释区--------------------------------
#   入口:https://www.xingdouduanju.com/pages/register/index.html?invite_code=351449 走个头谢谢
#   变量:yuanshen_xddj 多号@
#   抓取Authorization的值填入
#   corn: 八小时一次 22 8-23/8 * * *
exchange = True #是否自动兑换猪 开启True 关闭False
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
import json
import time
import os
import random
import hashlib
def version():
     txt = requests.get("https://gitee.com/HuaJiB/yuanshen34/raw/master/pubilc.txt").text
     print(txt)




class yuanshen():
    def __init__(self,cookie):
        self.url = "https://api.xingdouduanju.com"
        self.key = "kjKjb8WRmfb77U6IMqsVtIuIFQCvab4JBqABNqSp"
        self.cookie = cookie
        self.header = {
    "Authorization": f"{self.cookie}",
    "X-Version-Code": "126",
    "X-Platform": "android",
    "X-System": "13",
    "X-Brand": "Redmi",
    "Content-Type": "application/json; charset=utf-8",
    "Host": "api.xingdouduanju.com",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
    "User-Agent": "okhttp/4.9.2"
}

    def _md5(self,s):
        md5 = hashlib.md5()
        md5.update(s.encode('utf-8'))
        return md5.hexdigest()

    def _nonce(self,length=16):
        nonce = os.urandom(length)
        return nonce.hex()

    def _time(self):
        return (int(time.time() * 1000))

    def gold_task(self,id,name):
        url = f"https://api.xingdouduanju.com/api/gold_tasks/{id}/complete"
        self.nonce = self._nonce()
        self.time = self._time()
        if id == 11 or id == 1:
            self.sign = self._md5(f"{id}&{self.time}&{self.nonce}&{self.key}&true")
        else:
            self.sign = self._md5(f"{self.time}&{id}&{self.nonce}&{self.key}&true")
        data = {
            "timestamp": f"{self.time}",
            "nonce": f"{self.nonce}",
            "id": f"{id}",
            "done":True,
            "sign": f"{self.sign}"
        }
        r = requests.post(url,headers=self.header,json=data).json()
        if r["code"] == 200001:
            if id == 11:
                print(f"✅做任务[{id}][{name}]成功,获得现金[{r['data']['reward']}]")
            else:
                print(f"✅做任务[{id}][{name}]成功,获得金币[{r['data']['reward']}]")
            if id == 1:
                time.sleep(random.randint(10,30))
            elif id == 5:
                time.sleep(random.randint(61,63))
            elif id == 6:
                time.sleep(random.randint(34,60))
            else:
                time.sleep(random.randint(10,20))
        else:
            print(f"❌️做任务[{id}][{name}]失败,错误信息:{r}")
            time.sleep(random.randint(5,15))

    def daily_task(self):
        url = f"{self.url}/api/gold_tasks"
        r = requests.get(url,headers=self.header).json()
        do_id_list = [1,5,6,11]
        if r["code"] == 200001:
            print("🎉️获取任务列表成功！")
            for dataa in r["data"]["tasks"]:
                rjson = json.loads(json.dumps(dataa))
                if rjson['id'] in do_id_list:
                    
                    do_time = rjson['times'] - rjson['completedCount']
                    print(f"✅开始执行任务[{rjson['name']}],共执行[{do_time}]次")
                    for i in range(do_time):
                        self.gold_task(rjson['id'],rjson['name'])

                else:
                    print(f"❌️跳过任务[{rjson['name']}]")
        else:
            print(f"❌️获取任务失败,错误信息:{r}")

    def get_gold(self):
        url = f"{self.url}/api/gold_pigs/info"
        r = requests.get(url,headers=self.header).json()
        if r["code"] == 200001:
            print("🎉️获取金块信息成功！")
            global pigcount
            pigcount = r["data"]["goldPigCount"]
            url = "https://api.xingdouduanju.com/api/gold_pigs/collect_all_bullion"
            self.time = self._time()
            self.nonce = self._nonce()
            self.sign = self._md5(f"{self.time}&{self.nonce}&{self.key}&true")

            data ={
    "timestamp": f"{self.time}",
    "nonce": f"{self.nonce}",
    "hasWatchAd": True,
    "sign": f"{self.sign}"
            }
            r = requests.post(url,headers=self.header,json=data).json()
            if r["code"] == 200001:
                print(f"✅一键领取金块成功")
                time.sleep(random.randint(3,8))
            else:
                print(f"❌️一键领取金块失败,错误信息:{r}")
                time.sleep(random.randint(3,8))


    def userinfo(self):
        if exchange:
            while True:
                url = f"{self.url}/api/gold_pigs/gold_exchange"
                self.nonce = self._nonce()
                self.time = self._time()
                self.sign = self._md5(f"{self.time}&{self.nonce}&{self.key}")
                data = json.dumps({
                "timestamp": f"{self.time}",
                "nonce": f"{self.nonce}",
                "sign": f"{self.sign}"
                    })
                r = requests.post(url,headers=self.header,data=data).json()
                if r["code"] == 200001:
                    print(f"✅兑换猪仔成功 [{r['message']}]")
                    time.sleep(random.randint(5,10))
                else:
                    print(f"❌️兑换猪仔失败,错误信息 [{r['message']}]")
                    break
        else:
            print("❌️跳过兑换猪仔")

        url = f"{self.url}/api/user/profile"
        r = requests.get(url,headers=self.header).json()
        if r["code"] == 200001:
            print("=========================================")
            print("查询用户信息成功")
            print(f"🎉️当前金币 [{r['data']['walletGold']['balance']}]")
            print(f"🎉️当前金块 [{r['data']['walletBullion']['balance']}]")
            print(f"🎉️当前猪仔 [{pigcount}]")
        else:
            print(f"❌️查询用户信息失败,错误信息:{r}")

    def get_gold_tuandui(self):
        url = f"{self.url}/api/user_bonus_bullions/info"
        r = requests.get(url,headers=self.header).json()
        if r["code"] == 200001:
            print(f"🎉️获取团队金块信息成功 可领取[{r['data']['bullionTotal']}]")
            if r['data']['bullionTotal'] == 0:
                print("🎉️没有可领取的团队金块")
                return
            url = f"{self.url}/api/user_bonus_bullions/collect"
            self.time = self._time()
            self.nonce = self._nonce()
            self.sign = self._md5(f"{self.time}&{self.nonce}&{self.key}")
            data = {
                "timestamp": f"{self.time}",
                "nonce": f"{self.nonce}",
                "sign": f"{self.sign}"
            }
            r = requests.post(url,headers=self.header,json=data).json()
            if r["code"] == 200001:
                print(f"✅领取团队金块成功 [{r['message']}]")
            else:
                print(f"❌️领取团队金块失败,错误信息:{r}")
        else:
            print(f"❌️获取团队金块信息失败,错误信息:{r}")

    def steal_gold(self):
        i = 1
        while True:
            url = f"{self.url}/api/user/friends?level={i}&curor=2&keyword="
            r = requests.get(url,headers=self.header).json()
            if r["code"] == 200001:
                print(f"🎉️获取好友信息成功")
                for dataa in r["data"]:
                    rjson = json.loads(json.dumps(dataa))
                    if rjson['canCollectBullion']:
                        url = f"{self.url}/api/user_friend_bullions/collect"
                        self.time = self._time()
                        self.nonce = self._nonce()
                        self.sign = self._md5(f"{self.time}&{rjson['id']}&{self.nonce}&{self.key}")
                        data = json.dumps({
                            "timestamp": f"{self.time}",
                            "nonce": f"{self.nonce}",
                            "friendId": f"{rjson['id']}",
                            "sign": f"{self.sign}"
                        })
                        r = requests.post(url,headers=self.header,data=data).json()
                        if r["code"] == 200001:
                            print(f"✅领取好友[{rjson['nickname']}]金块成 获得[{r['data']['amount']}]金块")
                        else:
                            print(f"❌️领取好友[{rjson['nickname']}]金块失败,错误信息:{r}")
                        time.sleep(random.randint(1,3))
                    else:
                        print(f"❌️好友[{rjson['nickname']}]没有可领取的金块")
                        time.sleep(1)
            else:
                print(f"❌️获取好友信息失败,错误信息:{r}")
                break
            i += 1
            if i == 3:
                break

    def task(self):
        print("🎉️开始执行[日常任务]")
        self.daily_task()
        print("===========================")
        print("🎉️开始执行[领取金块]")
        self.get_gold()
        print("===========================")
        self.get_gold_tuandui()
        print("===========================")
        self.steal_gold()
        print("===========================")
        print("🎉️开始执行[兑换猪仔&查询信息]")
        self.userinfo()

if __name__ == '__main__':
    version()
    cookie = ''
    if not cookie:
        cookie = os.getenv("yuanshen_xddj")
        if not cookie:
            print("请设置环境变量:yuanshen_xddj")
            exit()
    cookies = cookie.split("@")
    print(f"一共获取到{len(cookies)}个账号")
    i = 1
    for cookie in cookies:
     print(f"\n--------开始第{i}个账号--------")
     main = yuanshen(cookie)
     main.task()
     print(f"--------第{i}个账号执行完毕--------")
     i += 1
    
