# La ordenación por selección funciona iterando a través de la lista, encontrando el valor mínimo y moviéndolo al comienzo de la lista.

def OrdenSeleccion(lista):
    
    for num in range(0,len(lista)-1): #Esto permite recorrer las lista en bucle saltandose 1 más por vuelta
        cambio = False #Esto permite ejecutar el cambio entre numero solo si en verdad hay alguno menor
        menor = lista[num] #Definimos al menor como el primero de la lista para luego hacer las comparaciones
        for i in range(num,len(lista),1): # Recorremos la lista desde num, saltandonos el que pusimos como menor al principio

            if lista[i] < menor: # Condicional de si alguien en la lista es menor que el primero
                cambio = True # Si encontro el menor procedemos a ejecutar el cambio linea 17
                menor = lista[i] # Asignamos a la variable menor al menor de la lista encontrado
                indice = i #y aca guardamos el indice para saber en que parte de la lista esta el menor
                # print("Es menor", lista[i], "indice", indice)
            

        if cambio == True: # Aca verificamos si necesitamos un cambio, entregado en la linea 11       
            lista[num], lista[indice] = lista[indice], lista[num] #Hacemos el swap entre el primero y el menor
        # print("el indice",indice)
        # print(lista)
        # print("Siguiente vuelta")
        """
        Termina el primer recorrido y se adigno al indice 0 de la lista el menor de esta misma lista, 
        Ahora en la siguiente vuelta se partira desde el siguiente indice, osea el 1, asi no comparamos de nuevo el que ya sabemos que es menor y esta el inicio, y asi hasta que se acabe la lista :D
        """

    return lista
print(OrdenSeleccion([4,5,6,1,2,3,9,-10]))
