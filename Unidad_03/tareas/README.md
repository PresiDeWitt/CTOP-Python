# Unidad 3 - Tareas: Estructuras de Control

## OPT3 – Tarea individual

### Contenido

#### Ejercicio 1: Mayor de Tres Números (RA3_a)
**Archivo:** `ejercicio1.py`

Solicita tres números enteros y muestra cuál es el mayor usando:
- Condicionales múltiples (if-elif-else)
- Operadores lógicos (and)
- Detección de números iguales
- Ordenamiento adicional

#### Ejercicio 2: Números del 1 hasta N (RA3_a)
**Archivo:** `ejercicio2.py`

Pide un número entero positivo y muestra todos los números desde 1 hasta ese número:
- Bucle for con range()
- Validación de entrada positiva
- Cálculo de suma total
- Manejo de errores

#### Ejercicio 3: Calculadora Básica (RA2_b)
**Archivo:** `ejercicio3.py`

Programa que pide dos números y una operación (+, -, *, /) y muestra el resultado:
- Condicionales para cada operación
- Operadores aritméticos
- Validación de división por cero
- Manejo de errores de entrada

#### Ejercicio 4: Depuración de Código (RA2_c)
**Archivo:** `ejercicio4.py`

Depura código con errores para calcular área de rectángulo:
1. Identifica errores de sintaxis (print)
2. Identifica errores lógicos (** en lugar de *)
3. Identifica errores de tipo (input sin conversión)
4. Presenta código corregido
5. Explica las correcciones
6. Guía para usar depurador de VS Code

Errores corregidos:
- Error sintaxis: falta coma en print
- Error lógico: ** (potencia) → * (multiplicación)
- Error tipo: input() → float(input())

#### Ejercicio 5: Evaluación de Rendimiento (RA2_d)
**Archivo:** `ejercicio5.py`

Calcula la suma de números del 1 al 1.000.000 de dos formas:
1. Usando bucle for
2. Usando función sum(range())

Mide tiempos con módulo `time` y compara:
- Tiempo de ejecución de cada versión
- Porcentaje de diferencia
- Análisis del rendimiento
- Bonus: fórmula matemática de Gauss

## Cómo ejecutar

Cada ejercicio se ejecuta de forma independiente:

```bash
# Desde el directorio raíz del proyecto
python3 Unidad_03/tareas/ejercicio1.py
python3 Unidad_03/tareas/ejercicio2.py
python3 Unidad_03/tareas/ejercicio3.py
python3 Unidad_03/tareas/ejercicio4.py
python3 Unidad_03/tareas/ejercicio5.py
```

## Depuración en VS Code

Para el ejercicio 4:
1. Abrir `ejercicio4.py`
2. Colocar breakpoint en `area = base * altura`
3. Presionar F5 (Start Debugging)
4. Introducir valores de base y altura
5. Inspeccionar variables en panel Variables
6. Step Over (F10) para ejecutar línea por línea
7. Verificar que el área se calcula correctamente

## Medición de Rendimiento

El ejercicio 5 muestra diferencias significativas:
- Bucle for: ~0.05 segundos (implementación Python)
- sum(range()): ~0.01 segundos (implementación C optimizada)
- Fórmula Gauss: <0.001 segundos (cálculo directo O(1))

## Formato de entrega

La entrega de la tarea consiste en un documento en formato **PDF** con:
- Capturas de ejecución de todos los ejercicios
- Código fuente de cada ejercicio
- Para ejercicio 4: identificación clara de errores y correcciones
- Para ejercicio 5: tabla comparativa de tiempos
- Comentarios sobre el rendimiento

## Criterios cumplidos

### RA3_a - Estructuras de control
- Ejercicio 1: Condicionales múltiples (if-elif-else)
- Ejercicio 2: Bucle for con range()

### RA2_b - Entradas y salidas
- Ejercicio 3: input() y print() adecuados

### RA2_c - Depuración
- Ejercicio 4: Errores identificados y corregidos
- Pruebas con depurador de VS Code

### RA2_d - Evaluación de rendimiento
- Ejercicio 5: Medición con módulo time
- Comparación de versiones

### RA2_e - Documentación
- Todos los ejercicios con comentarios explicativos
- Autor y fecha identificados
- Ejemplos de entrada/salida
- Código legible e indentado correctamente
