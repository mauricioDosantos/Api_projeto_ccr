Sejam Bem Vindos ao Projeto API CCR
===================================
Dependências de desenvolviemto:

* Python 3.8.5
* Django 3.1.5
* Django rest framework 3.12.2
* Ibm cloud sdk core 3.3.6
* Ibm watson 5.1.0

Descrição do projeto
===================================
Este protótipo de API tem a funcionalidade de retornar uma das seguintes personalidades: butarão, gato, águia, lobo, misto, decisão tomada com base no retorno da inteligência Natural Language Understanding da IBM. As informações recebidas pela API são no formato
JSON e enviadas no formato JSON. Protótipo compara caracteristicas pré-definidas das personalidade.

Utilização
===========================
Modo de uso da API.

* CURL 

Com o comando estruturado da seguinte maneira:

    $ curl -X POST -H 'Content-Type: application/json'
    --data '{"text":"<neste local adicione o seu texto>"}'
     https://api-projeto-ccr.herokuapp.com/v1/api
