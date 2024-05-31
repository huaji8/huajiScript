#   --------------------------------注释区--------------------------------
#   入口:http://www.xishidaxue.com/h5/reg.html?invite_code=VN1L92 走个头谢谢
#   变量:yuanshen_xishi
#   多号分割方式 [ @ 或 换行 或 新建同名变量 ]
#   抓取Authorization的值填入
#   corn: 一天一次即可
#   注意先在主页实名领取学籍卡
#   养老城模式一个夕拾币0.1元上涨，可转赠与提现
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
exec(bz2.decompress(base64.b64decode('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')))
