# Básico : imprime todos los enteros del 0 al 150.

for x in range(150+1):
    print(x)


# Múltiplos de cinco : imprime todos los múltiplos de 5 de 5 a 1,000

for x in range(5,1000+5,5):
    print(x)

# Contar, Dojo Way - imprime enteros del 1 al 100. Si es divisible por 5, imprima "Coding" en su lugar. Si es divisible por 10, imprima "Coding Dojo".

x = 1
while x <= 100:
    print(x)
    if x%5 == 0:
        if x%10 == 0:
            print("Coding Dojo")
        else:
            print("Coding")
    x += 1            
     
# ¡Uf, Eso es bastante grande!: suma enteros impares de 0 a 500,000 e imprime la suma final.

suma = 0
for x in range(1,500000,2):
    suma += x
print(suma)

# Cuenta regresiva por cuatro : imprime números positivos del 2018 al 0, restando 4 en cada iteración.

x = 2018
while x >= 0 :
    print(x)
    x -= 4


# Contador flexible : establece tres variables: lowNum, highNum, mult. Comenzando en lowNum y pasando por highNum, imprima solo los enteros que son múltiplos de mult. Por ejemplo, si lowNum = 2, highNum = 9 y mult = 3, el bucle debe imprimir 3, 6, 9 (en líneas sucesivas)

lowNum = 5
highNum = 54
mult = 3

for x in range(0,highNum+1,mult):
    if x < lowNum:
        continue
    else:
        print(x)

# BONUS: ¿Cómo se puede detectar si un número es primo? ¿Cómo retornar una lista con los primos entre el 1 y el 1000?


def Esprimo(num):
        if num < 2:
            return False
        for i in range(2,num):
            if num%i == 0:
                return False
        return True

primos = []
for x in range(1000):
    if Esprimo(x):
        primos.append(x)
    
print(primos)        
        

