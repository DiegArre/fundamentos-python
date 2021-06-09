# Objetivo de esta asignación es escribir una sola función, randInt() que tome hasta 2 argumentos.

# Si no se proporcionan argumentos, la función debería devolver un entero aleatorio entre 0 y 100.
# Si solo se proporciona un número máximo, la función debe devolver un número entero aleatorio entre 0 y el número máximo.
# Si solo se proporciona un número mínimo, la función debe devolver un número entero aleatorio entre el número mínimo y 100
# Si se proporcionan un número mínimo y máximo, la función debe devolver un número entero aleatorio entre esos 2 valores



#FUNCION DEL RANDOM !!!!!!!!!!!!!!
import random
num = 15.5
print(random.random())             #devuelve un número flotante aleatorio entre 0.00 y 1.00
print(random.random() * 50)        #devuelve un número flotante aleatorio entre 0.00 y 50.99
print(random.random() * 25 + 10)   #devuelve un número flotante aleatorio entre 10.00 y 35.99
print(round(num))                  #devuelve el valor entero redondeado de num


#FUNCION EDITADA Y TERMINADA FUNCIONANDO 
import random
def randInt(min = 0, max = 100):
    if min > max or max < 0:
        print("***Recuerde que el maximo por defecto es 100 (el maximo minimo es 99) y el maximo no puede ser menor a 0***")
        return False
    else:
        maxrandom = max-min    #Por la forma de funcionar random.random(), la suma tiene que ser el maximo!
        num = random.random() * maxrandom + min
        return round(num)

print(randInt()) 		    # debería imprimir un número aleatorio entre 0 a 100
print(randInt(max=50)) 	    # debería imprimir un número aleatorio entre 0 a 50
print(randInt(min=50)) 	    # debería imprimir un número aleatorio entre 50 a 100
print(randInt(min=50, max=500))    # debería imprimir un número aleatorio entre 50 y 500









