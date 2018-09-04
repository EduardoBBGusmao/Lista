import math

raio = float(input("Digite o raio de uma circunferência:\n"))

area = math.pi*raio**2
comprimento = math.pi*2*raio
print("Essa circunferência tem raio: ", raio, "\nDiametro: ", raio*2, "\nÁrea: ", area, "\nComprimento: ", comprimento)
