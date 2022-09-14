#FUP que leia o número da conta bancária e o saldo de um cliente. Caso a conta tenha saldo negativo, o programa deve enviar a seguinte mensagem: CONTA ESTOURADA, caso contrário CONTA NORMAL.

saldo=float(input("Qual saldo em conta?"))

if saldo<0:
    print("CONTA ESTOURADA")
else: print("CONTA NORMAL")