import schedule
import time
import requests
import json
import sys

# 웹훅 URL 설정
webhook_url = 'https://hook.swit.io/chat/221130071859018CeVZ/UpsUot1KdTVZuzbZb4ab?organization_id=221115053512172hCrx'

# 메시지를 보내는 함수
def send_message():
    payload = {
        'text': '주간회의 보고서 작성 하셨나요?'
    }
    response = requests.post(webhook_url, data=json.dumps(payload), headers={'Content-Type': 'application/json'})

    if response.status_code == 200:
        print('메시지가 성공적으로 전송되었습니다.')
        
    else:
        print(f'메시지 전송 실패: {response.status_code}, {response.text}')

send_message()
#매일 오후 5시에 send_message 함수를 실행하도록 스케줄링
schedule.every().day.at("18:00").do(send_message)
time.sleep(31)
