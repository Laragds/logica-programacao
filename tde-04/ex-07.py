#FUP para ler dois valores: NUM1 e NUM2, e se NUM1 for maior que NUM2 executa a soma de NUM1 e NUM2; caso contrário, executa uma subtração.

NUM1=float(input("Digite um número\n"))
NUM2=float(input("Digite um número\n"))

if NUM1>NUM2:
    print(f'A SOMA dos números {NUM1} e {NUM2} é: {NUM1+NUM2}')
else: print(f'A SUBTRAÇÃO dos números {NUM1} e {NUM2} é: {NUM1-NUM2}')