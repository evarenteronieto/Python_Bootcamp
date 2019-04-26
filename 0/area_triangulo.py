base = input("Escribe la base de tu triángulo: ")
altura = input("Introduce la altura de tu triángulo: ")

def n_decimal(numero):
    try:
        float(numero)
        return True
    except:
        return False
    
if n_decimal(base):
    b = float(base)
else:
    print(base,"debe ser un número")
    quit()


if n_decimal(altura):
    h = float(altura)
else:
    print(altura, "debe ser un número entero: ")
    quit()


def area_triangulo():
    area = (b*h)/2
    print("Él área de tu triángulo es: ", round(area,2))
    
area_triangulo()
