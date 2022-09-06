#Faça um algoritmo que leia dois números inteiros (x e y), e calcule o quociente e o resto da divisão de x por y e escreva os resultados.

number_int_01=int(input('Digite o número X\n'))
number_int_02=int(input('Digite um número Y\n'))
resto= number_int_01%number_int_02
quociente=number_int_01/number_int_02

print(f'O quociente da equação é:{quociente}.\n O resto da equação é: {resto} ')