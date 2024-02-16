print('Transformar Dias em Semanas|Dias')
print('------')

dia = int(input('Quantos Dias? : '))

sem = dia // 7
dia_rest = dia % 7

print('------')
print(f'O resultado é {sem} Semanas e {dia_rest} Dias ! ')