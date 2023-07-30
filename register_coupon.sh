#!/bin/sh

## Chrome 종료
kill -9 $(ps aux | grep -v "grep" | grep "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" | awk '{print $2}')

## Chrome debugger 열어서 띄우기
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 &
CHROME_PID=$!
sleep 3

source venv/bin/activate
python3 ./main.py -a
#python3 ./main.py -c 나맨시T야 -c 쿠폰2 -c 쿠폰3

deactivate

## Chrome 종료
kill -9 ${CHROME_PID}
