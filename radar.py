import requests

TOKEN="SEU_TOKEN"
CHAT_ID="5965060661"

url=f"https://api.telegram.org/bot{TOKEN}/sendMessage"

requests.post(url,data={
    "chat_id":CHAT_ID,
    "text":"🚀 Radar funcionando"
})
