#zad1a
a = [1-x for x in range(10)]
print(a)
#zad1b
b= [4**x for x in range(7)]
print(b)
#zad1c
c = [x for x in b if x % 2 == 0]
print(c)
#zad2
import random
lista1 = []
for y in range(10):
    lista1.append(random.randint(0, 10000))
print(lista1)
lista2 = [i for i in lista1 if i % 2 == 0]
print(lista2)

#zad4
def sprtroj(a,b,c):
    if (a ** 2 + b ** 2 == c ** 2 or
            a ** 2 + c ** 2 == b ** 2 or
            b ** 2 + c ** 2 == a ** 2):
        print("trójkąt jest prostokątny")
    else:
        print("trójkąt nie jest prostokątny")
    return
print(sprtroj(3,4,5))
print(sprtroj(6,4,5))

#zad5
a=5
b=7
h=3
pole=(((a+b)*h)/2)
print(pole)
