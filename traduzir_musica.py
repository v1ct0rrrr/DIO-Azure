import requests, os
from dotenv import load_dotenv


load_dotenv()
key = os.getenv("AZURE_KEY")
region = os.getenv("AZURE_REGION")
url = "https://api.cognitive.microsofttranslator.com/translate?api-version=3.0&from=en&to=pt-br"


with open("textos/nihil.txt", "r", encoding="utf-8") as arquivo:
    texto_ingles = arquivo.read()


headers = {
    'Ocp-Apim-Subscription-Key': key,
    'Ocp-Apim-Subscription-Region': region,
    'Content-type': 'application/json'
}
body = [{'text': texto_ingles}]

response = requests.post(url, headers=headers, json=body)
resultado = response.json()


texto_traduzido = resultado[0]['translations'][0]['text']

print("Tradução:\n", texto_traduzido)

with open("textos/musica_traduzida.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(texto_traduzido)

