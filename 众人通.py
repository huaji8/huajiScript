#   --------------------------------注释区--------------------------------
#   一区入口http://zrht.sxjcp.fun/index/wechat/login?share=HCQqKm
#   二区入口http://zrt2.716jcp.fun/index/wechat/login?share=sfC51Q
#   三区入口http://zz3q.716jcp.fun/index/wechat/login?share=OwgQqS
#   五区入口http://k2.716jcp.fun/index/wechat/login?share=j9ZiDq
#   六区入口http://k3.716jcp.fun/index/wechat/login?share=nck2T9
#   抓任意请求头的token 把值全部塞进去 哪个区就填哪个区的序号 填完后运行
#   每一个区数据不互通 好像还有其他区 知道的联系下我
#   可能有bug会无限循环 自己注意下
#   变量:yuanshen_zrt#你的对应区号   多号： @分割
#   例如 aaabbccc#1@bbbcccddd#2
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
