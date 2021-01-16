from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
import json
# imports IBM Watson
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions


def percorrer_dic_lis(lis, item):
    for value in lis:
        if value == item:
            return True
    return False


@api_view(('POST',))
@renderer_classes((JSONRenderer,))
def api_watson(request):
    # autenticação do serviço Watson Natural Language Understanding
    authenticator = IAMAuthenticator('a7YxRsMTVsi6aw1UCoV2WSrAkfT49936C6iJ1j-kw1KC')
    natural_language_understanding = NaturalLanguageUnderstandingV1(
        version='2020-08-01',
        authenticator=authenticator
    )

    natural_language_understanding.set_service_url(
        'https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/instances/5d23d705-15d0-4159-b398-9bf7a8472d53')

    # checa se a requisição é de método POST
    if request.method == "POST":
        list = dict(request.data).get(' name')
        text = list[0][11:-47]

        # manda os dados para o serviço da IBM Watson e recebe um JSON
        response = natural_language_understanding.analyze(text=text,
        features=Features(entities=EntitiesOptions(emotion=True, sentiment=True, limit=6),
                          keywords=KeywordsOptions(emotion=True, sentiment=True, limit=6))).get_result()
        resp = json.dumps(response)  # devido a erros, converte para um objeto JSON do módulo json do Python
        resp = json.loads(resp)  #  transforma em dicts
        list_the_dic = resp.get('keywords')  # pega as palavras-chave
        texts = [dic.get('text') for dic in list_the_dic]  # transforma em uma lista

        """
            lista de caracteristicas de cada personalidade,
            link da fonte:
            https://www.ibccoaching.com.br/portal/comportamento/analise-comportamento-teste-perfil-comportamental/
        """
        tubarao = ['focado em resultados', 'determinado', 'objetivo', 'superar desafios', 'força', 'ação']
        gato = ['amoroso', 'brincalhão', 'carinhoso', 'acolhedor', 'ajudar os outros', 'companheiro', 'recepitiva', 'fácil comunicação','comunicação']
        aguia = ['visionário', 'criativo', 'futurista', 'idealizador']
        lobo = ['observador', 'trabalho em grupo', 'metódica', 'organizado', 'estratégico', 'planos', 'organização']
        list_feat = [tubarao, gato, aguia, lobo]

        ponto_tubarao = 0
        ponto_gato = 0
        ponto_aguia = 0
        ponto_lobo = 0
        # compara a lista de valores restornados pela IA com a lista de caracteristicas de cada personalidade.
        for index, lista in enumerate(list_feat):
            for item in lista:
                result = percorrer_dic_lis(texts, item)
                if result:
                    if index == 0:
                        ponto_tubarao += 1
                    elif index == 1:
                        ponto_gato += 1
                    elif index == 2:
                        ponto_aguia += 1
                    elif index == 3:
                        ponto_lobo += 1

        # checa qual resultado irá retornar para a aplicação, assim definindo a personalidade.
        if ponto_tubarao == ponto_gato and ponto_tubarao == ponto_aguia and ponto_tubarao == ponto_lobo:
            resultado = 'misto'
        elif ponto_tubarao > ponto_gato and ponto_tubarao > ponto_aguia and ponto_tubarao > ponto_lobo:
            resultado = 'tubarao'
        elif ponto_gato > ponto_aguia and ponto_gato > ponto_lobo:
            resultado = 'gato'
        elif ponto_aguia > ponto_lobo:
            resultado = 'aguia'
        else:
            resultado = 'lobo'

        return Response({'tipo': f'{resultado}'})  # response
    else:
        return Response({'response': 'is not method POST'})