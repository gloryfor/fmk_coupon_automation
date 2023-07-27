
알아둘것
* ~~chromedriver는 각 arch별로 다운받아 지정할것 (default: arm64)~~  이제 안받아도 됩니다.
* ~~https://chromedriver.chromium.org/downloads~~
* Naver, Google 로그인 됨!!!

사전준비
* python3 -m venv env
* source env/bin/activate
* pip3 install -r requirements.txt
* deactivate

Chrome 현재창에서 selenium 스크립트 실행을 위해 
* /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222


venv pip 패키지 업그레이드
```bash
(venv) pip3 install --upgrade pip
(venv) pip3 install -r requirements.txt --upgrade
(venv) pip3 freeze > ./requirements.txt
```