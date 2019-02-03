import itchat
import time

def send_msg_to_friend(one_fri, one_msg):
    friend = itchat.search_friends(userName=one_fri['UserName'])
    if '%s' in one_msg:
        # a msg contain username
        itchat.send_msg(one_msg % (friend['RemarkName'] or friend['NickName']), 
                                    toUserName=friend['UserName'])
    else:
        # a common msg 
        itchat.send_msg(one_msg, toUserName=friend['UserName'])


def send_msg_to_tester(one_fri, one_msg):
    friend = itchat.search_friends(userName=one_fri['UserName'])
    if '%s' in one_msg:
        # a msg contain username
        itchat.send_msg(one_msg % (friend['RemarkName'] or friend['NickName']), 
                                    toUserName='filehelper')
    else:
        # a common msg 
        itchat.send_msg(one_msg, toUserName='filehelper')


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
        for friend in chatroom['MemberList']:
            send_msg_to_friend(friend, str_msg)
            time.sleep(1)


def group_send_tester(group_name, str_msg):
    chatroomName = group_name
    itchat.get_chatrooms(update=True)
    chatrooms = itchat.search_chatrooms(name=chatroomName)
    # no chatroom name error
    if chatrooms is None or len(chatrooms) == 0:
        itchat.send_msg(u'没有找到群聊：' + chatroomName, toUserName='filehelper')
    # sending msg to chatroom
    else:
        chatroom = itchat.update_chatroom(chatrooms[0]['UserName'])
        tester_msg = '群聊名称：' + group_name + '\n群成员包括：'
        tester_msg = tester_msg + chatroom['MemberList'][0]['NickName'] + ' 等' + str(len(chatroom['MemberList'])) + '名成员'
        itchat.send_msg(tester_msg, toUserName='filehelper')
        send_msg_to_tester(chatroom['MemberList'][0], str_msg)



def group_each_send_helper():
    helper_msg = '群发消息助手帮助：\n基础指令：群发消息 [群名称] [消息]\n发送消息进阶：\
    群发时若想自动替换消息中的人名（仅一个，且为对方的备注名/昵称）用%s代替，例：\n群发消息 祝福群 祝%s新年快乐！'
    itchat.send_msg(helper_msg, toUserName='filehelper')


def group_send_test_helper():
    helper_msg = '测试群发消息帮助：\n基础指令：测试群发消息 [群名称] [消息]\n用来测试发送的群聊成员是否正确'
    itchat.send_msg(helper_msg, toUserName='filehelper')