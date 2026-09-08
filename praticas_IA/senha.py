


senha = "Brasil123"
contador = 0
limite = 3

while contador <= limite :
    digitar = input("digite sua senha :")
    if digitar == senha :
        print("Senha correta!")
        break
    elif digitar != senha :
        print("senha errada!")
        contador += 1
    if contador == limite :
        print("Sistema bloqueado")
        break