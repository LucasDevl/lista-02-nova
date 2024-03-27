preco_camiseta = 25.00
preco_calca = 100.00
preco_cinto = 40.00

num_camisetas = int(input("Digite o número de camisetas compradas: "))
num_calcas = int(input("Digite o número de calças compradas: "))
num_cintos = int(input("Digite o número de cintos comprados: "))

valor_total = (num_camisetas * preco_camiseta) + (num_calcas * preco_calca) + (num_cintos * preco_cinto)

desconto = valor_total * 0.10

valor_com_desconto = valor_total - desconto

print("O valor do desconto é: R$", desconto)
print("O valor da compra com desconto é: R$", valor_com_desconto)
