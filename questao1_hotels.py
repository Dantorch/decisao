DIARIA = 60

nome = (input("\nInforme o nome do cliente: "))
dias = int(input("Informe o número de dias: "))

if dias > 15:
  taxa = 5.50
elif dias == 15:
  taxa = 6
else:
  taxa = 8

total = DIARIA*dias + taxa*dias

print(f"\nO nome do cliente é: {nome}.")
print(f"O valor total da conta ficou em: {total}\n")