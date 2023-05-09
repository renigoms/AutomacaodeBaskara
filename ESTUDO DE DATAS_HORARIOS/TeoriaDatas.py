# IMPORTAR ESSA BIBLIOTECA(ELA JÁ VEM IMBUTIDA)
import datetime
# MOSTRAR DATA E HORA ATUAIS
data = datetime.datetime.now()
print(data)
print(data.strftime('%I'))
# CONTRUINDO UMA DATA :
print(str(data.day) + '/' + str(data.month) + '/' + str(data.year))# AS VRIÁVEIS DEVEM SER TRANSFOMADAS EM STRINGS
# DATA EDITAVEL:
nasc = datetime.datetime(2003, 2, 4, 20, 5, 40)# AQUI A NOÇÃO DE DIA,MÊS E ANO É OPOSTA.
                        # ano , mês, dia, hora, minuto , segundo
print(nasc)
a=2003
m=2
d=4
nasc = datetime.datetime(a, m, d)# AQUI A NOÇÃO DE DIA,MÊS E ANO É OPOSTA.
#print(nasc)# da para usar com variável.
print(nasc.strftime('%A'))# Retorna o dia da semana
# %A -> retorna dia da semana com a função strftime()
'''
strftime('%...')
ANO,MÊS E DIA
%A-> DIA DA SEMANA
%a->DIA DA SEMANA ABREVIADO
%w->NUM.DIA DA SEMANA
%d->NUM.DIA DO MÊS
%B-> RETORNA O MÊS
%b-> RETORNA O MÊS ABREVIADO
%m-> NUM DO MÊS
%Y-> ANO INTEIRO(QUATRO DIGITOS)
%y-> ANO PELA METADE(DOIS DIGITOS)
%j-> DIA DO ANO 365
%W-> 
'''
print(nasc.strftime('%H'))
'''
strftime('%...')
HORA
%H-> HORA DE 00-23
%I-> HORA DE 00-12
%S-> segundos
%f-> microsegundos
'''