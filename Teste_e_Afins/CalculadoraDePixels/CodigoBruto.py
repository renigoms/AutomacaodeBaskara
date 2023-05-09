def calculadora_de_pixels(altura_cm_=0, largura_cm_=0):
    pixelsDeAltura = altura_cm_ // 0.0254
    pixelsDeLargura = largura_cm_ // 0.0254
    print(f"A altura e a largura em pixels são respectivamente: {pixelsDeAltura} e {pixelsDeLargura} ")


def somarecusiva(num1=0, num2=0):
    try:
        num1 = int(input("Digite um número"))
        soma = num1 + num2
        opcao = input("")
        if opcao == "=":
            print(f"soma total: {soma}")
        elif opcao == "+":
            return somarecusiva(num1, soma)
        else:
            print("você deve digitar + ou = para continuar")
            return somarecusiva()
    except:
        print("ocorreu um erro")
        return somarecusiva()

