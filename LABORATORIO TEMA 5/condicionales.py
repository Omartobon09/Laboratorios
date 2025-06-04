
numero = int(input("Ingresa un número: "))
if numero % 2 == 0:
    print(f"El número {numero} es par")
else:
    print(f"El número {numero} es impar")
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("\nCuadrados de los números del 1 al 10:")
for num in numeros:
    cuadrado = num ** 2
    print(f"{num}² = {cuadrado}")
print("\nIngresa números (escribe 'salir' para terminar):")
while True:
    entrada = input("Número: ")
    if entrada.lower() == 'salir':
        print("¡Hasta luego!")
        break
    try:
        numero = float(entrada)
        print(f"Has ingresado: {numero}")
    except ValueError:
        print("Por favor, ingresa un número válido o 'salir'")