#%%

# Prática simples usando usando while e if para testar a lógica dos operadores do python

while True :
    print("""
        Bem-vindo ao teste de temperatura.
        """)
    print("Para encerar o programa digite 0")
    temperatura = (input("Digite a temperatura do seu PC : "))
    temperatura = int(temperatura)

    if temperatura == 0:
        break
    elif temperatura <= 70:
        print("Status OK: Resfriamento funcionando bem.")
    elif temperatura >= 71 and temperatura <= 85:
        print("Atenção: O sistema está aquecendo.")
    elif temperatura > 85:
        print("PERIGO: Temperatura crítica! Reduzindo desempenho para evitar danos.")
