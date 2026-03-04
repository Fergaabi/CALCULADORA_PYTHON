import math

#Feito Por @_.Fergabi
print("OLÁ SEJA BEM VINDO À CALCULADORA DO FERNANDO")
print("Feito Por @_.Fergabi")

# Pedindo a operação
print("\nEscolha a operação:")
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("5 - Potenciação")
print("6 - Radiciação")

operacao = input("Digite o número da operação: ")

# Pedir números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Calcular
if operacao == "1":
    resultado = num1 + num2
    print("Resultado:", resultado)

elif operacao == "2":
    resultado = num1 - num2
    print("Resultado:", resultado)

elif operacao == "3":
    resultado = num1 * num2
    print("Resultado:", resultado)

elif operacao == "4":
    if num2 != 0:
        resultado = num1 / num2
        print("Resultado:", resultado)
    else:
        print("Erro: divisão por zero!")

elif operacao == "5":
    resultado = num1 ** num2
    print("Resultado:", resultado)

elif operacao == "6":
    # raiz de num1 com índice num2
    if num2 != 0:
        resultado = num1 ** (1/num2)
        print("Resultado:", resultado)
    else:
        print("Erro: raiz com índice zero!")

else:
    print("Operação inválida!")

input("\nPressione ENTER para sair...")