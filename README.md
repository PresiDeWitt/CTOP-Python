# CTOP-Python

Proyecto de aprendizaje de Python organizado por unidades didácticas.

## Estructura del Proyecto

```
CTOP-Python/
├── data/                          # Archivos de datos compartidos
│   ├── archivo.txt
│   └── seudoCodigo.txt
│
├── Unidad_01/                     # Fundamentos de Python
│   ├── ejercicios/
│   │   └── verificador_edad.py    # Validación y categorización de edades
│   └── tareas/                    # TAREAS EVALUABLES (OPT1)
│       ├── ejercicio1.py          # Componentes de Python
│       ├── ejercicio2.py          # Paradigmas de programación
│       ├── ejercicio3.py          # Sintaxis básica
│       ├── ejercicio4.py          # Conceptos fundamentales
│       ├── ejercicio5.py          # Debate sobre Python
│       └── README.md
│
├── Unidad_02/                     # Estructuras de datos y manejo de errores
│   ├── ejercicios/
│   │   ├── algoritmos/
│   │   │   ├── basta.py
│   │   │   ├── comparar_cantidades.py
│   │   │   ├── cuenta_atras.py
│   │   │   └── nota_media.py
│   │   ├── manejo_archivos/
│   │   │   ├── escritura_archivo.py
│   │   │   ├── try-except_2.py
│   │   │   └── try-except_3.py
│   │   ├── contar_vocales.py
│   │   └── crear_lista.py
│   └── tareas/                    # TAREAS EVALUABLES (OPT2)
│       ├── ejercicio1.py          # Diagrama de flujo
│       ├── ejercicio2.py          # Algoritmo par/impar
│       ├── ejercicio3.py          # Tabla de pruebas
│       ├── ejercicio4.py          # Depuración de código
│       ├── ejercicio5.py          # Explicación del algoritmo
│       └── README.md
│
├── Unidad_03/                     # Estructuras de control y funciones
│   ├── ejercicios/
│   │   ├── diccionario.py
│   │   ├── edad.py
│   │   ├── filtrar_nombres.py
│   │   ├── numeros_impares.py
│   │   ├── palabra.py
│   │   ├── suma.py
│   │   └── tabla_multiplicar.py
│   ├── ejemplos/
│   │   ├── manejo_listas.py
│   │   ├── parametros.py
│   │   ├── promedio.py
│   │   └── variable.py
│   └── tareas/                    # TAREAS EVALUABLES (OPT3)
│       ├── ejercicio1.py          # Mayor de tres números
│       ├── ejercicio2.py          # Números del 1 a N
│       ├── ejercicio3.py          # Calculadora básica
│       ├── ejercicio4.py          # Depuración área rectángulo
│       ├── ejercicio5.py          # Evaluación de rendimiento
│       └── README.md
│
└── RESUMEN_TAREAS.md              # Resumen completo de todas las tareas
```

## Cómo usar este proyecto

Cada unidad contiene:
- **ejercicios/**: Ejercicios prácticos para desarrollar habilidades
- **ejemplos/**: Código de demostración y ejemplos de conceptos
- **tareas/**: Tareas asignadas para evaluación (OPT1, OPT2, OPT3)

## Tareas Completadas

### 15 Tareas Implementadas (3 Unidades × 5 Ejercicios)

- **Unidad 1 (OPT1):** Conceptos básicos de Python
- **Unidad 2 (OPT2):** Desarrollo de algoritmos
- **Unidad 3 (OPT3):** Estructuras de control

Ver [RESUMEN_TAREAS.md](./RESUMEN_TAREAS.md) para detalles completos.

### Ejecutar todas las tareas

```bash
# Unidad 1
python3 Unidad_01/tareas/ejercicio1.py
python3 Unidad_01/tareas/ejercicio2.py
python3 Unidad_01/tareas/ejercicio3.py
python3 Unidad_01/tareas/ejercicio4.py
python3 Unidad_01/tareas/ejercicio5.py

# Unidad 2
python3 Unidad_02/tareas/ejercicio1.py
python3 Unidad_02/tareas/ejercicio2.py
python3 Unidad_02/tareas/ejercicio3.py
python3 Unidad_02/tareas/ejercicio4.py
python3 Unidad_02/tareas/ejercicio5.py

# Unidad 3
python3 Unidad_03/tareas/ejercicio1.py
python3 Unidad_03/tareas/ejercicio2.py
python3 Unidad_03/tareas/ejercicio3.py
python3 Unidad_03/tareas/ejercicio4.py
python3 Unidad_03/tareas/ejercicio5.py
```

## Convenciones

- Los nombres de archivos usan `snake_case` (minúsculas con guiones bajos)
- Los datos compartidos se encuentran en el directorio `data/` en la raíz
- Todos los ejercicios incluyen documentación completa (autor, fecha, descripción)

## Objetivos de Aprendizaje

- **Unidad 01**: Fundamentos de Python y validación de datos
- **Unidad 02**: Listas, cadenas, excepciones y manejo de archivos
- **Unidad 03**: Estructuras de control, funciones y diccionarios

## Documentación

Cada carpeta de tareas incluye un `README.md` detallado con:
- Descripción de cada ejercicio
- Resultados de aprendizaje cubiertos
- Instrucciones de ejecución
- Guías de depuración en VS Code
- Criterios de evaluación
