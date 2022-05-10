idade = int(input('QUANTOS ANOS VOCÊ TEM ?'))
mes = int(input('QUANTOS MESES PASSARAM DESDE DO DIA QUE VOCÊ FEZ ANIVESARIO?'))
dias = int(input('QUANTOS DIAS PASSOU DESDE DO DIA QUE SERIA SEU ANIVESARIO NO MES DO SEU ANIVESARIO?'))
totaldias = (idade*360) + (mes*30) + idade
print(f'Sua idade é: {totaldias} dias')


