def soma(a, b):
        #Insira o codigo aqui
    print("A soma é: ",a+b)
def subtrai(a, b):
        #Insira o codigo aqui
    print("A subtração é: ",a-b)
def multiplica(a, b):
        #Insira o codigo aqui
    print("A multiplicação é: ",a*b)
def divide(a, b):
        #Insira o codigo aqui
    print ("A divisão é: ",a/b)


#Programa principal

print("Calculadora simples")

num1 = float(input("Insira o primeiro numero: "))
num2 = float(input("Insira o segundo numero: "))

if num2 != 0:
    soma(num1, num2)
    subtrai(num1, num2)
    multiplica(num1, num2)
    divide(num1, num2)
else:
    print("o segundo número não pode ser 0")







