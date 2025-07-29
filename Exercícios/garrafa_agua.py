# Faça um prorgama que vende uma garrafa de água:  
# Se o cliente escolher aguá mineral natural, será cobrado R$ 1,50
# Mas caso o cliente escolher aguá mineral com gás, será cobrado R$ 2,50

escolha = input("Você deseja água natural ou com gás? Digite 'natural' ou 'com gás':")
escolha = escolha.lower().strip()  # Converte a entrada para minúsculas para evitar

if escolha == "natural":
    print("Você escolheu água mineral natural. O preço é R$ 1,50.")
    print("Obrigado pela compra!") 
    
    
elif escolha == "com gás" or escolha == "com gas": 
    print("Você escolheu água mineral com gás. O preço é R$ 2,50.")
    print("Obrigado pela compra!")

else: 
    print("Opção inválida. Por favor, escolha 'natural' ou 'com gás'.") 
    print("Tente novamente!")
