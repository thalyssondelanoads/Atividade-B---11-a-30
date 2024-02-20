print('Transformar Minutos em Dias,Horas e Minutos')
print('---------')

total_minutos = int(input('Digite o número de minutos: '))

dias = total_minutos // 1440
horas = (total_minutos % 1440) // 60
minutos = total_minutos % 60

print('---------')
print(f'{total_minutos} minutos correspondem a {dias} dias, {horas} horas e {minutos} minutos! ')
