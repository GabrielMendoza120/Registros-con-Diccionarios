agenda = [
    {"nombre": "Ana", "telefono": "555-1234", "email": "ana@outlook.com"},
    {"nombre": "Luis", "telefono": "555-5678", "email": "luis@outlook.com"}
]


def agregar_contacto():
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")
    email = input("Email: ")
    nuevo = {"nombre": nombre, "telefono": telefono, "email": email}
    agenda.append(nuevo)
    print("Contacto agregado.")


def buscar_contacto():
    nombre = input("Nombre a buscar: ")
    for contacto in agenda:
        if contacto["nombre"] == nombre:
            print("Encontrado:", contacto)
            return
    print("No se encontró ese contacto.")


def eliminar_contacto():
    nombre = input("Nombre a eliminar: ")
    for contacto in agenda:
        if contacto["nombre"] == nombre:
            agenda.remove(contacto)
            print("Contacto eliminado.")
            return
    print("No se encontró ese contacto.")


def listar_contactos():
    print("\n--- CONTACTOS ---")
    for contacto in agenda:
        print(contacto["nombre"], "-", contacto["telefono"], "-", contacto["email"])


opcion = ""
while opcion != "5":
    print("\n1. Agregar | 2. Buscar | 3. Eliminar | 4. Listar | 5. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        agregar_contacto()
    elif opcion == "2":
        buscar_contacto()
    elif opcion == "3":
        eliminar_contacto()
    elif opcion == "4":
        listar_contactos()
    elif opcion == "5":
        print("Programa terminado.")
    else:
        print("Opción no válida.")
