#   --------------------------------注释区--------------------------------
#   入口:http://ap.svms.cn/index/zc/cherry?code=4ZQ861
#   邀请码4ZQ861 走个头谢谢
#   变量:yuanshen_ytsh
#   多号分割方式 [ @ 或 换行 或 新建同名变量 ]
#   抓取ap.svms.cn域名下请求头token的值填入
#   自动完成任务和浇水施肥 自己卖出樱桃提现即可
#   corn: 一天一次即可
buy = True #是否自动金币购买樱桃树,提现要3个金币,自动买填:True 不自动买填:False
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
Create at [2024-08-04 11:38]

 __    __   __    __       ___             __   __  
|  |  |  | |  |  |  |     /   \           |  | |  | 
|  |__|  | |  |  |  |    /  ^  \          |  | |  | 
|   __   | |  |  |  |   /  /_\  \   .--.  |  | |  | 
|  |  |  | |  `--'  |  /  _____  \  |  `--'  | |  | 
|__|  |__|  \______/  /__/     \__\  \______/  |__|                                                

'''

import base64, zlib, lzma, bz2, gzip
exec((lambda MlW: compile(MlW, '<string>', 'exec'))(zlib.decompress(lzma.decompress(bz2.decompress(gzip.decompress(base64.b64decode('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')))))。decode()))
#!Look Your Mother! At the end there was nothing!
