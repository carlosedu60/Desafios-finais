#TODO: Criar as condições necessárias para impressão da saída conforme o enunciado.

valorPedido = int(input('Digite o valor do pedido:  '))

print("")
print('*' * 50)

if valorPedido >= 50:
    print('Parabens, você ganhou uma sobremesa gratis!')
else:
    print("Que pena, você nao ganhou nenhum brinde especial.")

print("")    
print('*' * 50)