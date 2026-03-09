import requests
import re
from datetime import datetime

TOKEN="SEU_TOKEN"
CHAT_ID="5965060661"

headers={
"User-Agent":"Mozilla/5.0"
}

def alerta(msg):

    url=f"https://api.telegram.org/bot8735265703:AAF-iaDIDuDLujTSzAuShHSSdcXtTr7HDag/sendMessage"

    requests.post(url,data={
        "chat_id":CHAT_ID,
        "text":msg
    })


def extrair_preco(html):

    precos=re.findall(r"R\$ ?[0-9\.,]+",html)

    valores=[]

    for p in precos:

        v=p.replace("R$","").replace(".","").replace(",",".").strip()

        try:
            valor=float(v)

            # evita pegar parcelas
            if valor > 300:
                valores.append(valor)

        except:
            pass

    if valores:
        return max(valores)

    return None



def identificar_loja(url):

    if "kabum" in url:
        return "🟦 KaBuM"
    if "pichau" in url:
        return "🟩 Pichau"
    if "terabyte" in url:
        return "🟧 Terabyte"
    if "amazon" in url:
        return "🟨 Amazon"
    if "mercadolivre" in url:
        return "🟪 Mercado Livre"

    return "Loja"


produtos={

"🖥️ Ryzen 5 7600":[

"https://www.kabum.com.br/busca/ryzen-7600",
"https://www.pichau.com.br/search?q=ryzen%207600",
"https://www.terabyteshop.com.br/busca?str=ryzen+7600"

],

"🎮 RX 7600":[

"https://www.kabum.com.br/busca/rx-7600",
"https://www.pichau.com.br/search?q=rx%207600",
"https://www.terabyteshop.com.br/busca?str=rx+7600"

],

"🧠 DDR5 2x8GB":[

"https://www.kabum.com.br/busca/ddr5-16gb-2x8",
"https://www.pichau.com.br/search?q=ddr5%202x8",
"https://www.terabyteshop.com.br/busca?str=ddr5+2x8"

]

}



hora=datetime.now().strftime("%d/%m %H:%M")

alerta(f"🛰️ Radar de Hardware ativo\n⏱️ {hora}\n🔎 Iniciando varredura...")


for produto,urls in produtos.items():

    for url in urls:

        try:

            r=requests.get(url,headers=headers,timeout=10)

            html=r.text

            preco=extrair_preco(html)

            loja=identificar_loja(url)

            if preco:

                mensagem=f"""
🔥 POSSÍVEL OFERTA DETECTADA

📦 Produto
{produto}

💰 Preço encontrado
R$ {preco}

🏪 Loja
{loja}

🔗 Ver oferta
{url}

⏱️ Detectado em
{hora}

🤖 Radar automático
"""

                alerta(mensagem)

        except:

            pass
