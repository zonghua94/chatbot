import itchat
import time
import group_send

def bot_helper():
    bot_msg = '微信机器人帮助：\n功能列表：群发消息\n回复指定功能名称，获取功能使用帮助！'
    itchat.send_msg(bot_msg, toUserName='filehelper')

@itchat.msg_register([itchat.content.TEXT], isFriendChat=False, isGroupChat=False, isMpChat=False)
def file_helper_bot(msg):
    if msg['ToUserName'] == 'filehelper':
        # analys command
        master_command = msg['Content'].split(' ', 2)
        # bot helper
        if master_command[0] == '召唤机器人':
            bot_helper()
        # group send command
        elif master_command[0] == '群发消息':
            # group send helper
            if len(master_command) != 3:
                group_send.group_each_send_helper()
            # begin group send
            else:
                itchat.send_msg('正在向 %s 群发消息，发送内容为:\n%s\n开始发送......' 
                                % (master_command[1], master_command[2]), 
                                toUserName='filehelper')
                group_send.group_each_send(master_command[1], master_command[2])
        # friend leaner
        elif master_command[0] == '清理好友':
            itchat.send_msg('网页版微信无法将好友加入群聊，该功能不可用！', toUserName='filehelper')
        else:
            print('命令错误')

itchat.auto_login(enableCmdQR=2, hotReload=True)
login_msg = '发送 召唤机器人 获取功能帮助'
itchat.send_msg(login_msg, toUserName='filehelper')
itchat.run()