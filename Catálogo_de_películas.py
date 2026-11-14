catalogo = [
    {"titulo": "Inception", "director": "Christopher Nolan", "anio": 2010, "genero": "Ciencia Ficcion", "duracion": 148},
    {"titulo": "Parasite", "director": "Bong Joon-ho", "anio": 2019, "genero": "Drama", "duracion": 132},
    {"titulo": "Interstellar", "director": "Christopher Nolan", "anio": 2014, "genero": "Ciencia Ficcion", "duracion": 169},
    {"titulo": "Coco", "director": "Lee Unkrich", "anio": 2017, "genero": "Animacion", "duracion": 105}
]


def filtrar_genero():
    genero = input("Ingresa el género a buscar: ")
    print("\n--- RESULTADOS ---")
    for peli in catalogo:
        if peli["genero"].lower() == genero.lower():
            print(peli["titulo"], "-", peli["anio"], "-", peli["duracion"], "min")


def filtrar_anio():
    anio = int(input("Mostrar películas posteriores al año: "))
    print("\n--- RESULTADOS ---")
    for peli in catalogo:
        if peli["anio"] > anio:
            print(peli["titulo"], "(", peli["anio"], ")")


def ordenar_duracion():
    orden = input("Escribe 'asc' para ascendente o 'desc' para descendente: ")
    copia = catalogo.copy()

    # Ordenamiento sencillo comparando duraciones
    for i in range(len(copia)):
        for j in range(i + 1, len(copia)):
            if orden == "asc" and copia[i]["duracion"] > copia[j]["duracion"]:
                copia[i], copia[j] = copia[j], copia[i]
            elif orden == "desc" and copia[i]["duracion"] < copia[j]["duracion"]:
                copia[i], copia[j] = copia[j], copia[i]

    print("\n--- PELÍCULAS ORDENADAS ---")
    for peli in copia:
        print(peli["titulo"], "-", peli["duracion"], "minutos")


def duracion_promedio():
    suma = 0
    for peli in catalogo:
        suma = suma + peli["duracion"]
    promedio = suma / len(catalogo)
    print("\nLa duración promedio es:", promedio, "minutos")


opcion = ""
while opcion != "5":
    print("\n1. Filtrar por género | 2. Filtrar por año | 3. Ordenar duración | 4. Promedio | 5. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        filtrar_genero()
    elif opcion == "2":
        filtrar_anio()
    elif opcion == "3":
        ordenar_duracion()
    elif opcion == "4":
        duracion_promedio()
    elif opcion == "5":
        print("Programa terminado.")
    else:
        print("Opción no válida.")
