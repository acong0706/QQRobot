def otherMsg(message):
    if message == '我爱你' or message == '我喜欢你':
        return_msg = '我也是，宝。'
    else:
        return_msg = '指令使用错误，请输入"/帮助"获取全部指令'
    return return_msg
