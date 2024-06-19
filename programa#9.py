# Escribe un programa que solicite un carácter al usuario y determine si es una letra (a-z, 
# A-Z) o un dígito (0-9)

print('=======================================')
print('reconoce si es una letra o numero')
print('======================================= \n')

L = str(input('igrese letra o numero:'))

print()

if 'A' <= L <= 'Z' :
    print('=> es una letra')
    
elif 'a' <= L <= 'z' :
    print('=> es una letra')
    
elif 0 <= L <= 10 :
    print('=> es un numero')
    
else :
    print('=> no esta en el programa ')
    

