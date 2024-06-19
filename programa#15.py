# Escribe un programa que solicite al usuario
# los años de experiencia y determine la categoría del trabajador:
# "Junior" (menos de 2 años), "Semi-Senior" (2-5 años), "Senior" (más de 5 años)

print(' categoria del trabajador')
print('--------------------------')

print()

print('si son mese agrege (0.) y la cantidad de mes.')
a = float(input('ingrese cuanto años tiene trabajando: '))

if 0.1 <= a <=2 :
    print('usted es junior')
    
elif 2<= a <= 5:
    print('usted es semi-senior')
    
elif a >= 5 :
    print('usted es senior')