import itchat
import time

def group_each_send(group_name, str_msg):
    chatroomName = group_name
    itchat.get_chatrooms(update=True)
    chatrooms = itchat.search_chatrooms(name=chatroomName)
    # no chatroom name error
    if chatrooms is None or len(chatrooms) == 0:
        itchat.send_msg(u'没有找到群聊：' + chatroomName, toUserName='filehelper')
    # sending msg to chatroom
    else:
        chatroom = itchat.update_chatroom(chatrooms[0]['UserName'])
        # a msg contain username
        if '%s' in str_msg:
            for friend in chatroom['MemberList']:
                friend = itchat.search_friends(userName=friend['UserName'])
                itchat.send_msg(str_msg % (friend['RemarkName'] or friend['NickName']), 
                                toUserName=friend['UserName'])
                time.sleep(.5)
        # a common msg 
        else:
            for friend in chatroom['MemberList']:
                friend = itchat.search_friends(userName=friend['UserName'])
                itchat.send_msg(str_msg, toUserName=friend['UserName'])
                time.sleep(.5)

def group_each_send_helper():
    helper_msg = '群发消息助手帮助：\n基础指令：群发消息 [群名称] [消息]\n发送消息进阶：\
    群发时若想自动替换消息中的人名（仅一个，且为对方的备注名/昵称）用%s代替，例：\n群发消息 祝福群 祝%s新年快乐！'
    itchat.send_msg(helper_msg, toUserName='filehelper')