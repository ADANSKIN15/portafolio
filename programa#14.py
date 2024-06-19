# Escribe un programa que solicite
# las longitudes de los tres lados de un triángulo y 
# determine si es un triángulo válido (la suma de las longitudes de dos lados debe ser 
# mayor que la longitud del tercer lado)

print('  determina si un triangulo es valido ')
print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')

la = float(input('ingrese lado A: '))
lb = float(input('ingrese lado B: '))
lc = float(input('ingrese lado C: '))

print()

if la + lb > lc:
    print('es valido')

elif lc + lb > la:
    print('es valido')
    
elif lc + la > lb:
    print(' es valido')
       
else:
    print('no es valido')