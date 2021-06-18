#print = exibir
print ("Olá")
print(7+7)
print("7"+"7")
print("Olá,", 5)
nome = "Rafael"
idade = "18"
game = "GTA"
print (nome,idade,game)

#input = interagir
nome = input("Qual o seu nome? ")
idade = input("Qual o sua Idade? ")
game = input("Qual o seu game? ")
print (nome,idade,game)


#int, float, bool, str = Tipo de valores e soma simples
inteiro = int(input("inteiro"))
número_com_virgula = float(input("Número com virgula"))
verdadeiro_ou_falso = bool(input("Verdadeiro ou falso"))
texto = str(input("Aceita Texto"))
soma = inteiro + número_com_virgula

#{}.format(primeiro{}, segundo{}, e etc...) = mostrar a variavel
print(".format {}, segundo .format {}" .format(inteiro,texto))

#Se é possivel converter o valor em um número com int com .isnumeric()
n = input("algo:")
print(n.isnumeric())

#se é letra com .isalpha()
n = input("algo:")
print(n.isalpha())

#se é alphanúmerico com .isalnum()
n = input("algo:")
print(n.isalnum())

#se está só com letras maiúsculas com .isupper
n = input("algo:")
print(n.isupper())

