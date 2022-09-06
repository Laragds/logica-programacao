#F.U.A para calcular o valor de lucro que um vendedor tem em um produto, 
# com base em seu preço de custo e o preço de venda.

value_sell=float(input('Qual o valor de venda do produto?\n'))
value_buy=float(input('Qual o valor de compra desse produto?\n'))
profit=value_sell-value_buy
print(f'O lucro sobre esse produto é de: R${profit}')


