# Escribe un programa que solicite
# al usuario su salario bruto y calcule el salario neto 
# después de aplicar un impuesto del 20% si el salario bruto es mayor a $2000


print("--------------------------------")
print("| 12. Calcular el salario neto |")
print("-------------------------------- \n")

salario=float(input("Ingrese el salario bruto: "))

if salario > 2000:
    impr = salario * 0.20
    sal_brut = salario - impr
    print("Su salario neto es:", sal_brut)
    
else:
    sal_brut = salario
    print("Su salario neto es:", sal_brut)





