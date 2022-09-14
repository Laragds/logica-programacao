#FUP que lê dois valores e escreve cada um juntamente com a mensagem: “É múltiplo de 2” ou “Não é múltiplo de dois”.

numero=int(input('Digite um número qualquer\n'))
numero1=int(input('Digite um número qualquer\n'))

if numero%2==0 and numero1%2==0:
    print(f"Os números {numero} e {numero1} são multiplos de dois.")
elif numero%2!=0 and numero1%2==0: print(f"O número {numero} não é multiplo de dois ja o número: {numero1} é multiplo de dois.")
elif numero%2==0 and numero1%2!=0: print(f"O número {numero1} não é multiplo de dois ja o número: {numero} é multiplo de dois.")
elif numero%2!=0 and numero1%2!=0: print(f"Os números: {numero1} e {numero} não são multiplos de dois.")