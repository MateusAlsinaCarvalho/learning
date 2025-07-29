#Faça um programa que receba uma quantidade indefinida de valores
#correspondentes a "saldo em conta", mas quando o usuario apertar 
#"enter" sem digitar valor algum, o programa para de receber valores
#e exibe a soma de todos os valores digitados anteriormente.

saldo_total = 0 
while True: 
    saldo = input("Entre com o saldo: ")
    if saldo == "":               # Se o usuário apertar enter sem digitar nada, sai do laço
        break                     #o break só pode ser usado dentro de laços de repetição 
                                  #o break interrompe o primeiro laço onde ele se encontra 

    saldo_total += float(saldo)

print ("Saldo total: ", saldo_total) #o break irá pular diretamente para fora do laço, sem testar as outras
                                     #linhas do laço, e irá executar o print final
