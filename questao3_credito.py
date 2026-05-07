saldo = float(input("DIGITE SEU SALDO ULTIMO ANO:\n"))
if saldo < 200:
    print("Você não tem nenhum crédito disponivel!")
elif   200 < saldo <= 400:
    print (f"Você tem crédito especial disponivel, seu crédito é {saldo*0.20}")
elif   400 < saldo <= 600:
    print (f"Você tem crédito especial disponivel, seu crédito é {saldo*0.30}")
else :
    print (f"Você tem crédito especial disponivel, seu crédito é {saldo*0.40}") 