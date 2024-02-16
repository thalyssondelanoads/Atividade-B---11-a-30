print('Transformar M para Km|M')
print('------')

m = float(input('Qual o valor em M? : '))

km = int(m // 1000)
m2 = int(m % 1000)

print('-------')
print(f' O resultado é {km} Quilômetros e {m2} Metros ! ')