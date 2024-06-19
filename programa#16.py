# Escribe un programa que solicite al usuario
# su peso y altura, calcule
#el Índice de Masa Corporal

print(' calcular el IMC')
print('^^^^^^^^^^^^^^^^^\n')

peso = float(input('ingrese peso en kg: '))

alt = float(input('ingrese altura en mts.: '))

IMC = peso / alt**2
print()

print('>>> su indice de masa corporal es de :', round ( IMC ,2))

if IMC <= 18.50 :
    print('-> bajo peso \n')
    
elif 18.50 <= IMC <= 24.99:
    print('-> peso normal\n')
    
elif 25 <= IMC <= 29.99 :
    print('-> sobre peso\n')
    
elif IMC >= 30 :
    print('-> obesidad ')
    
    
    
