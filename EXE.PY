texto = input('DIGITE UMA PALAVRA : ').strip(); # strip remove os espaços 
vogais = 'AEIOU'

for letra in texto:
    if letra.upper() in vogais:
        print(f'====================={letra}===================')


print(f'{texto} tem {len(texto)} letras em seu nome')       
