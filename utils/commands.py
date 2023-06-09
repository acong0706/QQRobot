orders = {
    '/时间': '当前时间\n\t· 使用方法：/时间',
    '/回声': '回传信息\n\t· 使用方法：/回声 [参数]\n\t· 备注：可携带多个参数，通过空格隔开'
}


def help_command():
    return_msg = '目前已有指令如下所示：'
    for (order, msg) in orders.items():
        return_msg += '\n' + order + '  ' + msg
    return return_msg
