from random import randint

Aleatorio = randint(0, 5)

print("\033[32m-----------------------------")
print("|                           | ")
print("|                           | ")
print("|\033[31m    Adivinhe o número \033[32m     | ")
print("|   \033[31m    Entre 0 e 5   \033[32m      | ")
print("|                           | ")
print("------------------------------")
print("        ------------          ")
print("        ------------          ")
print("     ------------------       ")

escolha = int(input("\n"))

if escolha > 5:
    print(" \n \033[35m O número escolhido é inválido")

if escolha == Aleatorio:
    print("\033[32m------------------------------")
    print("|                           | ")
    print("| \033[31m      Parabéns você    \033[32m   | ")
    print("|   \033[31m      adivinhou    \033[32m     | ")
    print("|                           | ")
    print("------------------------------")
    print("        ------------          ")
    print("        ------------          ")
    print("     ------------------       ") 

else:
    print("\033[32m------------------------------")
    print("|                           | ")
    print("| \033[31m      VOCÊ ERROU!!   \033[32m     | ")
    print("| \033[31m   O COMPUTADOR VENCEU  \033[32m  | ")
    print("|                           | ")
    print("------------------------------")
    print("        ------------          ")
    print("        ------------          ")
    print("     ------------------       ") 
    