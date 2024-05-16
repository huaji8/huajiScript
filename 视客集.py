#   --------------------------------注释区--------------------------------
#   入口https://app.cqskj.com/h5/#/pages/public/register?code=JSHNOH
#   抓任意接口 authorization参数的值
#   抓任意接口 PHPSESSID的值 [ PHPSESSID= 不要放进ck里面 凸(艹皿艹 ) ] 
#   抓任意接口 macid的值
#   变量:yuanshen_skj 多号： @分割
#   格式：authorization的值# PHPSESSID的值 # macid的值
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

