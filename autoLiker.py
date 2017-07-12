#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

def autoLike(session):
    while session.likes_remaining > 0:
        near = session.nearby_users()
        for i in near:
            if session.likes_remaining == 0:
                print("no more likes")
                break
            print('------------------------')
            print(i.name)
            i.like()
