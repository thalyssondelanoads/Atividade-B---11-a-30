print('Transformar segundos em Horas,Minutos e Segundos')
print('----------')

total_segundos = int(input('Digite o número de segundos: '))

horas = total_segundos // 3600
minutos = (total_segundos % 3600) // 60
segundos = total_segundos % 60

print('-------------')
print(f'{total_segundos} segundos correspondem a {horas} horas, {minutos} minutos e {segundos} segundos!')
