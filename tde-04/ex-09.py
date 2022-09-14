#FUP para ler três valores quaisquer e escrever o maior dos 3.

no1=float(input("Digite um número\n"))
no2=float(input("Digite outro número\n"))
no3=float(input("Digite outro número\n"))

if no1>no2 and no1>no3:
    print(no1)
elif no2>no1 and no2>no3:
    print(no2)
elif no3>no1 and no3>no2:
    print(no3)