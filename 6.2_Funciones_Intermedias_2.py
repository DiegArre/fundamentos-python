"""
ACTIVIDAD 1 : Actualiza los valores en diccionarios y listas

"""

# Cambia el valor 10 en x a 15. Una vez que haya terminado, x ahora debería ser [[5,2,3], [15,8,9]].

x = [ [5,2,3], [10,8,9] ] 
# print(x[1][2]) #Listas dentro de listas
def Cambialista(lista):
    for i in range(0,len(lista)): #recorre la lista y obtiene 2 listas
        # print(lista[i])
        for j in range(0,len(lista[i])): #recorre las listas internas 
            # print(lista[i][j])
            if lista[i][j] == 10:
                lista[i][j] = 1
    return lista
print(Cambialista(x))
print(x)     



# Cambia el apellido del primer alumno de 'Jordan' a 'Bryant'

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
def CambiaApellido(lista):
    for i in lista:
        # print(i["last_name"])
        if i["last_name"] == "Jordan":
            i["last_name"] = "Bryant"
    return lista        
print(CambiaApellido(students))



# En el directorio sports_directory, cambia 'Messi' a 'Andres'

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
def CambiarDict(diccionario):
    for i in diccionario:
        # print(diccionario[i])
        for j in range(0,len(diccionario[i])):  
            # Como hay una lista hay que recorrerala con range para poder cambiar su valor despues. Si no fuera lista solo se cambia diccionario[i]
            # print(diccionario[i][j])
            if diccionario[i][j] == "Messi":
                diccionario[i][j] = "Andres"
    return diccionario
print(CambiarDict(sports_directory))



# Camba el valor 20 en z a 30

z = [ {'x': 10, 'y': 20} ]

def Cambiarvalor(lista):
    for dict in lista: #Primero hay que recorrer la lista
        # print(dict)
        for keys in dict:
            print(dict[keys])#Da los valores del objeto
            if dict[keys] == 20:
                dict[keys] = 30
    return lista        

print(Cambiarvalor(z))


"""
ACTIVIDAD 2: Itera a través de una lista de diccionarios.

"""

# Crea una función iterateDictionary(some_list) que, dada una lista de diccionarios, la función recorra cada diccionario de la lista e imprime cada clave y el valor asociado. Por ejemplo, dada la siguiente lista:

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(lista):
    for dicts in lista:
        print(dicts)
        for key, values in dicts.items():
            print(f"{key} - {values}")

iterateDictionary(students) 

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]


def iterateDictionary(lista):
    bonus = ""
    for dicts in lista:
        # print(dicts)
        # print(len(dicts))
        quizas = len(dicts)
        for key, values in dicts.items():
            bonus += f"{key} - {values}"
            while quizas > 1:
                bonus += ", "
                quizas -= 1
            # print(f"{key} - {values}")
        bonus += "\n"
    print(bonus)
iterateDictionary(students) 

# La salida debería ser: (Está bien si cada clave y valor quedan en dos líneas separadas)
# Bonus: Hacer que aparezcan exactamente así!
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel


"""
ACTIVIDAD 3: Itera a través de una lista de diccionarios.

"""

# Obtén valores de una lista de diccionarios
# Crea una función iterateDictionary2(key_name, some_list)que, dada una lista de diccionarios y un nombre de clave, la función imprima el valor almacenado en esa clave para cada diccionario. Por ejemplo, iterateDictionary2 ('first_name', students) debería generar:

# Michael
# John
# Mark
# KB
# Y iterateDictionary2('last_name', students) debería generar:

# Jordan
# Rosales
# Guillen
# Tonel


students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary2(key_name, some_list):
    for datos in some_list:
        print(datos[key_name])

iterateDictionary2('last_name', students)    


"""
ACTIVIDAD 4: Itera a través de un diccionario con valores de listas

"""

# Crea una función printInfo(some_dict)que, dado un diccionario cuyos valores son todas listas, imprima el nombre de cada clave junto con el tamaño de su lista, y luego imprima los valores asociados dentro de la lista de cada clave. Por ejemplo:


dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dict):
    for key, value in dict.items():

        print(key.upper(),len(value))
        for datos in value:
            print(datos)
printInfo(dojo)

# # output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon
