preco_smartphone = 1000.00
preco_tablet = 1500.00

quantidade_smartphones = int(input("Digite o número de smartphones vendidos: "))
quantidade_tablets = int(input("Digite o número de tablets vendidos: "))

total_arrecadado_smartphones = quantidade_smartphones * preco_smartphone
total_arrecadado_tablets = quantidade_tablets * preco_tablet
total_arrecadado = total_arrecadado_smartphones + total_arrecadado_tablets

print("O total arrecadado com a venda de smartphones é R$", total_arrecadado_smartphones)
print("O total arrecadado com a venda de tablets é R$", total_arrecadado_tablets)
print("O total arrecadado é R$", total_arrecadado)
