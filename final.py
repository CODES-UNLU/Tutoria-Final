# Consigna 1
# El Servicio de Empleo Universitario de la UNLu ha solicitado desarrollar un programa que permita 
# cargar los datos de los egresados de la UNLu con el promedio general obtenido (el promedio es de tipo real).
# El programa deberá contener los módulos o funciones que permitan procesar lo siguiente, así como las llamadas 
# necesarias para su ejecución en el programa principal:

# a) Un módulo que permita al Servicio de Empleo Universitario cargar los promedios en una lista,
# validando que los valores ingresados se encuentren entre 1.00 y 10.00 (tipo real y no se ingresarán valores no numéricos),
# y retorne la lista cargada con los promedios correspondientes de todos los egresados. No se sabe cuántos son, 
# por lo tanto se deberá establecer una condición de corte informada al usuario desde el mismo módulo.

# b) Un módulo que, a partir de la lista anterior, 
# genere una lista con las cantidades de egresados en cada categoría según este esquema:

# Promedio entre 1 y 4 
# Promedio entre 4 y 6
# Promedio entre 6 y 7
# Promedio entre 7 y 9      
# Promedio entre 9 y 10 
# Este módulo deberá retornar la lista mencionada.



# c) En el programa principal, llamar al módulo del punto (b) y mostrar la lista indicando 
# los valores de rango con su respectiva cantidad y porcentaje (porcentaje = cantidad del rango / total * 100).

# isdigt() == dato[i] >= "0" or dato[i] <= "9":

def validar(dato):
    cant_punto = 0
    longitud = len(dato)
    for i in range(longitud):
        if dato[i] == ".":
            cant_punto += 1
            if cant_punto > 1:
                print("Error: El dato ingresado no puede tener más de un punto decimal.")
                flag = False
        elif (dato[i].isdigit() or dato[i] == "."):
            flag = True
    flag = False
    while not flag:
        if dato.isalpha():
            print("Error: El dato ingresado no es un número.")
            flag = False
            dato = input("ingrese el promedio del egresado (entre 1.00 y 10.00) o 'fin' para terminar: ")
        elif dato == "":
            print("Error: El dato ingresado no puede estar vacío.")
            flag = False
            dato = input("ingrese el promedio del egresado (entre 1.00 y 10.00) o 'fin' para terminar: ")
        elif 1.00 > float(dato) or float(dato) > 10.00:
            print("Error: El dato ingresado debe estar entre 1.00 y 10.00.")
            flag = False
            dato = input("ingrese el promedio del egresado (entre 1.00 y 10.00) o 'fin' para terminar: ")
        else:
            flag = True
    return flag


def carga_promedio():
    promedios = []
    prom = input("Ingrese el promedio del egresado (entre 1.00 y 10.00) o 'fin' para terminar: ")
    while prom.lower() != "fin":
        if validar(prom):
            promedios.append(prom)
        else:
            print("Promedio inválido. Debe estar entre 1.00 y 10.00.")
            prom = input("Ingrese el promedio del egresado (entre 1.00 y 10.00) o 'fin' para terminar: ")
        prom = input("Ingrese el promedio del egresado (entre 1.00 y 10.00) o 'fin' para terminar: ")
    return promedios

def categorias(promedios):
    categorias = [0, 0, 0, 0, 0]  # Inicializa las categorías
    for promedio in promedios:
        promedio = float(promedio)
        if 1 <= promedio < 4:
            categorias[0] += 1
        elif 4 <= promedio < 6:
            categorias[1] += 1
        elif 6 <= promedio < 7:
            categorias[2] += 1
        elif 7 <= promedio < 9:
            categorias[3] += 1
        elif 9 <= promedio <= 10:
            categorias[4] += 1
    return categorias

def main(categorias):
    suma = 0
    for i in range(len(categorias)):
        suma += categorias[i]
    rangos = [
    "promedio entre 1 y 4",
    "promedio entre 4 y 6",
    "promedio entre 6 y 7",
    "promedio entre 7 y 9",
    "promedio entre 9 y 10"
    ]

    for i in range(len(categorias)):
        porcentaje = categorias[i] / suma * 100 if suma != 0 else 0
        print(f"{rangos[i]}: {categorias[i]} ({porcentaje:.2f}%)")

# main(categorias(carga_promedio()))
     
    
        
                

# Consigna 2
# Desarrollar una función que, dada una lista de números enteros, 
# la recorra y retorne una lista con aquellos que sean divisibles por 3 y por 5.

# Consigna 3
# Desarrollar la función de prueba del ejercicio anterior, 
# incluyendo al menos 3 casos de prueba.
def divisibles_por_3_y_5(lista):
    return [num for num in lista if num % 3 == 0 and num % 5 == 0]

def test_divisibles(lista):
    # Caso 1: Lista con números divisibles por 3 y 5
    assert divisibles_por_3_y_5([15, 30, 45]) == [15, 30, 45], "Error en el caso 1"
    
    # Caso 2: Lista sin números divisibles por 3 y 5
    assert divisibles_por_3_y_5([1, 2, 4, 7]) == [], "Error en el caso 2"
    
    # Caso 3: Lista mixta
    assert divisibles_por_3_y_5([10, 15, 20, 25]) == [15], "Error en el caso 3"

divisibles_por_3_y_5([1, 2, 4, 7])
test_divisibles([])

# Solo para alumnos libres
# Desarrollar una función que reciba una lista con números enteros y 
# retorne el mayor de los impares y la posición en la que aparece por última vez.