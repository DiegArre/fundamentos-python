# Tamaño grande: dada una lista, escriba una función que cambie todos los números positivos de la lista a "big". Ejemplo: biggie_size ([- 1, 3, 5, -5]) devuelve la misma lista, pero cuyos valores son ahora [-1, "big", "big", -5]

def Tgrande(lista):
    newlista = []
    for x in lista:
        if x > 0:
            newlista.append("Big")
        else:
            newlista.append(x)
    return newlista

print(Tgrande([- 1, 3, 5, -5]))
    

# Contar positivos : dada una lista de números, cree una función para reemplazar el último valor con el número de valores positivos. (Tenga en cuenta que cero no se considera un número positivo). Ejemplo: count_positives ([- 1,1,1,1]) cambia la lista original a [-1,1,1,3] y la devuelve. Ejemplo 2: count_positives ([1,6, -4, -2, -7, -2]) cambia la lista a [1,6, -4, -2, -7,2] y la devuelve


def Contarpositivos(lista):
    positivos = []
    for x in lista:
        if x > 0:
            positivos.append(x)
    lista[-1] = len(positivos)
    return lista
print(Contarpositivos([- 1,1,1,1]))


# Suma total : crea una función que toma una lista y devuelve la suma de todos los valores de la matriz. Ejemplo: sum_total ([1,2,3,4]) debería devolver 10. Ejemplo 2: sum_total ([6,3, -2]) debería devolver 7

def Sum_total(lista):
    suma = 0
    for x in lista:
        suma += x

    print("A traves de funcion sum():",sum(lista))
    return(suma)
    
print("A traves de bucle for:", Sum_total([1,2,3,4,]))


# Promedio : crea una función que toma una lista y devuelve el promedio de todos los valores. Ejemplo: el promedio ([1,2,3,4]) debería devolver 2.5

def Promedio(lista):
    suma = 0
    for x in lista:
        suma += x
    print("A traves de funcion sum()y len()", sum(lista)/len(lista)) 
    return suma/len(lista)

print("A traves de bucle for:", Promedio([1,2,3,4,]))

# Longitud : crea una función que toma una lista y devuelve la longitud de la lista. Ejemplo: la longitud ([37,2,1, -9]) debería devolver 4. Ejemplo 2: longitud ([]) debería devolver 0

def Longitud(lista):
    x = len(lista)
    return x
print("Longitud",Longitud([37,2,1, -9]))


# Mínimo : crea una función que tome una lista de números y devuelva el valor mínimo en la lista. Si la lista está vacía, haga que la función devuelva False. Ejemplo: mínimo ([37,2,1, -9]) debería devolver -9. Ejemplo 2: mínimo ([]) debería devolver False

def Minimo(lista):
    if len(lista) == 0:
        return False
    else:
        minimo = lista[0]
        for x in lista:
            if x < minimo:
                minimo = x
        return minimo

print("Minimo: ",Minimo([37,2,1, -9]))    


# Máximo : crea una función que toma una lista y devuelve el valor máximo en la matriz. Si la lista está vacía, haga que la función devuelva False. Ejemplo: máximo ([37,2,1, -9]) debería devolver 37. Ejemplo 2: máximo ([]) debería devolver False

def Maximo(lista):
    if len(lista) == 0:
        return False
    else:
        maximo = lista[0]
        for x in lista:
            if x > maximo:
                maximo = x
        return maximo

print("Maximo: ",Maximo([37,2,1, -9])) 

# Análisis final : crea una función que tome una lista y devuelva un diccionario que tenga la suma total, promedio, mínimo, máximo y longitud de la lista. Ejemplo: ultimate_analysis ([37,2,1, -9]) debería devolver {'total': 31, 'promedio': 7.75, 'minimo': -9, 'maximo': 37, 'longitud': 4}

def Analisisfinal(lista):
    dic = {}
    dic["total"] = Sum_total(lista)
    dic["promedio"] = Promedio(lista)
    dic["minimo"] = Minimo(lista)
    dic["maximo"] = Maximo(lista)
    dic["longitud"] = Longitud(lista)
    return dic
print("Diccionario: ", Analisisfinal([37,2,1, -9]))    


# Lista inversa : crea una función que tome una lista y la devuelva con los valores invertidos. Haz esto sin crear una segunda lista. (Se sabe que este desafío aparece durante las entrevistas técnicas básicas).
# Ejemplo: reverse_list ([37,2,1, -9]) debería devolver [-9,1,2,37]


#A TRAVES DE CAMBIOS DE POSICION EN LA LISTA
def ListaInversa(lista):

    mitad = int(len(lista)/2)
    ultimo = len(lista)-1

    for x in range(0,mitad,1):
        lista[x], lista[ultimo-x] = lista[ultimo-x], lista[x]

    return lista

print(ListaInversa([37,2,1, -9,5]))



#USANDO UNA VARIABLE TEMPORAL
def ListaInversa(lista):

    mitad = int(len(lista)/2)
    ultimo = len(lista)-1

    for x in range(0,mitad,1):
        temp = lista[x]
        lista[x] = lista[ultimo-x]
        lista[ultimo-x] = temp
    return lista

print(ListaInversa([37,2,1, -9,5]))



#USANDO UNA SEGUNDA LISTA... NO LO PERMITE EL EJERCICIO
def ListaInversa(lista):
    inversa = []
    for x in range(len(lista)-1, 0-1, -1):
        inversa.append(lista[x])
    return inversa

print(ListaInversa([1,4,8,0]))