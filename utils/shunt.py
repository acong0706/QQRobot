import requests
import datetime


from utils.commands import help_command
from utils.otherMsgRet import otherMsg


def shunt_of_keyword(message, uid, gid=None):
    # 目前暂时没有处理群信息
    token = ''
    if gid is None:
        # 处理逻辑
        # message分析判断是什么指令
        if message[0:1] == '/':
            # 根据空格进行切分（目的是希望一些指令带有各自参数，并且通过空格进行隔开）
            messages = message.split()
            order_now = messages[0][1:]
            if order_now == '帮助':
                return_msg = help_command()
                print(return_msg)
            elif order_now == '时间':
                return_msg = '当前时间为' + datetime.datetime.now().strftime('%Y年%m月%d日 %H:%M:%S')
            elif order_now == '回声':
                if len(messages) > 1:
                    return_msg = '返回信息如下：'
                    for i in range(len(messages)-1):
                        return_msg += '\n' + messages[i+1]
                else:
                    return_msg = '请输入参数！！！'
            else:
                return_msg = '暂时当前指令'
        else:
            return_msg = otherMsg(message)

        # 最终返回的数据
        data = {
            "user_id": uid,
            "message": return_msg
        }
        requests.post(url='http://127.0.0.1:5700/send_private_msg?access_token={token}', data=data, timeout=5)
