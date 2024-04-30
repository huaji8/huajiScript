#   --------------------------------注释区--------------------------------
#   入口:http://r.zsxx.tuesjf.cn?type=1&share_code=DB0LF3
#   抓token参
#   变量: yuanshen_zsxx 多号： @分割
#   格式: token
#   晚饭 看广告卖那个什么灵石 每天0.25自己卖
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
import zlib, base64
exec(zlib.decompress(base64.b64decode('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')))


