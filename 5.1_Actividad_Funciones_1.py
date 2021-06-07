#1
def a():
    return 5
print(a())

"""
CONSOLA : 5
"""

#2
def a():
    return 5
print(a()+a())

"""
CONSOLA : 10
"""

#3
def a():
    return 5
    return 10 #No llega a ejecutarse esta parte :D
print(a())

"""
CONSOLA : 5
"""

#4
def a():
    return 5
    print(10) #No se ejecuta esta parte
print(a())

"""
CONSOLA : 5
"""

#5
def a():
    print(5)
x = a()            # imprime  "5", pero la funcion no retorna ningun valor
print(x)           # x se le asigna el valor "None"

"""
CONSOLA : 5 , None
"""

#6
def a(b,c):
    print(b+c)
print(a(1,2) + a(2,3)) # Imprime: 1+2 , y 2+3 . se retornan "none" en ambas y no se pueden sumar (error)

"""
CONSOLA : 3, 5  
"""


#7
def a(b,c):
    return str(b)+str(c)  
print(a(2,5)) 

"""
CONSOLA : 2 5
"""

#8
def a():
    b = 100
    print(b)  # imprime 100
    if b < 10:
        return 5
    else:
        return 10 # retorna 10!
    return 7 # no se ejecuta
print(a())

"""
CONSOLA : 100, 10 
"""

#9
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3# no se ejecuta
print(a(2,3)) # retorna 7 
print(a(5,3)) # retorna 14
print(a(2,3) + a(5,3)) # retorna 7 + 14 

"""
CONSOLA : 7, 14, 21
"""

#10
def a(b,c):
    return b+c
    return 10 #no se ejecuta
print(a(3,5))

"""
CONSOLA : 8
"""

#11
b = 500
print(b) # 500
def a():
    b = 300
    print(b)
print(b)# 500
a() # 300
print(b) # 500

"""
CONSOLA : 500, 500, 300, 500
"""

#12
b = 500
print(b) #500
def a():
    b = 300
    print(b)
    return b
print(b) #500
a()     #300
print(b) #500

"""
CONSOLA : 500, 500, 300, 500
"""

#13
b = 500
print(b) # 500
def a():
    b = 300
    print(b)
    return b
print(b) # 500
b=a() # 300 , b=300
print(b) #300

"""
CONSOLA : 500, 500, 300, 300
"""

#14
def a():
    print(1) # 1
    b() # busca la funcion e imprime 3
    print(2) # 2 
def b():
    print(3)
a() 

"""
CONSOLA : 1, 3, 2
"""

#15
def a():
    print(1)
    x = b() #x = 5 e imprime 3
    print(x) # 5
    return 10
def b():
    print(3)
    return 5
y = a() #1, 3 , 5 e y= 10
print(y) # 10

"""
CONSOLA :1, 3, 5, 10
"""