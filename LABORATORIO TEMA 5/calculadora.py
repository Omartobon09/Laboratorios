import random
def calculadora():
    print("=== CALCULADORA BÁSICA ===")
    while True:
        print("\nOperaciones disponibles:")
        print("1. Suma (+)")
        print("2. Resta (-)")
        print("3. Multiplicación (*)")
        print("4. División (/)")
        print("5. Salir")
        opcion = input("Selecciona una operación: ")
        if opcion == "5":
            print("¡Gracias por usar la calculadora!")
            break 
        if opcion in ["1", "2", "3", "4"]:
            try:
                num1 = float(input("Primer número: "))
                num2 = float(input("Segundo número: "))
                
                if opcion == "1":
                    resultado = num1 + num2
                    print(f"{num1} + {num2} = {resultado}")
                elif opcion == "2":
                    resultado = num1 - num2
                    print(f"{num1} - {num2} = {resultado}")
                elif opcion == "3":
                    resultado = num1 * num2
                    print(f"{num1} * {num2} = {resultado}")
                elif opcion == "4":
                    if num2 != 0:
                        resultado = num1 / num2
                        print(f"{num1} / {num2} = {resultado}")
                    else:
                        print("Error: No se puede dividir por cero")
                        
            except ValueError:
                print("Error: Ingresa números válidos")
        else:
            print("Opción no válida")
def juego_adivinanza():
    print("=== JUEGO DE ADIVINANZA ===")
    numero_secreto = random.randint(1, 100)
    intentos = 0
    print("He pensado un número entre 1 y 100. ¡Adivínalo!")
    while True:
        try:
            intento = int(input("Tu adivinanza: "))
            intentos += 1
            if intento == numero_secreto:
                print(f"¡Felicidades! Adivinaste el número {numero_secreto} en {intentos} intentos")
                break
            elif intento < numero_secreto:
                print("El número es MAYOR")
            else:
                print("El número es MENOR")
        except ValueError:
            print("Por favor, ingresa un número válido")
calculadora()
juego_adivinanza()