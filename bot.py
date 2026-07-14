import requests
from config import BOT_TOKEN, CHAT_ID

message = """🎉 JH Portfolio AI Bot

연결 테스트 성공!

이 메시지가 보인다면
GitHub와 텔레그램이 정상적으로 연결되었습니다.

다음 단계부터는
📈 주식 브리핑 기능을 추가합니다.
"""

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

response = requests.post(
    url,
    data={
        "chat_id": CHAT_ID,
        "text": message
    }
)

print(response.text)
