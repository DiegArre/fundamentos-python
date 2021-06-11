arr = [1,7,4,0,5,14,-1,0,43,6]
     # 0 1 2 3 4 5

def ordenarBurbuja(lista):
    ultimo = len(lista)-1 # define el ultimo valor del arreglo i = 5
    while ultimo > 0: #Permite realizar la ultima vuelta cuando ultimo == 1 osea realiza el "len()-1" vueltas
        for i in range(len(lista)):
            if i < ultimo: # Llega al penultimo ya que se compara con el siguiente, esto incluye al ultimo! 
                if lista[i] > lista[i+1]: # lo compara con el siguiente, por eso se incluye al ultimo
                    lista[i], lista[i+1] = lista[i+1], lista [i]
                    print(lista)
                else:
                    print("Sin cambios",lista)
        ultimo -= 1 # Esto permite acotar ell array y no hacer la ultima comparacion, ya que sbemos que el nuevo ultimo es el mayor de todos

        print ("Vuelta, restantes: ",ultimo)
    return lista

print("Resultado final: ",ordenarBurbuja(arr))  