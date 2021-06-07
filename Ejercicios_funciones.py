# Ejercicios en clase
# Pruebas
x = "HoLa"
y = x[::-1] #PYTHON SLICE STRING
z = x.lower()
print(x[:4])
print(y)
print(z)
print (len(x))


# Crea una funcion que dado una palabra diga si es palindroma o no.

# Python slice   
# [inicio: final: step] **final no se considera
def Palindromo(pal):
    pal = pal.lower()
    inv = pal[::-1]
    if pal == inv:
        print("OOhh!! Es Palindromaa!")
        print(f"""Palabra: {pal}
Invertida: {inv}""")
    else:
        print("No es palindroma")

Palindromo("Reconocer")        

# - Crea una función que tome una lista y devuelva el primer y el último valor de la lista. Si la longitud de la lista es menor que 2, haga que devuelva False.

def devolver(lista = []): #AL ASIGNARLE VALOR = [], PERMITE QUE AL NO DARLE PARAMETROS A LA FUNCION, NO TIRA ERROR Y CONTINUA
    if len(lista) >= 2:
        x = lista[0]
        y = lista[len(lista)-1]  # y = lista[:len(lista)]  SLICE STRING
        print("Primero:", x)
        print("Ultimo:", y)
        return x,y
    else:
        print("La longitud es menor que dos")
    return False, False #Asi en la linea 41 se define bien ambas variables

ejemplo = devolver([12,3,4,5,6,7,8,9,"hola"]) #EL RETURN CREA UNA TUPLA

print("tupla =", ejemplo)
primero,ultimo = ejemplo
print(f"El primero es {primero}, y el ultimo es {ultimo}")


# - Crea una función que tome una lista y devuelva un diccionario con su mínimo, máximo, promedio y suma.

def Diccionario(lista):
    minimo = min(lista)
    maximo = max(lista)
    suma = sum(lista)
    promedio = sum(lista)/len(lista)
    dic = {"Minimo" : minimo, "Maximo": maximo,"Suma": suma, "Promedio": promedio}
    return dic
print(Diccionario([1,2,3,4,5,6,7,8,9,10]))

# Otra forma 

def Funcion(lista):
    minimo = lista[0]
    maximo = lista[0]
    suma = 0
    promedio = 0
    for i in lista:
        if i < minimo:
            minimo = i 
        if i > maximo:
            maximo = i
        suma += i
    promedio = suma/len(lista)
    dic = {"Minimo" : minimo, "Maximo": maximo,"Suma": suma, "Promedio": promedio}
    return dic
print(Funcion([1,2,3,4,5,6,7,8,9,10]))

#Agregar de apoco a dic
# def Diccionario(lista):
#     dic = {}
#     minimo = min(lista)
#     dic["Minimo"] = minimo
#     maximo = max(lista)
#     suma = sum(lista)
#     promedio = sum(lista)/len(lista)
    
#     return dic
# print(Diccionario([1,2,3,4,5,6,7,8,9,10]))

