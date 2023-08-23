valorHamburguer = float(input('Digite o valor do hamburguer:   '))
quantidadeHamburguer = int(input('Digite a quantidade de hamburguer:   '))
valorBebida = float(input('Digite o valor da bebida:   '))
quantidadeBebida = int(input('Digite a quantidade de bebida:   '))
valorPago = float(input('Digite o valor pago:   '))

totaldoshamburguers = (valorHamburguer * quantidadeHamburguer)
totaldasbebidas = (valorBebida * quantidadeBebida)
precoTotalPedido = (totaldoshamburguers + totaldasbebidas)
trocoNecessario = (valorPago - precoTotalPedido)

print('')
print('*' * 50)
print(f'O preço final do pedido é de R${precoTotalPedido:.2f}\nSeu troco é R${trocoNecessario:.2f}\n')
print('*' * 50)




   
