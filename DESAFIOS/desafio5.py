#TODO: Tendo em vista a variável booleana "ehVegano", imprima a saída deste desafio.

numPedidos = int(input("número de pedidos que o usuário deseja fazer:  "))
frases = []


for i in range(1, numPedidos + 1):
    prato = input("nome do prato:  ")
    calorias = int(input("quantidade de calorias do prato:  "))
    ehVegano = input("DIGITE SE É VEGANO OU NÃO:  ")
    if ehVegano == "s":
        frases.append(f"Pedido {i}: {prato} - (Vegano) - {calorias}")
    else:
        frases.append(f"Pedido {i}: {prato} - (Não - Vegano) - com {calorias} calorias.")
        
for frase in frases:
    print(frase)        

    