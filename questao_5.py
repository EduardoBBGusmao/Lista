CigarrosPorDia = int(input("Digite quantos cigarros por dia o fumante fuma: \n"))
Anosfumados = float(input("Digite há quantos anos o fumante fuma: \n"))

TotalDeCigarros = CigarrosPorDia*(Anosfumados*365)
DiasPerdidos = int(TotalDeCigarros*10/60)

print("Esse fumante já perdeu: ", DiasPerdidos, " dias.")