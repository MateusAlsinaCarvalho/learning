# Faça um programa que receba 4 alturas usando um laço
# de repetição e realize a soma dessas alturas.

#%%
soma = 0 # valor final 
qtde_entradas = 4 # contador de entradas

while qtde_entradas > 0: 
    altura = input("Entre com a altura:") 
    altura = float(altura)                     #float converte string para número decimal 
    soma += altura 
    qtde_entradas -= 1  

print("Soma das alturas:", soma)


#%% Explicação 
# Faça um programa que receba 4 alturas usando um laço
# de repetição e realize a soma dessas alturas.

soma = 0 # valor final 
# Aqui criamos uma variável chamada 'soma' e começamos ela com zero. Ela vai guardar o total das alturas.

qtde_entradas = 4 # contador de entradas
# Esta variável controla quantas vezes vamos pedir uma altura. Começa com 4 porque queremos 4 alturas.

while qtde_entradas > 0: 
    # O laço 'while' repete o bloco abaixo enquanto qtde_entradas for maior que zero.
    altura = input("Entre com a altura:") 
    # Aqui pedimos para o usuário digitar uma altura. O valor vem como texto (string).
    altura = float(altura) 
    # Convertendo o texto para número decimal (float), para poder somar.
    soma += altura 
    # Adicionamos a altura digitada ao total (soma).
    qtde_entradas -= 1  
    # Diminuímos 1 do contador. Assim, depois de 4 repetições, o laço termina.

print("Soma das alturas:", soma)
# Mostramos o resultado final da soma das alturas digitadas.