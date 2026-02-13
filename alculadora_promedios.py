# calculadora_promedios.py

def ingresar_calificaciones():
    """
    Solicita al usuario el número de materias y luego pide nombre y calificación (0 a 10).
    Retorna dos listas paralelas: (materias, calificaciones)
    """
    materias = []
    calificaciones = []

    # Pedir número de materias con validación
    while True:
        try:
            n = int(input("Ingrese el número de materias: ").strip())
            if n <= 0:
                print("El número de materias debe ser un entero positivo.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor ingrese un número entero.")

    # Pedir materias y calificaciones
    for i in range(n):
        nombre = input(f"Ingrese el nombre de la materia #{i+1}: ").strip()
        if nombre == "":
            nombre = f"Materia_{i+1}"

        while True:
            try:
                nota = float(input(f"Ingrese la calificación de {nombre} (0 a 10): ").strip())
                if 0.0 <= nota <= 10.0:
                    break
                print("La calificación debe estar en el rango de 0 a 10.")
            except ValueError:
                print("Entrada inválida. Por favor ingrese un número para la calificación.")

        materias.append(nombre)
        calificaciones.append(nota)

    return materias, calificaciones


def calcular_promedio(calificaciones):
    """
    Calcula el promedio de una lista de calificaciones.
    Si la lista está vacía, retorna 0.0 para evitar división por cero.
    """
    if not calificaciones:
        return 0.0
    return sum(calificaciones) / len(calificaciones)


def determinar_estado(calificaciones, umbral):
    """
    Determina qué materias están aprobadas y reprobadas según umbral.
    Retorna dos listas con los ÍNDICES: (aprobadas, reprobadas)
    """
    aprobadas = []
    reprobadas = []

    for i, nota in enumerate(calificaciones):
        if nota >= umbral:
            aprobadas.append(i)
        else:
            reprobadas.append(i)

    return aprobadas, reprobadas


def encontrar_extremos(calificaciones):
    """
    Identifica el índice de la calificación más alta y más baja.
    Retorna (indice_max, indice_min). Si lista vacía, retorna (None, None).
    """
    if not calificaciones:
        return None, None

    indice_max = 0
    indice_min = 0

    for i in range(1, len(calificaciones)):
        if calificaciones[i] > calificaciones[indice_max]:
            indice_max = i
        if calificaciones[i] < calificaciones[indice_min]:
            indice_min = i

    return indice_max, indice_min


def main():
    umbral = 5.0

    materias, calificaciones = ingresar_calificaciones()
    promedio = calcular_promedio(calificaciones)
    aprobadas, reprobadas = determinar_estado(calificaciones, umbral)
    idx_max, idx_min = encontrar_extremos(calificaciones)

    print("\n--- Resumen de Materias y Calificaciones ---")
    for i in range(len(materias)):
        print(f"{i+1}. {materias[i]}: {calificaciones[i]}")

    print(f"\nPromedio general: {promedio:.2f}")

    print("\nMaterias aprobadas (índices):", aprobadas)
    print("Materias reprobadas (índices):", reprobadas)

    # Mostrar extremos
    if idx_max is not None and idx_min is not None:
        print(f"\nCalificación más alta: {materias[idx_max]} (índice {idx_max}) -> {calificaciones[idx_max]}")
        print(f"Calificación más baja: {materias[idx_min]} (índice {idx_min}) -> {calificaciones[idx_min]}")

    print("\nGracias por usar la calculadora de promedios. ¡Hasta luego!")


if __name__ == "__main__":
    main()
