# AULA DE CONJUNTOS  // MUDANDO CONJUNTO PARA LISTA 

lista_1 = [1,2,3,4,4,5,5,6,7,8,8,9,10]

print(lista_1)
print('='*50)
# NESTE CASO DEMOS UM SET E ELIMINAMOS OS REPETIDOS 
lista_1 = set(lista_1)
print(lista_1) # JA FOI EXIBIDO UM CONJUNTO 
# NÃO CONSEGUIMOS EXTRAIR ELEMENTO DE UM CONJUNTO ENTÃO TEMOS QUE TORNA-LO UMA LISTA
print('='*50)
lista_1 = list(lista_1) # AQUI O CONJUNTO JA VIROU UMA LISTA NOVAMENTE 
print(lista_1[2]) # AQUI ACESSAMOS O INDICE DA LISTA INDICADO