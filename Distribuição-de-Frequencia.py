valores = []
resp = ''
while resp not in 'Nn' or 'Ss':
    perg = str(input('Deseja colocar um valor? [S/N] ')).upper().strip()[0]
    if perg == 'S':
        print('Digite o valor desejado: ')
        valor = int(input('Valor: '))
        valores.append(valor)
    elif perg == 'N':
        break
    else:
        print('Resposta inválida!')
print(valores)