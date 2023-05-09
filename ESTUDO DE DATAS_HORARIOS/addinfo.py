import ProgetoControler
import datetime

diciodatas = {}


def datas():
    ano = 2022
    mes = int(input('DIGITE O MÊS(em número de um algarismo) >>>'))
    dia = int(input('DIGITE O DIA>>>'))
    data1 = datetime.datetime(ano, mes, dia)
    a = str(data1.day) + '/' + str(data1.month) + '/' + str(data1.year)
    return a


def cadastro():
    diciodatas = ProgetoControler.lerarqjson()
    while True:
        print('-'*29)
        print('-'*8, 'MENU TEST', '-'*10)
        nome = input('DIGITE O NOME>>>')
        rota = input('DIGITE A ROTA DA VIAGEM>>>')
        data = datas()
        print('-' * 29)
        diciodatas[nome] = {
            'nome': nome,
            'rota': rota,
            'data': data
        }
        print(diciodatas)
        ProgetoControler.gravardados(diciodatas, 3)
        op = input('quer continuar s-sim ou n-não?').lower()
        if op == 'n':
            break





