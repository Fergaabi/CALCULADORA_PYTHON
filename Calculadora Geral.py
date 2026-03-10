#INICIO DA CALCULADORA 
import math

print("CALCULADORA")

op = input("Digite 1 para ADIÇÃO, 2 para SUBTRAÇÃO, 3 para MULTIPLICAÇÃO, 4 para DIVISÃO, 5 para POTENCIAÇÃO, 6 para RADICIAÇÃO")
op = int(op)

a = int(input("Digite o Primeiro Número: "))
b = int(input("Digite o Segundo Número: "))

if (op == 1):
    print(a+b)
    
elif (op == 2):
    print(a-b)

elif (op ==3):
    print(a*b)

elif (op ==4):
    print(a/b)

elif (op==5):
    print (a**b)

elif (op==6):
    print (a**(0.5))

else:
    print("Digite um Número novamente")
    
input()

