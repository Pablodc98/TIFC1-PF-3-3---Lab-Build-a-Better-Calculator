#Primero defino las funciones que voy a usar

#suma Easy
def addmultiplenumbers(numeros):
    resultado = 0
    for n in numeros:
        resultado = resultado + n
    return resultado

#multiplicacion Easy
def multiplymultiplenumbers(numeros):
    resultado = 1
    for n in numeros:
        resultado = resultado * n
    return resultado

# Uso el modulo para saber si es entero o decimal y lo comparo Medium
def isitaninteger(num):
    if type(num) == bool:
        return False
    return num % 1 == 0

# uso el modulo para saber si es par o impar y lo comparo Easy
def isiteven(num):
    return isitaninteger(num) and num % 2 == 0

# Llamé las funciones en el main para que se ejecuten Medium 💪🏿💪🏿💪🏿💪🏿💪🏿💪🏿💪🏿 
def main():
    # Pedir dos numeros sencillos
    n1 = float(input("Primer numero: "))
    n2 = float(input("Segundo numero: "))
    lista = [n1, n2]

    print("Suma:", addmultiplenumbers(lista))
    print("Multiplicacion:", multiplymultiplenumbers(lista))
    print("¿El primero es entero?:", isitaninteger(n1))
    print("¿El primero es par?:", isiteven(n1))

if __name__ == "__main__":
    main()