#   --------------------------------注释&变量区--------------------------------
#   入口 https://kaifang.qukandrama.com/api/user/register/QFAhAn4Ton
#   一天一次
#   变量:yuanshen_qk 多号@分割
#   抓取Authorization填入即可
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
import os
def version():
    txt = requests.get("https://gitee.com/HuaJiB/yuanshen34/raw/master/pubilc.txt").text
    print(txt)

class yuanshen:
    def __init__(self,cookie):
        self.cookie = cookie
        self.header = {
   "Authorization": f"{self.cookie}",
   "user-agent": "Mozilla/5.0 (Linux; Android 13; 23054RA19C Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 uni-app Html5Plus/1.0 (Immersed/36.363636)",
   "Content-Type": "application/json",
   "Host": "api.qukandrama.com",
   "Connection": "Keep-Alive",
   "Accept-Encoding": "gzip"
}
        
    def task(self):
        url = "https://api.qukandrama.com/api/score/receiveBonus"
        r = requests.post(url,headers=self.header).json()
        if r['code'] == 200:
            print(f"🎉️领取分红成功,获得{r['data']['money']}元")
        else:
            print(f"领取分红失败,[{r}]")

    def userinfo(self):
        url = "https://api.qukandrama.com/api/user/profile"
        r = requests.post(url,headers=self.header).json()
        if r['code'] == 200:
            print(f"🎉️账号{r['data']['username']} 当前剩余看点[{r['data']['score']}] 当前余额[{r['data']['money']}]")
        else:
            print(f"获取账号信息失败,[{r['msg']}]")

        
    def main(self):
        self.task()
        self.userinfo()

if __name__ == '__main__':

    cookie = ''
    if not cookie:
        cookie = os.getenv("yuanshen_qk")
        if not cookie:
            print("❌你还没有设置ck,请设置环境变量:yuanshen_qk")
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
    
