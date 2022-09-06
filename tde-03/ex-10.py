#Elabore um algoritmo para calcular e escrever o preço final de um computador, sendo fornecido o preço de fábrica. O preço final do computador é calculado com base nos adicionais 45 % de imposto e 28 % de revenda sobre o preço de fábrica.

pc_inc=int (input('Qual o valor de fábrica do computador?\n'))
pc_fnl=pc_inc + (pc_inc*0.45)+ (pc_inc*0.28)
print(f'O valor final do computador ficará no valor de R${pc_fnl}')