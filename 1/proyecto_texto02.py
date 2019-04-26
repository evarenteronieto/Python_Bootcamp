cadena = "Bienvenido/a" 
print(cadena.center(50, "="))



entrada = input('Introduzca aquí el nombre completo del texto a analizar en formato << .txt >>:  ')
while entrada == '':
    print('Ha habido un error al encontrar su fichero, por favor, inténtelo de nuevo')
    entrada = input('Introduzca aquí el nombre completo del texto a analizar:  ')
        
#ABRIR EL ARCHIVO PARA LEERLO
    
archivo = open(entrada, 'r')
texto = archivo.read()
archivo.close()



#FUNCIONES CONTAR


def contar_palabras(texto):
    count = 0
    cc = ' '
    for c in texto:
        if c == ' ' and cc != ' ':
            count += 1
        cc = c
    if c != ' ':
        count += 1
        
    return count




def contar_vocales(texto):
    count = 0
    for c in texto:
        if c in "aeiouAEIOU":
            count = count + 1
    return count






def contar_consonantes(texto):
    count = 0
    for c in texto:
        if c in "bcdfghjklmnñpqrstvwxyzBCDFGHJKLMNÑPQRSTVWXYZ":
            count = count + 1
    return count







def contar_mayusculas(texto):
    count = 0
    for c in texto:
        if c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            count = count + 1
    return count






def contar_minusculas(texto):
    count = 0
    for c in texto:
        if c in "abcdefghijklmnopqrstuvwxyz":
            count = count + 1
    return count





def contar_numeros(texto):
    count = 0
    for c in texto:
        if c in "0123456789":
            count = count+  1
    return count






def contar_diferentes(texto):
    count = 0
    for c in texto:
        if c in "!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~\t\s\x0b\x0c":
            count = count + 1
    return count






def contar_parrafos(texto):  #aqui tengo que afinar mas, estoy en ello
    count = 0
    letter = ''
    for c in texto:
        if c in "\n\r":
            count = count + 1
    return count           




#FUNCIONES CORREGIR ESPACIOS Y MAYUSCULAS



def correcciones_espacios(texto):
    texto = texto.replace('  ', '')
    texto = texto.replace('. ', '.')
    texto = texto.replace(' .', '.')
    texto = texto.replace('.', '. ')
    texto = texto.replace(':', ': ')
    texto = texto.replace(';', '; ')
    texto = texto.replace(';  ', '; ')
    texto = texto.replace(',', ', ')
    texto = texto.replace('.    ', '.\n')
    texto = texto.replace('  ', ' ')
    texto = texto.replace(' -', ':\n-')
    texto = texto.replace('. 0', '.0')
    texto = texto.replace('. 1', '.1')
    texto = texto.replace('. 2', '.2')
    texto = texto.replace('. 3', '.3')
    texto = texto.replace('. 4', '.4')
    texto = texto.replace('. 5', '.5')
    texto = texto.replace('. 6', '.6')
    texto = texto.replace('. 7', '.7')
    texto = texto.replace('. 8', '.8')
    texto = texto.replace('. 9', '.9')
    texto = texto.replace(', 0', ',0')
    texto = texto.replace(', 1', ',1')
    texto = texto.replace(', 2', ',2')
    texto = texto.replace(', 3', ',3')
    texto = texto.replace(', 4', ',4')
    texto = texto.replace(', 5', ',5')
    texto = texto.replace(', 6', ',6')
    texto = texto.replace(', 7', ',7')
    texto = texto.replace(', 8', ',8')
    texto = texto.replace(', 9', ',9')
    
    
    
    return texto




def mayusc_correcciones(text):
    text = correcciones_espacios(texto)
    text = ". ".join(oracion.capitalize() for oracion in text.split(". "))
    return text





#FUNCION PARA CREAR EL ARCHIVO STATS.TXT



def guardarArchivo(valor):
  # Abro (o creo) el archivo de salida en modo anexar, para agregar al final del archivo.
  with open("stats.txt","a") as archivo:
    if type(valor) is list:
      # Si el valor recibido es de tipo lista, uso writelines, para escribir todo de una vez
      archivo.writelines("\n".join(valor))
    else:
      # Si no, uso write, para escribir sólo el valor.
      archivo.write("\n" + str(valor))




#VARIABLES PARA CREAR ARCHIVOS

palabras = 'Su texto tiene: ',contar_palabras(texto),'palabras.'
guardarArchivo(palabras)

vocales = 'Su texto tiene: ',contar_vocales(texto),'vocales.'
guardarArchivo(vocales)

consonantes = 'Su texto tiene: ',contar_consonantes(texto),'consonantes.'
guardarArchivo(consonantes)

mayusculas = 'Su texto tiene: ',contar_mayusculas(texto),'mayusculas.'
guardarArchivo(mayusculas)

minusculas = 'Su texto tiene: ',contar_minusculas(texto),'minusculas.'
guardarArchivo(minusculas)

numeros = 'Su texto tiene: ',contar_numeros(texto),'numeros.'
guardarArchivo(numeros)

diferentes = 'Su texto tiene: ',contar_diferentes(texto),'caracteres diferentes.'
guardarArchivo(diferentes)

parrafos = 'Su texto tiene: ',contar_parrafos(texto),'parrafos.'
guardarArchivo(parrafos)







#FUNCION PARA CREAR EL ARCHIVO CORREGIDO.TXT


def guardarArchivo_correccion(valor):
  # Abro (o creo) el archivo de salida en modo anexar, para agregar al final del archivo.
  with open("correccion.txt","a") as archivo:
    if type(valor) is list:
      # Si el valor recibido es de tipo lista, uso writelines, para escribir todo de una vez
      archivo.writelines("\n".join(valor))
    else:
      # Si no, uso write, para escribir sólo el valor.
      archivo.write("\n" + str(valor))


#VARIABLES PARA CREAR ARCHIVOS

corregido = mayusc_correcciones(texto)
guardarArchivo_correccion(corregido)




archivo.close()