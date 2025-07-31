#as listas são um conjunto de elementos 
#sempre dentro das listas usando colchetes
#uma das maneiras de definir listas:
#uma coisa importante sobre listas: listas no python não são arrays
#em python podemos ter listas de absolutamente qualquer tipo de elementos
#e esses elementos não precisam ser do mesmo tipo.
#As listas são análogas a um molho de chaves

#%%
idades = [28, 42, 43, 35, 39, 28, 38]
print(idades)


#%%
mateus = ["Mateus", "Alsina", 26, False, "Solteiro", 1800.50]
print(mateus) 


#%% 
type(mateus)

#%%
#para acessar as posições dentro da lista fazemos:
#para apontar um elemento de uma lista eu preciso apontar o indice 
#desse elemento. Os elementos dentro de uma lista começam no zero.

#nome do elemento
print(mateus[0])

#idade do Mateus 
print(mateus[2])

#estado civil do Mateus
print(mateus[4])

#%%

idades = [20, 89, 34, 89, 26, 19, 90, 42]

print("Soma das idades: ", sum(idades))

print("Quantidade de idades: ", len(idades))

print("Média das idades: ", sum(idades)/len(idades))

#ao realizar um hardcoding, ou seja, quando codamos de forma mais 
#rustica ou sem usar tantas ferramentas, algo como utilizar "sum(idades)/9"
#ao inves de utilizarmos o len, isso pode causar bugs, que não necessariamente quebram
#o código causando um erro, mas pode apontar conclusões erradas.
#Se por exemplo, esquecermos de atualizar o numero "9" quando inserimos
#um elemento a mais na lista, a média será exibida de forma erronea. Isso 
#não irá causar um erro, mas o programa funcionará de uma forma que não era a esperada
#Não é uma regra, mas utilizar menos códigos "chumbados" ou menos hardcoding pode te 
#fazer um programador melhor.

print("Menor idade: ", min(idades)) 

print("Maior idade: ", max(idades))

#%%

mateus = ["Mateus Alsina", 26, 
          True, "Solteiro", 
          1800.50, 
          ["gerente", "marketing", "cientista de dados"]]

print("tamanho de mateus: ", len(mateus))

print("ultimo emprego do Mateus: ", mateus[5][0])

emprego = mateus[5]
primeiro_emprego = emprego[0]
print(primeiro_emprego)



#consigo criar uma lista dentro da outra, e para acessar os seus elementos eu utilizo da forma
#exemplificada acima. 

#%%

tamanho = len(mateus)
pos = tamanho - 1 
mateus(pos) 
