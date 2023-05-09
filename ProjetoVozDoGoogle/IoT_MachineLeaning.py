import speech_recognition as ia
import os


# Função para ouvir e reconhecer a fala
def ouvir_microfone():
    # Habilita o microfone do usuário
    microfone = ia.Recognizer()
    # Usando o microfone
    with ia.Microphone() as sourse:
        # chama um algoritmo de redução de ruídos
        microfone.adjust_for_ambient_noise(sourse)
        # Frase para que o usuário entenda que nesse momento ele preceisa dizer algo
        print('Diga alguma coisa: ')
        # Armazenamento do que foi dito
        audio = microfone.listen(sourse)
    try:
        # passa a variável para o algoritmo reconhecedor de padrõees
        frase = microfone.recognize_google(audio, language='pt-BR')
        if 'navegador' in frase:
            os.system('start Chrome.exe')
        elif 'escrever' in frase:
            os.system('start WINWORD.EXE')
        elif 'Excel' in frase:
            os.system('start Excel.exe')

        print(f'VOCÊ DISSE: {frase}')  # Exibe a frase dita
    # Se não reconhexeu o padrão de fala exibi a mensagem
    except ia.UnknownValueError:
        print('Não entendi')

    # return frase


ouvir_microfone()
