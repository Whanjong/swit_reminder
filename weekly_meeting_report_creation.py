import requests
import json
import os

# GitHub Secrets에서 불러오기
webhook_url = os.environ.get("SWIT_WEBHOOK_URL")

def send_message():
    payload = {
        'text': '주간회의 보고서 작성 하셨나요?'
    }
    response = requests.post(webhook_url, data=json.dumps(payload), headers={'Content-Type': 'application/json'})
    if response.status_code == 200:
        print('메시지가 성공적으로 전송되었습니다.')
    else:
        print(f'메시지 전송 실패: {response.status_code}, {response.text}')

if __name__ == "__main__":
    send_message()
