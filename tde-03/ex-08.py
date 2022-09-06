#Construa um algoritmo que calcule a quantidade de latas de tintas necessárias e o custo para pintar tanques cilíndricos de combustível, onde são fornecidos a altura e o raio desse cilindro. Sabendo que:
#a lata de tinta custa R$ 150,00;
#cada lata contém 5 litros;
#cada litro de tinta pinta 3 metros quadrados;
#a área do total cilindro é dada por área da base + área lateral;
#a área da base do cilindro é dada π*raio2;
#a área da lateral é 2*π*raio*altura.

"""Total de área a ser pintada"""
altura=float(input('Qual a altura do cilindro de gasolina?\n'))
raio=float(input('Qual o raio da base do cilintro?\n'))

a_base=3.14*(raio*raio)
a_lateral=(2*3.14)*(raio*altura)
a_total=a_base+a_lateral


print(f'A área total do cilindro de gasolina é aproximadamente {round(a_total)}')
"""quanto de tinta é usado"""
area_por_lata=3
preco_por_lata=150
quantas_latas=round(a_total)/area_por_lata
preco_total=quantas_latas*150

print(f"preco_total para pintura do cinlindro é aproximadamente: R${round(preco_total)}")