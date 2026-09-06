

print("\n=== Bem-vindo ao Senna Game ===\nEscolha uma opção para continuar:\n")

while True:
    print("Digite 1 para ver a biografia")
    print("Digite 2 para jogar o game")
    print("Digite 3 para fechar o programa")
    escolha = int(input("Digite um numero : "))
    match escolha:
        case 1 :
            print("\n--- Biografia de Ayrton Senna ---\nAyrton Senna foi um piloto brasileiro de Fórmula 1, três vezes campeão mundial (1988, 1990, 1991). Conhecido por sua velocidade, determinação e carisma, ele permanece como um ícone do esporte.\n")
        case 2 :
            print("===Quiz do Ayrton Senna===")
            pontos = 0
            # Pergunta 1
            print("Em que ano o Senna faleceu?")
            print("A) 1994")
            print("B) 1992")
            print("C) 1981")
            print("D) 1982")
            escolha = input("escolha uma opção : ").strip().upper()
            if escolha == "A":
                pontos += 1
            # Pergunta 2
            print("\nQual era a nacionalidade de Senna?")
            print("A) Brasileiro")
            print("B) Argentino")
            print("C) Português")
            print("D) Italiano")
            escolha = input("escolha uma opção : ").strip().upper()
            if escolha == "A":
                pontos += 1
            # Pergunta 3
            print("\nQuantas vezes Senna venceu o Campeonato Mundial de Fórmula 1?")
            print("A) 3")
            print("B) 2")
            print("C) 1")
            print("D) 4")
            escolha = input("escolha uma opção : ").strip().upper()
            if escolha == "A":
                pontos += 1
            print(f"Você fez {pontos} ponto(s) no quiz.")
        case 3 :
            break
        case _ :
            print("digite a opçao correta")