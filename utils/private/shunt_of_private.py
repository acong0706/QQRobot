import requests
from utils.private.help import help_command
from utils.private.otherMsgRet import otherMsg
from utils.private.easyCommands import easyCommands


def keyword_private(message, uid, gid=None):
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
            else:
                return_msg = easyCommands(order_now, messages)
        else:
            return_msg = otherMsg(message)

        # 最终返回的数据
        data = {
            "user_id": uid,
            "message": return_msg
        }
        requests.post(url='http://127.0.0.1:5700/send_private_msg?access_token={token}', data=data, timeout=5)
