#Faça um algoritmo que leia três números inteiros e calcule a sua média. 
# Ao final, o algoritmo deve escrever os números lidos e o resultado da média.

number_01=int (input('Escreva qualquer número inteiro:\n'))
number_02=int (input('Escreva qualquer número inteiro:\n'))
number_03=int (input('Escreva qualquer número inteiro:\n'))

soma= number_01 + number_02 + number_03
media= soma/3

print(f'O primeiro número escolhido foi:{number_01}\n O segundo número escolhido foi:{number_02}\n O terceiro número escolhido foi: {number_03}\n A média dos números que foram informados anteriomente foi de: {media}')