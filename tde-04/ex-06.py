#FUP para ler e escrever três números. Se o primeiro for positivo, imprimir sua raiz quadrada, caso contrário, imprimir o seu quadrado; se o segundo número for maior que 10 e menor que 100, imprimir a mensagem: "NÚMERO ESTÁ ENTRE 10 E 100 - INTERVALO PERMITIDO"; se o terceiro número for menor que o segundo, calcular e escrever a diferença entre eles, caso contrário, calcular e escrever a soma entre eles.

import math
no1=float(input("Digite um número\n"))
no2=float(input("Digite outro número\n"))
no3=float(input("Digite outro número\n"))

if no1>=0:
    print(math.sqrt(no1))
else:
    print(f"O quadrado de {no1} é {no1*no2}")

if no2>10 and no2<100:
    print("NÚMERO ESTÁ ENTRE 10 E 100 - INTERVALO PERMITIDO")
else: print("NÚMERO NÃO ESTÁ ENTRE 10 E 100 - INTERVALO NÃO PERMITIDO")
if no3<no2:
    print(f'A diferença entre os números {no1} e {no2} é de: {no2-no3}')
else: print(no2+no3)