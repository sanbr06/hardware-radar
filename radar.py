import requests

TOKEN="SEU_TOKEN"
CHAT_ID="5965060661"

def alerta(msg):

    url=f"https://api.telegram.org/bot8735265703:AAF-iaDIDuDLujTSzAuShHSSdcXtTr7HDag/sendMessage"

    requests.post(url,data={
        "chat_id":CHAT_ID,
        "text":msg
    })


headers={
    "User-Agent":"Mozilla/5.0"
}

produtos={

"Ryzen 7600":[

"https://www.kabum.com.br/busca/ryzen-7600",
"https://www.pichau.com.br/search?q=ryzen%207600",
"https://www.terabyteshop.com.br/busca?str=ryzen+7600",
"https://www.amazon.com.br/s?k=ryzen+7600",
"https://lista.mercadolivre.com.br/ryzen-7600"

],

"RX 7600":[

"https://www.kabum.com.br/busca/rx-7600",
"https://www.pichau.com.br/search?q=rx%207600",
"https://www.terabyteshop.com.br/busca?str=rx+7600",
"https://www.amazon.com.br/s?k=rx+7600",
"https://lista.mercadolivre.com.br/rx-7600"

],

"DDR5 2x8GB":[

"https://www.kabum.com.br/busca/ddr5-16gb-2x8",
"https://www.pichau.com.br/search?q=ddr5%202x8",
"https://www.terabyteshop.com.br/busca?str=ddr5+2x8",
"https://www.amazon.com.br/s?k=ddr5+2x8+16gb",
"https://lista.mercadolivre.com.br/ddr5-16gb-2x8"

]

}

for produto,urls in produtos.items():

    for url in urls:

        try:

            r=requests.get(url,headers=headers,timeout=10)

            if r.status_code==200:

                alerta(f"🔎 Monitorando {produto}\n{url}")

        except:

            pass
