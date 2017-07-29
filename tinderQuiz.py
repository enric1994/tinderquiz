#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import data
import telegramMessaging
import pynder
import quiz
import autoLiker
import updateToken

updateToken.update()

fbUsername = data.get('fbUser')
fbPass = data.get('fbPass')

fbID = data.get('fbID')
token = data.get('fbToken')
telegramToken = data.get('telegramToken')

print 'Project Tinder started!'
telegramMessaging.sendMessage('Project Tinder started!')

while True:
    token = data.get('fbToken')
    session = pynder.Session(facebook_id=fbID, facebook_token=token)

    # auto like
    try:
        if session.likes_remaining > 0:
            autoLiker.doAutoLike(fbID, token)
    except:
        print 'error in autolike'
    # check the state of the matches and ask questions
    try:
        matches = [m for m in session.matches()]
        for y in range(0, len(matches)):
            state = quiz.checkState(matches[y])
            quiz.checkAnswers(state, matches[y])
    except:
        print 'ERROR in quiz'
    time.sleep(3)
