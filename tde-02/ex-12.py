#F.U.A que leia dois números e calcule qual é o valor inteiro da divisão do 2o pelo 1o número. 
# Exiba na tela este valor final.

valor_01=int(input("Digite um número inteiro"))
valor_02=int(input("Digite novamente um número inteiro"))
divisao=round(valor_01%valor_02)
print(f'O resto da divisão é: {divisao}')