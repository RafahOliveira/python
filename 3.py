#import "biblioteca" = importar biblioteca completa
#from "biblioteca" import "oque você quer importar" = importar algo especifico de dentro da biblioteca

import  math
import random
#from math import ceil,floor
#n1 = math.ceil(input(""))           #Arredondamento pra cima
#n1 = math.floor(input(""))          #Arredondamento para baixo
#n1 = math.trunc(input(""))          #Eliminar da virgula pra frente
#n1 = math.pow(input(""))            #Potência
#n1 = math.sqrt(input(""))           #Raiz quadrada
#n1 = math.factorial(input(""))      #Fatorial

n1 = int(input("Digite um número: "))
raiz = math.sqrt(n1)
print("A raiz de {} é igual a {}." .format(n1,raiz))
print("A raiz de {} é igual a {}." .format(n1, math.ceil(raiz)))
print("A raiz de {} é igual a {}." .format(n1, math.floor(raiz)))
print("A raiz de {} é igual a {:.2f}." .format(n1, raiz))

n2 = random.random()
print(n2)

n3 = random.randint(1, 10)
print(n3)