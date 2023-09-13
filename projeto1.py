import pyautogui, time
import keyboard
import win32api, win32con

enviar_email = True

while enviar_email:
    entradadoemail = input("Por favor, coloque o email para o qual deseja enviar: ")
    print("Quando terminar, escreva 'pronto'. Será enviado para este email:", entradadoemail)
    mensagem_email = input("Qual o assunto você deseja enviar?: ")
    texto_email = input("Qual o texto você deseja enviar?: ")
    pronto = input("Digite 'pronto' : ")

    if pronto == "pronto":
        print("Abrindo... Não toque em nada até o processo terminar!!!")
        time.sleep(3)
        pyautogui.hotkey('win')
        time.sleep(0.5)
        pyautogui.typewrite("edge")  # Abrir o navegador
        time.sleep(1.5)
        pyautogui.hotkey('enter')
        time.sleep(1.5)
        pyautogui.hotkey('ctrl', 't')  # Abrir nova aba
        time.sleep(2)
        pyautogui.typewrite('https://mail.google.com/mail/u/0/#inbox')  # Abrir o Gmail
        pyautogui.hotkey('enter')
        time.sleep(2)  # Aguarde o Gmail carregar
        # Função para clicar no botão "Escrever" no Gmail
        def clicar_escrever():
            # Encontre a posição do ícone de "Escrever" no Gmail usando coordenadas
            pos = pyautogui.locateOnScreen('botao_escrever.png', confidence=0.7) 
            if pos:
                # Calcule o centro do ícone de "Escrever"
                centro_x, centro_y = pyautogui.center(pos)
                pyautogui.click(centro_x, centro_y)
                return True
            else:
                print("Não foi possível encontrar o botão 'Escrever'.")
                return False

        if clicar_escrever():
            # Escrever o email
            time.sleep(0.5)
            pyautogui.typewrite(entradadoemail)
            time.sleep(0.5)
            time.sleep(1)
            time.sleep(1)
            pyautogui.typewrite(entradadoemail)
            pyautogui.hotkey('tab')
            pyautogui.typewrite(mensagem_email)
            pyautogui.hotkey('tab')
            pyautogui.typewrite(texto_email)
    # pedir para enviar mais
    resposta = input("Deseja enviar outro email? (s/n): ")
    if resposta.lower() != "s":
        enviar_email = False
