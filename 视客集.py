#   --------------------------------注释区--------------------------------
#   入口https://app.cqskj.com/h5/#/pages/public/register?code=JSHNOH
#   抓任意接口 authorization参数的值
#   抓任意接口 PHPSESSID的值 [PHPSESSID= 不要放进ck里面 凸(艹皿艹 )] 
#   抓任意接口 macid的值
#   变量:yuanshen_skj 多号： @分割
#   格式：authorization的值# PHPSESSID的值 # macid的值
#   任务显示操作失败是正常的 重跑就行了 我也不知道为什么失败hh
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
import bz2, base64
exec(bz2.decompress(base64.b64decode('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')))
