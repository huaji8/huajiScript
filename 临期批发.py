#   --------------------------------注释区--------------------------------
#   入口:微信扫码：https://gitee.com/HuaJiB/yuanshen34/raw/master/lqpf.jpg
#   变量:yuanshen_lqpf
#   多号分割方式 [ @ 或 换行 或 新建同名变量 ]
#   抓取shop.linqishop.com下任意请求头的token的值填入
#   corn: 每日21点运行即可
#   一日出三单 一天3r 1r起提现 无自动提现
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
import bz2, base64
exec(bz2.decompress(base64.b64decode('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秒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')))
