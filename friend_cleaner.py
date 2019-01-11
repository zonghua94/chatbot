import itchat

# add_member_into_chatroom 功能已经不可用
def get_friend_status(group_name):
    chatroomName = group_name
    itchat.get_chatrooms(update=True)
    chatrooms = itchat.search_chatrooms(name=chatroomName)
    friend = itchat.get_friends()[1]
    r = itchat.add_member_into_chatroom(chatrooms[0]['UserName'], [friend])
    if r['BaseResponse']['ErrMsg'] == '':
        status = r['MemberList'][0]['MemberStatus']
        itchat.delete_member_from_chatroom(chatrooms[0]['UserName'], [friend])
        print({ 3: u'该好友已经将你加入黑名单。',
            4: u'该好友已经将你删除。', }.get(status,
            u'该好友仍旧与你是好友关系。'))
    else:
        print(u'无法获取好友状态，预计已经达到接口调用限制。')