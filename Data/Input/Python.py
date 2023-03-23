import requests

def fetch_data():

    url = "https://www.4devs.com.br/ferramentas_online.php"

    payload="acao=gerar_pessoa&sexo=I&idade=0&txt_qtde=20"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    response = requests.request("POST", url, headers=headers, data=payload)

    res = response.text

    return res