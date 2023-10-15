matrix = [   
   #   0      /         1                 /     2       / AQUI SERÁ ACESSADO PELO INDICE 
    [1, 2, 3],['fabricio', 'pauly','sony'],['a','b','c']    
]

print(matrix)
print(matrix[0][2])
print(matrix[1][0])

# fazendo um for com indice  e com enumerate  
carros = ['gol', 'celta', 'uno' ]

for indice, carros in enumerate(carros):
    print(f'{indice}:{carros}')
    
# filtro de lista versão 1

numeros = [2,10,45,87,99,6363,22,13,22,37,45,88]
pares =[]

for numeros in numeros:
    if numeros %2 == 0:
        pares.append(numeros)    
print(pares)   
print('='*50)
# filtro de lista versão 2 (DESTA FORMA ESTA EM LISTCOMPRENSHION)

numeros = [2,10,45,87,99,6363,22,13,22,37,45,88]
pares =[numeros for numeros in numeros if numeros %2 == 0]    

print(pares)



    




    