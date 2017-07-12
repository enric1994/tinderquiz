#!/bin/bash
while :
do
echo 'project tinder started'
python /home/tinderquiz/tinderQuiz.py
sleep 8000
pkill python
done
