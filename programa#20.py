# Escribe un programa que solicite
# la distancia recorrida en kilómetros y calcule la tarifa 
# del taxi. La tarifa es $2.50 por kilómetro para los primeros 10 kilómetros
# y $2.00 por kilómetro adicional

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
print('        tarifa del kilometraje       ')
print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n')

d = float(input(' ingrese kilometro:'))

print()

ex = 2.00
pa = 2.50

a = d * pa
e = ((d - 10) * ex)
total = 25 + e

if 1 <= d <= 10 :
    print(f'precio a pagar: {a}')
    
        
elif d > 10 :
    total = 25 + e
    print(f'su tarifa despues de 10km es:{e}')
    print(f'la tarifa es :{total}')
    
        
            