# Análisis de un estudio de caso: decisión de diversificar contenidos en un diario colombiano

Trabajo académico del módulo **Metodología de Casos**, Maestría en Arquitectura de Software, Politécnico Grancolombiano. Corresponde a la actividad "Análisis de un estudio de caso" y reúne los Escenarios 3, 5 y 7.

El caso analizado es el de Arango-Forero y Roncallo-Dow (2013): en 1995, el director de un diario colombiano debe decidir si la empresa continúa solo con los impresos o si se expande hacia la generación de múltiples contenidos.

## Pregunta central

¿Qué factores determinan si al diario le conviene más incursionar en la generación de múltiples contenidos o continuar solo con los impresos?

## Recomendación

Una expansión gradual y condicionada, con compuertas de decisión entre etapas, que mantenga el impreso como base de caja.

## Contenido del documento

| Escenario | Contenido |
|-----------|-----------|
| **Escenario 3** | Árbol del problema (causas, problema central y efectos) y criterios de validez del estudio. |
| **Escenario 5** | Diseño metodológico, diagnóstico del mercado de medios y tabla de información cualitativa y cuantitativa. |
| **Escenario 7** | Cursos de acción, matriz multicriterio, ruta por etapas con compuertas, estructura del estudio y triangulación. |

Las figuras del documento se incluyen por separado en `docs/figuras/`:

- `figura1_arbol_problema.png`: árbol del problema.
- `figura2_ruta_etapas.png`: ruta de implementación por etapas y compuertas.

## Estructura del repositorio

```
.
├── docs/
│   ├── Analisis_Estudio_de_Caso_Diario.docx
│   └── figuras/
│       ├── figura1_arbol_problema.png
│       └── figura2_ruta_etapas.png
├── src/
│   └── sensibilidad_matriz.py
├── .gitignore
├── LICENSE
└── README.md
```

## Prueba de sensibilidad de la matriz multicriterio

El script `src/sensibilidad_matriz.py` calcula el puntaje ponderado de las tres opciones (A. solo impresos, B. expansión plena, C. gradual) sobre seis criterios y bajo cuatro perfiles de pesos. Luego simula 100.000 combinaciones aleatorias de pesos (semilla fija) para estimar con qué frecuencia gana cada opción.

Requisitos: Python 3.9 o superior. No usa dependencias externas.

```
python src/sensibilidad_matriz.py
```

Resultados de referencia:

| Perfil de pesos | A. Solo impresos | B. Expansión plena | C. Gradual |
|-----------------|-----------------:|-------------------:|-----------:|
| Base | 3,35 | 2,85 | **3,95** |
| Prioriza crecimiento | 2,90 | 3,40 | **4,10** |
| Prioriza riesgo | **3,95** | 2,20 | 3,70 |
| Pesos iguales | 3,50 | 2,50 | **4,00** |

En la simulación, la opción C gana en cerca del 73 % de las combinaciones, la A en cerca del 26 % y la B en menos del 1 %.

## Referencia del caso

Arango-Forero, G., & Roncallo-Dow, S. (2013). Social media and new audiences as a new challenge for traditional and new media industries. En M. Friedrichsen & W. Mühl-Benninghaus (Eds.), *Handbook of social media management: Value chain and business models in changing media markets* (pp. 635-656). Springer.

## Autor

Alejandro de Mendoza Tovar
Politécnico Grancolombiano, 2026

## Licencia

Distribuido bajo la licencia MIT. Ver [LICENSE](LICENSE).
