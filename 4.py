#fatiamento

n1 = input("Digita: ")

print(n1[4])                            #pega a quarta letra
print(n1[2:6])                          #mostra oq ta na posição 2 até a 5 pois ele para de contar no 6 e nao mostra ele
print(n1[2:10:2])                       #vai pulando de 2 em 2
print(n1[:5])                           #Ele vai do inicio até a 5   
print(n1[5:])                           #Começa no 2 e vai até o final da string
print(n1[2::2])                         #começa no 2 e vai até o final pulando de 2 em 2

#Analise

print(len(n1))                           #contar quantos caracteres tem.
print(n1.count("e"))                     #contar quantos "e" tem na frase.
print(n1.count("e", 0, 13))              #contar quantos "e" tem na frase do começo "0" até o 12 "13".
print(n1.find("el"))                     #ele mostra onde ele encontrou o "el" começou na frase.
print(n1.find("Android"))                #se a string nao existe ele retorna como "-1"
print("Elias" in n1)                     #Se tiver Elias ele me retorna como true se nao tiver false
print(n1.replace("Elias","Rafael"))      #Muda a palavra Elias para Rafael
print(n1.upper())                        #Troca tudo que é minúsculo por maiúsculo
print(n1.lower())                        #Troca tudo que é maiúculo por minúsculo
print(n1.capitalize())                   #Transforma toda a string em minúscula e deixa a primeira letra em maiúscula
print(n1.title())                        #Transforma toda letra dps do espaços em minúscula e deixa a primeira letra em maiúscula
print(n1.strip())                        #Remove todos os espaços inúteis  
print(n1.rstrip())                       #Remove todos os espaços inúteis no final
print(n1.lstrip())                       #Remove todos os espaços inúteis no começo

#Divisão de strings

print(n1.split())                        #Divisão na string dentro dos espaços gerando outra lista para cada palavra
print('-'.join(n1))                      #Vai juntar as listas e separando cada espaço com oq colocar no meio das aspas
