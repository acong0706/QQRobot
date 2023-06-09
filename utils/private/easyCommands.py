import datetime


def easyCommands(order_now, messages):
    if order_now == '时间':
        return_msg = '当前时间为' + datetime.datetime.now().strftime('%Y年%m月%d日 %H:%M:%S')
    elif order_now == '回声':
        if len(messages) > 1:
            return_msg = '返回信息如下：'
            for i in range(len(messages) - 1):
                return_msg += '\n' + messages[i + 1]
        else:
            return_msg = '请输入参数！！！'
    else:
        return_msg = '暂时当前指令'

    return return_msg
