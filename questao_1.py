opcao = 'sim'

while opcao == 'sim' or opcao == 'Sim':
	salario = float(input("Digite o salário atual?\n"))
	aumento = float(input("Digite a porcentagem do aumento\n"))

	salario = salario*(100+aumento)/100
	print("Esse é o novo salário", salario)
	opcao = input("Deseja continuar? (Sim/Nao)\n")