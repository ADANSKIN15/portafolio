# Escribe un programa
# que solicite un nombre al usuario y determine si el nombre es 
# corto

print('determina un nombre corto o largo')
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n')

N = str(input('ingresar nombre: '))

can_pal = len (N)

if can_pal <= 5:
    print('tines un nombre corto')
    
elif 5<= can_pal <= 8:
    print('tines un nombre mediano')
    
elif can_pal >= 8:
    print('tines un nombre largo')
    
    




