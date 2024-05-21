#   --------------------------------注释区--------------------------------
#   入口http://mcwreg.bfyxh.cn/h5#/pages/regindex/index?uid=508
#   抓任意接口 token参数的值
#   变量:yuanshen_mcw 多号： @分割
#   一个金币 1 块钱 0 手续费
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
import time
import random
import os
class yuanshen():
    def __init__(self,cookie):
        self.cookie = cookie
        self.h = {
    "Host": "mcw.bfyxh.cn",
    "Connection": "keep-alive",
    "Content-Length": "8",
    "User-Agent": "Mozilla/5.0 (Linux; Android 13; 23054RA19C Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36",
    "token": f"{self.cookie}",
    "content-type": "application/json",
    "Accept": "*/*",
    "Origin": "http://mcw.bfyxh.cn",
    "X-Requested-With": "wemaitcp.maichongwang",
    "Referer": "http://mcw.bfyxh.cn/h5/",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
}
        
    def task(self):
        id_list = []
        url = "http://mcw.bfyxh.cn/api/gold_config/index"
        r = requests.post(url,headers=self.h,json={}).json()
        for i in r['data']:
            id_ = i.get("id")
            if i.get("button_status") == 2:
                id_list.append(id_)
            else:
                break
        id = 0
        url = "http://mcw.bfyxh.cn/api/gold_config/applytask"
        while True:
            id += 1
            if id in id_list:
                print(f"第[{id}]奖励已领取")
                continue
            data = {"id":id}
            r = requests.post(url,headers=self.h,json=data).json()
            if r['code'] == 0:
                print(f"第[{id}]奖励领取成功")
            else:
                print(f"第[{id}]奖励领取失败---[{r['msg']}]")
                break
            time.sleep(random.randint(3,10))
    
    def get_t(self):
        id_list = [1,5,9]
        for i in id_list:
            url = "http://mcw.bfyxh.cn/api/task/lqtask"
            data = {"id":i}
            print(data)
            r = requests.post(url,headers=self.h,json=data).json()
            if r['code'] == 0:
                print(f"第[{i}]分润领取成功")
            else:
                print(f"第[{i}]分润领取失败---[{r['msg']}]")
            time.sleep(random.randint(3,10))
    
    def do_t(self):
        # 阅读任务
        t = 0
        url = "http://mcw.bfyxh.cn/api/project/getlist"
        d = {"limit":21,"page":1}
        r = requests.post(url,headers=self.h,json=d).json()
        if r['code'] == 0:
            for i in r['data']['data']:
                id = i.get("id")
                d = {"id":f"{id}"}
                url = "http://mcw.bfyxh.cn/api/project/readproject"
                r = requests.post(url,headers=self.h,json=d).json()
                if r['code'] == 0:
                    print(f"[{id}]阅读成功")
                    t += 1
                else:
                    print(f"[{id}]阅读失败---[{r['msg']}]")
                if t == 10:
                    break
                time.sleep(random.randint(8,15))
        
        # 点赞任务

        #傻逼平台

        # 领取
        id_list = [1,5,9]
        url = "http://mcw.bfyxh.cn/api/task/getactivity"
        for i in id_list:
            d = {"id":i}
            r = requests.post(url,headers=self.h,json=d).json()
            if r['code'] == 0:
                print(f"第[{i}]活跃度任务奖励领取成功")
            else:
                print(f"第[{i}]活跃度任务奖励领取失败---[{r['msg']}]")
            time.sleep(random.randint(8,15))





    

    def main(self):
        self.get_t()
        self.do_t()
        self.task()

if __name__ == '__main__':
    cookie = ''
    if not cookie:
        cookie = os.getenv("yuanshen_mcw")
        if not cookie:
            print("请设置环境变量:yuanshen_mcw")
            exit()
    cookies = cookie.split("@")
    print(f"一共获取到{len(cookies)}个账号")
    i = 1
    for cookie in cookies:
        print(f"\n--------开始第{i}个账号--------")
        main = yuanshen(cookie)
        main.main()
        print(f"--------第{i}个账号执行完毕--------")
        time.sleep(20)
        i += 1
