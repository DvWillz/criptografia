from functions.main import *

while True:
    print("=-"*20)
    print("Criptografia de texo\n[1] Criptografar\n[2] Descriptografar\n[3] Fechar o programa")
    op = int(input("Opção: "))
    if op == 1:
        criptografar = cripto(str(input("Digite o texto para ser criptografado: ")))
        print(f'Texto criptografado: {criptografar}')
    elif op == 2:
        descriptografado = descripto(str(input("Digite o texto para ser descriptografado: ")))
        print(f'Texto descriptografado: {descriptografado}')
    else:
        break
