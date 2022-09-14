#FUP para ler dois números. Se os números forem iguais, imprimir a mensagem: "NÚMEROS IGUAIS" e encerrar a execução; caso contrário, imprimir o de maior valor.

numeroa=int(input('Digite um número qualquer'))
numerobb=int(input('Digite um número qualquer'))

if numeroa==numerobb:
    print("Números iguais")
elif numeroa<numerobb:
    print(numerobb)
else: print(numeroa)

