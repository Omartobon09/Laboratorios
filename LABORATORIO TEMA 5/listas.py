
estudiantes = ["Ana", "Carlos", "María", "Juan", "Luis", "Carmen"]

print("Lista de estudiantes:")
for i, estudiante in enumerate(estudiantes, 1):
    print(f"{i}. {estudiante}")


contactos = {
    "Ana": "ana@email.com",
    "Carlos": "carlos@email.com",
    "María": "maria@email.com"
}

print("\nInformación de contacto:")
for nombre, email in contactos.items():
    print(f"Nombre: {nombre} - Email: {email}")

def gestionar_datos():
    while True:
        print("\n--- Gestor de Datos ---")
        print("1. Agregar estudiante a la lista")
        print("2. Agregar contacto al diccionario")
        print("3. Actualizar email de contacto")
        print("4. Mostrar lista de estudiantes")
        print("5. Mostrar contactos")
        print("6. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            nuevo_estudiante = input("Nombre del nuevo estudiante: ")
            estudiantes.append(nuevo_estudiante)
            print(f"Estudiante {nuevo_estudiante} agregado")
            
        elif opcion == "2":
            nombre = input("Nombre: ")
            email = input("Email: ")
            contactos[nombre] = email
            print(f"Contacto {nombre} agregado")
            
        elif opcion == "3":
            nombre = input("Nombre del contacto a actualizar: ")
            if nombre in contactos:
                nuevo_email = input("Nuevo email: ")
                contactos[nombre] = nuevo_email
                print(f"Email de {nombre} actualizado")
            else:
                print("Contacto no encontrado")
                
        elif opcion == "4":
            print("Estudiantes:", estudiantes)
            
        elif opcion == "5":
            print("Contactos:", contactos)
            
        elif opcion == "6":
            break
            
        else:
            print("Opción no válida")
gestionar_datos()