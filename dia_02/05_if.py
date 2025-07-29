#prorgama para receber a idade da pessoa e dizer se pode ou nao beber cerveja
#pela idade
#%%
input = int(input("Qual é a sua idade? "))  # Solicita ao usuário que insira sua idade
idade = input  # Atribui o valor inserido à variável idade

if idade >= 18:
    print("Você pode beber cerveja")    
else:
    print("Você não pode beber cerveja")    

# Aqui nós vemos como é usado o if, que é uma estrutura de controle que permite executar um bloco de código se uma condição for verdadeira
# O else é usado para executar um bloco de código se a condição for falsa
# Também é importante observar que não existe um limite de ifs, ou seja, podemos ter vários ifs dentro de um mesmo programa
# O elif é usado para testar uma segunda condição, caso a primeira não seja verdadeira  