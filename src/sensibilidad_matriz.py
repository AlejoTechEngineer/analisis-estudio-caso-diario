"""Prueba de sensibilidad de la matriz multicriterio del análisis de caso.

Calcula el puntaje ponderado de los tres cursos de acción evaluados para el
diario (A. solo impresos, B. expansión plena, C. expansión gradual) bajo
cuatro perfiles de pesos y, después, estima con qué frecuencia gana cada
opción cuando los pesos de los criterios se generan al azar.

Escala de puntajes: 1 (peor) a 5 (mejor) en cada criterio. En los criterios
de riesgo un puntaje alto significa menor riesgo.

Uso:
    python src/sensibilidad_matriz.py

Requiere Python 3.9 o superior y solo usa la biblioteca estándar.
"""

import random

CRITERIOS = [
    "Crecimiento en audiencia y pauta",
    "Activos y sinergias",
    "Riesgo financiero",
    "Riesgo de ejecución y regulatorio",
    "Flexibilidad",
    "Protección del impreso",
]

PUNTAJES = {
    "A. Solo impresos": [2, 2, 5, 5, 3, 4],
    "B. Expansión plena": [5, 4, 1, 2, 1, 2],
    "C. Gradual": [4, 5, 3, 3, 5, 4],
}

PERFILES = {
    "Base": [0.25, 0.20, 0.20, 0.15, 0.10, 0.10],
    "Prioriza crecimiento": [0.40, 0.20, 0.10, 0.10, 0.10, 0.10],
    "Prioriza riesgo": [0.10, 0.15, 0.30, 0.25, 0.10, 0.10],
    "Pesos iguales": [1 / 6] * 6,
}

SEMILLA = 1
SIMULACIONES = 100_000


def puntaje_ponderado(puntajes, pesos):
    """Devuelve la suma de cada puntaje multiplicado por su peso."""
    return sum(p * w for p, w in zip(puntajes, pesos))


def ganadora(pesos):
    """Devuelve el nombre de la opción con mayor puntaje ponderado."""
    return max(PUNTAJES, key=lambda op: puntaje_ponderado(PUNTAJES[op], pesos))


def formato(valor):
    """Formatea un número con dos decimales y coma decimal."""
    return f"{valor:.2f}".replace(".", ",")


def evaluar_perfiles():
    """Imprime el puntaje de cada opción por perfil y la opción ganadora."""
    print("Puntaje ponderado por perfil de pesos")
    print("=" * 37)
    for perfil, pesos in PERFILES.items():
        print(f"\n{perfil}")
        for opcion, puntajes in PUNTAJES.items():
            print(f"  {opcion:<20} {formato(puntaje_ponderado(puntajes, pesos))}")
        print(f"  Ganadora: {ganadora(pesos)}")


def simular_pesos():
    """Simula pesos aleatorios e imprime el porcentaje de victorias por opción.

    Cada peso se toma de una distribución exponencial y luego se normaliza
    para que el conjunto sume 1, lo que equivale a muestrear de manera
    uniforme todas las combinaciones posibles de pesos.
    """
    rng = random.Random(SEMILLA)
    victorias = {opcion: 0 for opcion in PUNTAJES}
    for _ in range(SIMULACIONES):
        crudos = [rng.expovariate(1.0) for _ in CRITERIOS]
        total = sum(crudos)
        pesos = [w / total for w in crudos]
        victorias[ganadora(pesos)] += 1

    print(f"\nSimulación de {SIMULACIONES:,} combinaciones de pesos (semilla {SEMILLA})".replace(",", "."))
    print("=" * 37)
    for opcion, n in sorted(victorias.items(), key=lambda kv: -kv[1]):
        porcentaje = formato(100 * n / SIMULACIONES)
        print(f"  {opcion:<20} {porcentaje} %")


def main():
    evaluar_perfiles()
    simular_pesos()


if __name__ == "__main__":
    main()
