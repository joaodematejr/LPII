numero1 = "Um\n"
numero2 = "Dois\n"
numero3 = "Três\n"
numero4 = "Quatro\n"
numero5 = "Cinco\n"

numero = -1

while numero != 0:
    numero = int (input("Para encerrar o programa digite 0 \nDigite um número inteiro entre 1 e 5: "))

    if numero < 1 or numero > 5:
        print ("Número inválido! Para encerrar o programa digite 0 \n Digite um número entre 1 e 5: ")

    if numero == 1:
        print(numero1)

    if numero == 2:
        print(numero2)
    
    if numero == 3:
        print(numero3)
    
    if numero == 4:
        print (numero4)
    
    if numero == 5:
        print (numero5)

print("Programa encerrado!")
    