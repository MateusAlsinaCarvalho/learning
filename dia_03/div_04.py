

#%%

#Quais numeros são divisiveis por 4 no intervalo de 4 a 100?

count = 4 
while count <= 100:    
    resto = count % 4  #calcula o resto da divisão de count por 4
    if resto == 0:      #se o resto for igual a 0, significa que count é divisível por 4
        print(count)    #imprime o valor de count, pois é divisível por 4
    count += 1         #incrementa o valor de count em 1 a cada iteração do laço


#%%
#aqui faremos o mesmo programa mas utilizando o for 

for numero in range(4, 101):
    if numero % 4 == 0:
        print(numero)


#O while utilizamos para comparações lógicas, repetidos por uma condição lógica
#O for usamos para percorrer os elementos de um objeto, seja uma string ou uma sequencia 
#normalmente usamos o While quando não sabemos quantas vezes iremos repetir, o for sabemos 
#qual objeto queremos percorrer. 