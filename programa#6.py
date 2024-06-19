# Escribe un programa que solicite la edad del usuario y clasifique la edad en una de las 
# siguientes categorías: "Infantil" (0-12), "Adolescente" (13-19), "Adulto" (20-59) y "Adulto 
# mayor" (60 o más).

print('******************************')
print('  clasificacion de edad ')
print('****************************** \n')


E = int(input(' ingrese su edad:'))

if 0 <= E <= 12 :
    print('-> infantil')
    
elif 13 <= E <= 19 :
    print('-> adolecente')
    
elif 20 <= E <= 59 :
    print('-> adulto')
    
elif E > 60 :
    print(' -> adulto mayor')


