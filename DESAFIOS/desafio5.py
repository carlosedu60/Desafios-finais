#TODO: Tendo em vista a variável booleana "ehVegano", imprima a saída deste desafio.

numPedidos = int(input("número de pedidos que o usuário deseja fazer:  "))

for i in range(1, numPedidos + 1):
    prato = input("nome do prato:  ")
    calorias = int(input("quantidade de calorias do prato:  "))
    ehVegano = False
    