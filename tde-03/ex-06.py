#Faça um algoritmo que leia 3 números inteiros e:
#Escreve o produto (multiplicação) destes números;
#Escreva a soma destes números;
#Escreve a subtração destes números;
#Escreve a soma de todos os resultados acima.

number_one=float(input('Digite qualquer número aleatório\n'))
number_two=float(input('Digite qualquer número novamente\n'))
number_three=float(input('Digite qualquer número novamente\n'))
multiplicacao=number_one*number_two*number_three
soma=number_one+number_two+number_three
subtracao=number_one-number_two-number_three
allIn=multiplicacao+soma+subtracao
print(f'O produto da multiplicação é: {multiplicacao}\nO resultado da Soma dos números é: {soma}\nA subtração é: {subtracao}\nA soma dos resultados é:{allIn}')