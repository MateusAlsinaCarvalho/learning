#selecionando uma palavra e apertando CTRL + D você consegue selecionar várias linhas
#enquanto a condição for verdadeira, o laço será executado
#while espera respostas logicas, ou seja, True ou False ou booleano

#%%
numero = 2 
count = 1 

while count <= 100:                    #enquanto count for menor ou igual a 100 o laço será executado  
    print (numero, "x", count, "=", numero * count)  #imprime a tabuada do número 2
    count += 1                         #incrementa o valor de count em 1 a cada iteração do laço
                                       #count = count + 1  #outra forma de incrementar o valor de count                       

print ("Acabou!!") 


# Este código gera a tabuada do número 2 até o 100 usando um laço while.
# O laço while executa o bloco de código repetidamente enquanto a condição (count <= 100) for verdadeira.
# A cada repetição, o valor de count é incrementado em 1, e o resultado da multiplicação é exibido.
# Quando count passa de 100, a condição se torna falsa e o laço é encerrado.
# O while é útil quando não sabemos exatamente quantas vezes o bloco será executado, apenas que depende de uma condição lógica.