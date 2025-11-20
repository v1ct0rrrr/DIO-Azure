import requests, os, uuid
from bs4 import BeautifulSoup
from dotenv import load_dotenv


load_dotenv()
subscription_key = os.getenv("AZURE_KEY")
region = os.getenv("AZURE_REGION")
endpoint = "https://api.cognitive.microsofttranslator.com"


url_artigo = 'https://dev.to/kenakamu/azure-open-ai-in-vnet-3alo'


def extrair_texto_site(url):
    print("1. Acessando o site...")

    headers_fake = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers_fake)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    for lixo in soup(['script', 'style', 'nav', 'footer', 'header', 'aside']):
        lixo.decompose()

    conteudo = soup.find(id='article-body')
    
    if not conteudo:
        conteudo = soup.find('article')
    if not conteudo:
        conteudo = soup.find('main')

    if conteudo:
        texto = conteudo.get_text(separator='\n', strip=True)
    else:
        texto = soup.get_text(separator='\n', strip=True)
        
    return texto


def traduzir_texto(texto_ingles):
    print("2. Enviando para o Azure Translator...")
    path = '/translate'
    constructed_url = endpoint + path

    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Ocp-Apim-Subscription-Region': region,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    
    tamanho = len(texto_ingles)
    print(f"Tamanho total: {tamanho} caracteres.")

    if tamanho > 50000:
        print("Aviso: O texto é maior que o limite do Azure (50k). Cortando para 50k...")
        texto_ingles = texto_ingles[:50000]

    body = [{'text': texto_ingles}]
    
    params = {
        'api-version': '3.0',
        'from': 'en',
        'to': 'pt-br'
    }

    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()
    
   
    try:
        return response[0]["translations"][0]["text"]
    except:
        return f"Erro na tradução: {response}"


texto_original = extrair_texto_site(url_artigo)


texto_traduzido = traduzir_texto(texto_original)


print("3. Salvando arquivo...")
texto_traduzido = "# Tradução do Artigo\n\n" + texto_traduzido
with open('textos/artigo_traduzido.md', 'w', encoding='utf-8') as f:
    f.write(texto_traduzido)

print("-" * 30)
print("SUCESSO! Confira o arquivo 'artigo_traduzido.md'")