#FUP que leia um número e mostre uma mensagem indicando se este número é par ou ímpar e se é positivo ou negativo.

numero=int(input('Digite um número qualquer\n'))

if numero%2==0:
    print("Este número é par")
else: print("Este número é impar")

if numero>0:
    print("Este número é positivo")
else: print("Este número é negativo")
