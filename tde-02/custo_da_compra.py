#10.F.U.A que leia o preço de um produto e a quantidade comprada
# e exiba para o usuário o preço que ele tem que pagar pela compra.

valor_produto=int(input('Digite o preço do seu produto '))
quantidade_comprada=int(input('Qual o valor desse produto? '))
preco_a_pagar=quantidade_comprada * valor_produto
print(f'Você precisa pagar ao caixa {preco_a_pagar}')
