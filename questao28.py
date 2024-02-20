print('Transformar Horas em Semanas,Dias e Horas')
print('------------')
total_horas = int(input("Digite o número de horas: "))

semanas = total_horas // 168  # 1 semana = 7 dias * 24 horas
dias = (total_horas % 168) // 24
horas = total_horas % 24

print('-----------')
print(f"{total_horas} horas correspondem a {semanas} semanas, {dias} dias e {horas} horas!")
