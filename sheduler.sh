#!/bin/bash
until tinderQuiz.py; do
    echo "'tinderQuiz' crashed with exit code $?. Restarting..." >&2
    sleep 1
done