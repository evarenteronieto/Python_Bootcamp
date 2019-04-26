precio = None
unidades = None

totalUnidades = 0
total = 0
subtotal = 0
resumen = ""

while precio == None and unidades == None:
    while precio == None:
        try:
            precio = float(input("Precio Unitario: "))
            if precio < 0:
                precio = None
                print('Sólo se admiten valores positivos')
        except:
            print('Se necesita un valor numérico')
            precio = None

    if precio == 0:
        unidades = 0

    while unidades == None:
        try:
            unidades = int(input("Unidades: "))
            if unidades < 0:
                unidades = None
                print('Sólo se admiten valores positivos')
        except:
            print('Se necesita un valor numérico positivo')
            unidades = None
    
    if unidades == 0:
        precio = 0

    totalUnidades += unidades
    subtotal = precio * unidades
    total += precio * unidades
    if precio != 0:
        resumen += "\n{} € - {} unidades = {} €".format(precio, unidades, subtotal)
        precio = None
        unidades = None
    
print(resumen)
print('------------------------')
print('Unidades: {}'.format(totalUnidades))
print('TOTAL: {:.2f} €'.format(total))