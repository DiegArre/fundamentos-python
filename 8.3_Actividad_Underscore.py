
class Underscore:

    def map(self, iterable, callback):
        temp = []
        for num in iterable:   
            temp.append(callback(num))   
        return temp

    def find(self, iterable, callback):

        for num in iterable:
            # print(callback(num))
            if callback(num): #== True:
                 return num



    def filter(self, iterable, callback):
        temp = []
        for num in iterable:
            if callback(num): #== True:
                temp.append(num)
        return temp

    def filter2(self, iterable, callback):
        return [x for x in iterable if callback(x)]

    def reject(self, iterable, callback):

        temp = []
        for num in iterable:
            if callback(num): #== True:
                continue
            else:
                temp.append(num)
        return temp 


# has creado una libreria con 4 métodos
# se crea la instancia de la clse
_ = Underscore() # sí, estamos configurando una instancia a una variable que es un guión bajo
evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
# debe retornar [2, 4, 6] después que termines de implementar el código de arriba

print(_.map([1,2,3], lambda x: x*2)) # debe retornar [2,4,6]
print(_.find([7,5,3,3,6,4], lambda x: x>4)) # debe retornar el primer valor que es mayor que 4
print(_.filter([1,2,3,4,5,6], lambda x: x%2==0)) # debe retornar [2,4,6]
print(_.filter2([1,2,3,4,5,6], lambda x: x%2==0)) # debe retornar [2,4,6]

print(_.reject([1,2,3,4,5,6], lambda x: x%2==0)) # debe retornar [1,3,5]







