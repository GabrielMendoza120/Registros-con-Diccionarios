nombre = input("Ingresa el nombre del estudiante: ")
edad = int(input("Ingresa la edad: "))
carrera = input("Ingresa la carrera: ")
promedio = float(input("Ingresa el promedio: "))

estudiante = {
    "nombre": nombre,
    "edad": edad,
    "carrera": carrera,
    "promedio": promedio
}

print("\n--- FICHA DE ESTUDIANTE ---")
print("Nombre:", estudiante["nombre"])
print("Edad:", estudiante["edad"])
print("Carrera:", estudiante["carrera"])
print("Promedio:", estudiante["promedio"])
