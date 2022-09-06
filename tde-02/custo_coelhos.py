#8. Uma loja de animais precisa de um algoritmo para calcular os custos de criação de coelhos. 
# O custo é calculado com a fórmula CUSTO=(NRO_COELHOS*0.70)/18+10. 
# O algoritmo tem como entrada o número de coelhos, devendo fornecer, como saída, o custo.


num_rabbit=int(input('Quantos coelhos possuimos em loja nesse momento?\n'))
cust=(num_rabbit*0.70)/18+10
print(f'O custo total com os coelhos será de: {cust}')