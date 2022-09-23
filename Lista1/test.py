c = []

for i in range(0,6):
    puts = input('Insira o nome da %d cidade: ' % (i + 1))
    
    while True:
        if puts in c:
            puts = input('Esse nome já está na lista. Insira o nome de outra cidade: ')
            break
        else:
            continue
        
    c.append(puts)
    answer = input('Deseja estender o nome da cidade?(s/n)')
    
    if answer in ('S', 's'):
        extra = input('Insira a extensão do nome: ')
        c[i] = c[i] + extra
        print(c[i])
        
print('Os nomes das cidades inseridas são: ', *c)
longest = max(c,key=len)
print(longest,'é o nome de cidade mais extenso!')