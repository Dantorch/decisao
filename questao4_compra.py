
valor_compra = float(input('Informe o valor da compra: '))
valor_pago = float(input('Informe o valor pago: '))
troco = valor_pago - valor_compra
if troco < 0:
    print('Valor pago é menor que o valor da compra. Por favor, informe um valor válido.')
else:
    notas_100 = int(troco / 100)
    troco -= notas_100 * 100
    notas_10 = int(troco / 10)
    troco -= notas_10 * 10
    notas_1 = int(troco)
    print(f'Valor da compra: R$ {valor_compra:.2f}')
    print(f'Valor do troco: R$ {valor_pago - valor_compra:.2f}')
    print(f'Quantidade de notas de 100: {notas_100}')
    print(f'Quantidade de notas de 10: {notas_10}')
    print(f'Quantidade de notas de 1: {notas_1}')