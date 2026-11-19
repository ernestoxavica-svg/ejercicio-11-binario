def busqueda_binaria(puntajes_ordenados, objetivo):
    """Divide a la mitad el rango de búsqueda en cada paso sobre una lista ordenada."""
    izquierda = 0
    derecha = len(puntajes_ordenados) - 1
    comparaciones = 0

    while izquierda <= derecha:
        comparaciones += 1
        medio = (izquierda + derecha) // 2
        valor_medio = puntajes_ordenados[medio]

        if valor_medio == objetivo:
            return medio, comparaciones
        elif valor_medio < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return -1, comparaciones


def ejecutar_binaria():
    # Lista previamente ordenada de menor a mayor
    puntajes = [45, 52, 60, 68, 70, 75, 80, 84, 88, 91, 95, 98, 100]

    print("\n--- EJERCICIO 2: BÚSQUEDA BINARIA (PUNTAJES ORDENADOS) ---")
    print("Puntajes registrados (ordenados):", puntajes)

    try:
        objetivo = int(input("Ingresa el puntaje exacto a buscar: ").strip())
    except ValueError:
        print("Error: debes ingresar un número entero válido.")
        return

    indice, comparaciones = busqueda_binaria(puntajes, objetivo)

    if indice != -1:
        print(f"Puntaje {objetivo} encontrado en el índice {indice}.")
    else:
        print(f"El puntaje {objetivo} no existe en la lista.")
    print(f"Comparaciones realizadas: {comparaciones}")


if __name__ == "__main__":
    ejecutar_binaria()