#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

import pynder

import autoLiker
import telebot

import getToken
import quiz
#commit lol
fbUsername='surtdeloutet@gmail.com'
fbPass='12345aAaAa'
fbID=100019273237047
token='EAAGm0PX4ZCpsBAFYdo5NsC4RSNXZBCWHRVZAWgL50N0ohNJsHHkvQAwG8K57pW0pBiZBMUwvitRaWB02Y9Y4oa9YZBWxZB4S2GR64XrO4rDb86YDqRKsHeeccxSlb4Du4IRA05joR2IPPM3Vh8rczmALcgnLDvwqaUkzLVtdRc8C0HvBPnDy0MQxpRqU9teErCHTas9XiB3LariK18EMIhnaOLoRTOIQZBVZC3dQDycUAxAifqKw0PWS'
telegramToken = '252299965:AAG-8H4z7QeQkFztEyEoyfl8ei5mauFhTEY'

bot = telebot.TeleBot(telegramToken)
bot.config['api_key'] = telegramToken

lastToken = 0
lastLikes = 0
bot.send_message(10951183, "Project Tinder Quiz started")

while True:
    '''
    # Refresh the token every hour
    if  time.time() - lastToken > 60*60:
        print 'getting token...'
        token = temporaltoken #getToken.getToken(fbUsername, fbPass)
        if token ==-1:
            print 'error obtaining token'
            bot.send_message(10951183, "CRASH: error obtaining token")

        lastToken = time.time()
    # AutoLike every 13h
    if time.time()-lastLikes > 3600*13:
        session = pynder.Session(facebook_id=fbID, facebook_token=token)
        if session.likes_remaining > 0:
            bot.send_message(10951183, "AutoLiker ON")
            print 'started autoLiker'
            autoLiker.autoLike(session)
            print 'finished autoLiker'
            lastLikes=time.time()
    '''
    # check the state of the matches and ask questions
    time.sleep(2)
    quiz.quiz(fbID,token)
