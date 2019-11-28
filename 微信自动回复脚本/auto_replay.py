# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 16:37:07 2019

@author: lee
"""

import re
import time

import itchat
from itchat.content import *


#单人聊天（文本）
@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    reply = r'1'
    replay_friend = ['莫奈的雨露', '咸鱼饭丶']  
    name = itchat.search_friends(userName=msg['FromUserName'])['NickName']
    if name in replay_friend:
        message = msg['Text']
        if u'玉泉' in message and u'讲解' in message and u'报名' in message:
            return reply

#群聊（文本）
@itchat.msg_register(itchat.content.TEXT, isGroupChat=True)
def group_text_reply(msg):
    reply = r'1'
    name = itchat.search_chatrooms(userName=msg['FromUserName'])['NickName']
    
    if name == u'Lab306活跃群': #换成自己群的名称
        print(name)
        print(msg['Text'])
        message = msg['Text']
        if u'玉泉' in message and u'讲解' in message and u'报名' in message:
#        # 当然如果只想针对@你的人才回复，可以设置if msg['isAt']:
#        if msg['isAt']:
#            return reply
            return reply 
        

if __name__ == '__main__':#启动微信自动登录，二维码登录
    itchat.auto_login(hotReload=True)
    itchat.run()