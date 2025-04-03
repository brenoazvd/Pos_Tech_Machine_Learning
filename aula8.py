import os
# import datetime
# import pyautogui

# pyautogui.press("Win")
# pyautogui.write('chrome')

# print(os.listdir('arquivos'))

# print(datetime.date.today())

lista_arquivos = os.listdir("arquivos")
# os.rename("arquivos/abr22.txt", "arquivos/22/abr22.txt")


# Sempre que você quiser colocar uma váriavel dentro de um texto, você coloca o f antes do texto
for arquivo in lista_arquivos:
    if ".txt" in arquivo:
        if "22" in arquivo:
            os.rename(f"arquivos/{arquivo}", f"arquivos/22/{arquivo}")
            print("Movimentar para a pasta 22", arquivo)
        elif "23" in arquivo:
            os.rename(f"arquivos/{arquivo}", f"arquivos/23/{arquivo}")
            print("Movimentar para a pasta 23", arquivo)