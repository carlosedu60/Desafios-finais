  #TODO: Criar as condições para aplicar o cupom de desconto (10% ou 20%).

def main():
    n = int(input("quantidade de pedidos que o usuário deseja inserir  "))
 
    total = 0
 
    for i in range(1, n + 1):
        pedido = input().split(" ")
        nome = pedido[0]
        valor = float(pedido[1])
        total += valor

 
if __name__ == "__main__":
    main()
    
