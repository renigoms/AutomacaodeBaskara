
lista_estados_abranger = ["mt","wa", "or","id", "nv", "ut","ca", "az"]
estacoes = {
    "kum" : {"id", "nv", "ut"},
    "kdois" : {"wa", "id", "mt"},
    "ktres": {"or", "mv", "ca"},
    "kquatro": {"nv", "ut"},
    "kcinco": {"ca", "az"}
}
def algoritmoGulosso(lista:list, dicionario_com_estacoees:dict):
    estados_abranger =  set(lista)
    estacoes_final = set()
    while estados_abranger:
        melhor_estacao = None
        estados_cobertos = set()

        for estacao, estados_por_estacao in estacoes.items():
            cobertos = estados_abranger & estados_por_estacao
            if len(cobertos) > len(estados_cobertos):
                melhor_estacao = estacao
                estados_cobertos = cobertos

        estados_abranger -= estados_cobertos
        estacoes_final.add(melhor_estacao)
    print(estacoes_final)
algoritmoGulosso(lista_estados_abranger, estacoes)
