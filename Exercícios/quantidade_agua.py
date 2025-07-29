# Faça um prorgama que vende uma garrafa de água:  
# Se o cliente escolher aguá mineral natural, será cobrado R$ 1,50
# Mas caso o cliente escolher aguá mineral com gás, será cobrado R$ 2,50

texto = """
Escolha a sua água para comprar
(1) Água mineral natural - preço R$ 1,50
(2) Água mineral com gás - preço R$ 2,50
"""

opcao = input(texto)

valor_item = 0
if opcao == "1":
    valor_item = 1.5
elif opcao == "2":
    valor_item = 2.5

if valor_item == 0:
    print("Entre com a opção correta, por favor.")
else:     
    qtde = input("Quantas garrafas?:")
    qtde = int(qtde)
    valor_total = valor_item * qtde
    print("Sua conta é: R$", valor_total)
