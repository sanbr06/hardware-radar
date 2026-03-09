import requests

TOKEN="SEU_TOKEN"
CHAT_ID="5965060661"

def alerta(msg):
    url=f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url,data={"chat_id":CHAT_ID,"text":msg})

r=requests.get("https://www.kabum.com.br/busca/ryzen-7600")

if "ryzen 7600" in r.text.lower():
    alerta("Radar monitorando Ryzen 7600")
