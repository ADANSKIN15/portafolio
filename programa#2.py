#Escribe un programa que solicite la edad del usuario
#y determine si es un adolescente 
#(entre 13 y 19 años)

print(' Determina si es adolecente ')
print('****************************')

edad = int(input('ingrese su edad:' ))

print()

if 13<=edad and edad <=19:
    print('!!!eres adolecente!!!')
    
else:
    print(' -> no predeterminado <- ')
    