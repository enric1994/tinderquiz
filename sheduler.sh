#!/bin/bash
until python tinderQuiz.py; do
    echo "'tinderQuiz' crashed with exit code $?. Restarting..." >&2
    sleep 10
done