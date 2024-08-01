#   --------------------------------注释区--------------------------------
#   入口:http://230640607122241.asfuoqa.cn/r?upuid=2306406
#   走个头谢谢 不然没更新动力了呜呜呜
#   可乐现在是两套接口轮流换 2.13A提示获取参数异常用2.13B版本 同理2.13B不行用2.13A都不行再反
#   变量:yuanshen_klyd
#   多号分割方式 [ @ 或 换行 或 新建同名变量 ]
#   抓取Cookie中udtauth12的值填入 搜udtauth12
#   在抓取上面的参数时同时抓取请求头中的user-agent填入yuanshen_useragent
#   corn: 一小时一次即可

#   检测配置：
#   在yuanshen_apptoken，yuanshen_topicid分别填入你的wxpusher的apptoken和topicid
#   注意是填的topicid而不是你的uid 不要傻乎乎把uid填上去 填了不推送文章包黑号的
#   不懂看 https://wxpusher.zjiecode.com/docs/#/ 或 百度 或 打钱

withdrawal_money = 3000 #提现金币数量 1000金币=0.1r
Quantity_limit = 180  #阅读上限篇数 跑满(195篇左右)概率封号
fuck_list = [1,2,126] # 强制推送篇数 不懂默认别瞎改 需要新加的话在后面用 英文逗号加篇数 就行 
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
'''
Powered By Huaji
Create at [2024-07-30 14:52]

 __    __   __    __       ___             __   __  
|  |  |  | |  |  |  |     /   \           |  | |  | 
|  |__|  | |  |  |  |    /  ^  \          |  | |  | 
|   __   | |  |  |  |   /  /_\  \   .--.  |  | |  | 
|  |  |  | |  `--'  |  /  _____  \  |  `--'  | |  | 
|__|  |__|  \______/  /__/     \__\  \______/  |__|                                                

'''

import base64, zlib, lzma, bz2, gzip
exec((lambda c: compile(c,'<string>','exec'))(zlib.decompress(lzma.decompress(bz2.decompress(gzip.decompress(base64.b64decode('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')))))。decode()))
#!Look Your Mother! At the end there was nothing!
