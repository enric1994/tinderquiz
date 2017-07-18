#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pynder
import telegramMessaging


def doAutoLike(fbID, token):
    session = pynder.Session(facebook_id=fbID, facebook_token=token)
    near = session.nearby_users()
    for i in near:
        if session.likes_remaining == 0:
            telegramMessaging.sendMessage('Likes exhausted')
            break
        i.like()
