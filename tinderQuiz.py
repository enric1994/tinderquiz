#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import data
import telegramMessaging
import pynder
import quiz
import autoLiker

# commit lol 2 new branch
fbUsername = data.get('fbUser')
fbPass = data.get('fbPass')

fbID = data.get('fbID')
token = data.get('fbToken')
telegramToken = data.get('telegramToken')

telegramMessaging.sendMessage('Project Tinder started!')

while True:

    session = pynder.Session(facebook_id=fbID, facebook_token=token)

    # auto like
    if session.likes_remaining > 0:
        telegramMessaging.sendMessage('started autolike:')
        autoLiker.doAutoLike(fbID, token)

    # check the state of the matches and ask questions
    matches = [m for m in session.matches()]
    for y in range(0, len(matches)):
        state = quiz.checkState(matches[y])
        quiz.checkAnswers(state, matches[y])

    time.sleep(3)
