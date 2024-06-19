# Escribe un programa
# que solicite un número al usuario y determine si es divisible por 3, 
# por 5, por ambos o por ninguno

print(' divisible 3 y 5')
print('*****************\n')

D = int(input('ingrese un número :'))


div3 = D % 3
div5 = D % 5
div = div3 + div5


if div3 == 0 :
    print('es multiplo de 3')
    
elif div5 == 0 :
    print('es multiplo de 5')
    
elif div == 0 :
    print('es multiplo de 3 y 5')
    
else:
    print('no es multiplo de 3 y 5')


