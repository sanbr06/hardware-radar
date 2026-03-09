import requests
import re
import json
import os
from datetime import datetime

TOKEN="SEU_TOKEN"
CHAT_ID="5965060661"

HEADERS={"User-Agent":"Mozilla/5.0"}

ARQUIVO="historico_precos.json"


def telegram_foto(msg,foto):

    url=f"https://api.telegram.org/bot{TOKEN}/sendPhoto"

    requests.post(url,data={
        "chat_id":CHAT_ID,
        "caption":msg,
        "photo":foto
    })


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


def extrair_precos(html):

    precos=re.findall(r"R\$ ?[0-9\.,]+",html)

    valores=[]

    for p in precos:

        v=p.replace("R$","").replace(".","").replace(",",".").strip()

        try:

            valor=float(v)

            if valor>150:
                valores.append(valor)

        except:
            pass

    return valores


def extrair_imagem(html):

    img=re.search(r'https://http[^"]+\.(jpg|png)',html)

    if img:
        return img.group()

    return None


produtos={

"🖥 Ryzen 7600":[

"https://www.kabum.com.br/busca/ryzen-7600",
"https://www.pichau.com.br/search?q=ryzen%207600",
"https://www.terabyteshop.com.br/busca?str=ryzen+7600",
"https://www.amazon.com.br/s?k=ryzen+7600",
"https://lista.mercadolivre.com.br/ryzen-7600"

],

"🎮 RX 7600":[

"https://www.kabum.com.br/busca/rx-7600",
"https://www.pichau.com.br/search?q=rx%207600",
"https://www.terabyteshop.com.br/busca?str=rx+7600",
"https://www.amazon.com.br/s?k=rx+7600",
"https://lista.mercadolivre.com.br/rx-7600"

],

"🧠 DDR5 8GB 5200MHz":[

"https://www.kabum.com.br/busca/ddr5-8gb-5200",
"https://www.pichau.com.br/search?q=ddr5%208gb%205200",
"https://www.terabyteshop.com.br/busca?str=ddr5+8gb+5200",
"https://www.amazon.com.br/s?k=ddr5+8gb+5200",
"https://lista.mercadolivre.com.br/ddr5-8gb-5200"

]

}


if os.path.exists(ARQUIVO):

    historico=json.load(open(ARQUIVO))

else:

    historico={}


hora=datetime.now().strftime("%d/%m %H:%M")


for produto,urls in produtos.items():

    for url in urls:

        try:

            r=requests.get(url,headers=HEADERS,timeout=10)

            html=r.text

            precos=extrair_precos(html)

            if not precos:
                continue

            preco=min(precos)

            loja=identificar_loja(url)

            chave=f"{produto}-{loja}"

            preco_antigo=historico.get(chave)

            if preco_antigo and preco>=preco_antigo:
                continue

            historico[chave]=preco

            imagem=extrair_imagem(html)

            mensagem=f"""
🚨 ALERTA DE OFERTA

📦 Produto
{produto}

🏪 Loja
{loja}

💰 Preço
R$ {preco}

🔗 Link
{url}

⏰ {hora}
"""

            if imagem:
                telegram_foto(mensagem,imagem)

        except:
            pass


json.dump(historico,open(ARQUIVO,"w"))
