#Fazer um algoritmo que calcule o número de litros de combustível gastos em uma viagem, sabendo-se que o carro faz 12 km com um litro. Deverão ser lidos o tempo gasto na viagem e a velocidade média. Aplicar as seguintes fórmulas: 
#Distância = tempo gasto x velocidade média
#litros gastos = distância / 12

time_travel=float(input('Quanto tempo durou sua viagem?\n'))
vel_travel=float(input('Qual foi a velociadade média que você usou?\n'))
distance=time_travel*vel_travel
gastos_com_gasolina=distance/12

print(f'Você gastou R${gastos_com_gasolina} em sua viagem.')