#Faça um algoritmo que calcule e escreva o preço final 
#de um computador, sendo fornecido o preço de fábrica. 
#O preço final do computador é calculado com base nos adicionais de: 30 % de imposto
# e 10 % de revenda sobre o preço de fábrica. 

price_i=int (input('Qual o preço de fábrico do computador?\n'))
price_f=(price_i + (price_i*0.3) + (price_i * 0.1))
print(f'O final do computador, com os impostos fornecidos é de: {price_f}')
