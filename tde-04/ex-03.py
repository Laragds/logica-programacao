#FUP para ler dois valores numéricos e apresentar a diferença do maior pelo menor. 

n1=float(input("Digite um número\n"))
n2=float(input("Digite outro número\n"))

if n1>n2:
    diferenca=n1-n2
else: diferenca=n2-n1
print(diferenca)