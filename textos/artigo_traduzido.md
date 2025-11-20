# Tradução do Artigo

Modelos GPT estão hospedados em múltiplos fornecedores de serviços no momento, e o Microsoft Azure é um deles.
Embora os modelos em si sejam os mesmos, existem muitas diferenças, incluindo:
custar
Funcionalidades
Tipo de Modelos e Versões
Geolocalização
segurança
apoio
etc.
Um dos aspectos mais importantes quando o utilizamos em um ambiente corporativo é, claro, a segurança.
Ao usar recursos de segurança de rede do Azure com o Azure Open AI, os clientes podem consumir o serviço Open AI a partir e dentro do VNet, portanto nenhuma informação está circulando em público.
Implantação de Exemplos
O repositório Azure Sample fornece um arquivo bicep de exemplo para implantar o Azure Open AI no ambiente VNet.
GitHub: openai-enterprise-iac
As principais características que o bíceps utiliza são:
VNet
Integração com VNet para Web App
Private Endpoint for Azure Open AI
Endpoint Privado para Busca Cognitiva
Zona DNS Privada
Ao usar esses recursos, todo o tráfego de saída do Web App só foi roteado dentro do VNet e todos os nomes são resolvidos em endereços IP privados. A Open AI e a Busca Cognitiva desligavam o endereço IP público, portanto não há mais endpoints de interface pública disponíveis.
Implantar
O arquivo bicep será implantado após o Azure Resources.
Vamos implantar e confirmar como funciona. Criei um grupo de recursos na região Leste dos EUA para meu próprio teste.
Clone do Git https://github.com/Azure-Samples/openai-enterprise-iac
CD
OpenAI-Enterprise-IAC
az group create
-n
openaitest
-L
eastus
AZ Deployment Group Create
-g
openaitest
-f
.
\eu
NFRA
\m
ain.bíceps
Entrar no modo tela cheia
Sair do modo tela cheia
Depois que executo a recomendação acima, vejo que a implantação começou.
Espere até o desdobramento terminar.
Teste
Vamos ver se o lançamento foi bem sucedido.
Azure Open AI
Vamos tentar o acesso público primeiro.
Eu poderia criar uma implantação sem nenhum problema. Mas quando tento pelo Chat Playground no meu Azure Portal, vejo o seguinte erro.
E quanto ao acesso via Web API?
A partir de uma ferramenta avançada do App Service, eu faço login no Bash session e primeiro faço ping na URL do serviço.
Vejo que o endereço IP privado atribuído ao Endpoint Privado está returend.
Depois, uso o comando curl para enviar a requisição ao endpoint.