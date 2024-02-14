#Solicita os Valores ao Usuário!

print('Calcule a distância entre 2 pontos no plano !')
print('-----')

print('Informe as coordenadas de x1 e y1')
x1 = float(input('x1: '))
y1 = float(input('y1: '))
print('-----')

print('Informe as coordenadas de x2 e y2')
x2 = float(input('x2: '))
y2 = float(input('y2: '))
print('-----')

#Processa as informações e executa a fórmula!

dist = int(((x2 - x1) ** 2) + ((y2 - y1) ** 2))

#Entrega ao Usuário o Resultado da Operação! 

print(f'A distância entre os 2 pontos é √{dist} !')
aprox = round(float(dist ** 0.5), 2)
print('-----')

print(f'Dessa forma, o valor exato ou aproximado da distância é {aprox} !')