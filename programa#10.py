# Escribe un programa que solicite al usuario dos números y determine cuál es mayor o 
# si son iguales

print('........................................')
print('          es mayor o menor              ')
print('........................................')
 
print('\n')

num1 = input('ingrese un numero:')
print()
num2 = input('ingrese otro numero:')
print()


if num1 < num2 :
    print(f'=> el numero:{num1} es menor que :{num2}')
    
elif num1 > num2 :
    print(f'=> el numero :{num1} es meyor que :{num2}')
    
elif num1 == num2 :
    print('=> son iguales ')


 
