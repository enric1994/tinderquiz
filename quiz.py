#!/usr/bin/env python
# -*- coding: utf-8 -*-
import texts
import notify
# Check the last question
def checkState(match):
    state = 0
    for x in range(0, len(match.messages)):

        if texts.q1 in str(match.messages[x]):
            state = 1
        if texts.q2 in str(match.messages[x]):
            state = 2
        if texts.q3 in str(match.messages[x]):
            state = 3
        if texts.q4 in str(match.messages[x]):
            state = 4
        if texts.q5 in str(match.messages[x]):
            state = 5
        if texts.q6 in str(match.messages[x]):
            state = 6
        if texts.q7 in str(match.messages[x]):
            state = 7
        if texts.q8 in str(match.messages[x]):
            state = 8
        if texts.q9 in str(match.messages[x]):
            state = 9
        if texts.q10 in str(match.messages[x]):
            state = 10

    return state


# Check the answer for the current question
def checkAnswers(state, match):
    if state == 0:
        match.message(texts.q1)
        notify.matchInfo(match, 0)
    if state == 1:
        for x in range(0, len(match.messages)):
            if 'estocolm' in str(match.messages[x]).lower():
                match.message(texts.q2)
    if state == 2:
        for x in range(0, len(match.messages)):
            if '63' in str(match.messages[x]):
                match.message(texts.q3)
    if state == 3:
        for x in range(0, len(match.messages)):
            if '1492' in str(match.messages[x]):
                match.message(texts.q4)
    if state == 4:
        for x in range(0, len(match.messages)):
            if 'oasis' in str(match.messages[x]).lower():
                match.message(texts.q5)
    if state == 5:
        for x in range(0, len(match.messages)):
            if 'cuyo nombre' in str(match.messages[x]).lower():
                match.message(texts.q6)
    if state == 6:
        for x in range(0, len(match.messages)):
            if 'model' in str(match.messages[x]).lower():
                match.message(texts.q7)
    if state == 7:
        for x in range(0, len(match.messages)):
            if 'tetris' in str(match.messages[x]).lower():
                match.message(texts.q8)
    if state == 8:
        for x in range(0, len(match.messages)):
            if '141' in str(match.messages[x]):
                match.message(texts.q9)
    if state == 9:
        for x in range(0, len(match.messages)):
            if 'strong' in str(match.messages[x]).lower():
                match.message(texts.q10)
                notify.matchInfo(match,1)
