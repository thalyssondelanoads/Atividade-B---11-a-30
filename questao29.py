print('Transformar Meses em Anos e Meses')
print('------------')

mes = int(input('Qual valor em Meses? : '))

ano = mes // 12
mes_result = mes - ( ano * 12 )

print('------------')
print(f'O resultado é {ano} Anos e {mes_result} Meses! ')
