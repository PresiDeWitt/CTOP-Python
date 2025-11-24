# Unidad 2 - Tareas: Desarrollo de Algoritmos en Python

## OPT2 – Tarea individual

### Contenido

#### Ejercicio 1: Diagrama de Flujo (RA2_a)
**Archivo:** `ejercicio1.py`

Diagrama de flujo que representa un algoritmo para:
1. Pedir al usuario un número entero
2. Determinar si es par o impar
3. Mostrar el resultado en pantalla

Contiene representación textual ASCII del diagrama con inicio, proceso de decisión y fin.

#### Ejercicio 2: Implementación del Algoritmo (RA2_b)
**Archivo:** `ejercicio2.py`

Implementa en Python el algoritmo del ejercicio 1:
- Entrada de datos del usuario
- Determinación par/impar usando operador módulo (%)
- Salida del resultado
- Manejo de errores

#### Ejercicio 3: Pruebas de Validación (RA2_c)
**Archivo:** `ejercicio3.py`

Realiza pruebas del programa con:
- Número par (10)
- Número impar (7)
- Número negativo (-8)
- Número cero (0)

Presenta tabla con:
- Número introducido
- Resultado esperado
- Resultado obtenido
- ¿Coincide? [OK]/[FAIL]

#### Ejercicio 4: Identificación de Errores (RA2_d)
**Archivo:** `ejercicio4.py`

Analiza código erróneo y:
1. Identifica errores (tipo de dato, operador, sintaxis)
2. Escribe la versión corregida
3. Explica las correcciones realizadas
4. Guía para usar el depurador de VS Code

#### Ejercicio 5: Explicación del Algoritmo (RA2_e)
**Archivo:** `ejercicio5.py`

Explica el proceso de desarrollo:
- Cómo se ideó el algoritmo
- Por qué funciona correctamente
- Pasos para adaptarlo a múltiplo de 3
- Demostración práctica de la adaptación

## Cómo ejecutar

Cada ejercicio se ejecuta de forma independiente:

```bash
# Desde el directorio raíz del proyecto
python3 Unidad_02/tareas/ejercicio1.py
python3 Unidad_02/tareas/ejercicio2.py
python3 Unidad_02/tareas/ejercicio3.py
python3 Unidad_02/tareas/ejercicio4.py
python3 Unidad_02/tareas/ejercicio5.py
```

## Depuración en VS Code

Para el ejercicio 4, sigue estos pasos:
1. Abrir `ejercicio4.py` en VS Code
2. Colocar breakpoint en la línea del `if` (clic en margen izquierdo o F9)
3. Presionar F5 para iniciar el depurador
4. Introducir un número cuando se solicite
5. Inspeccionar variables en el panel de Variables
6. Usar Step Over (F10) para ejecutar línea por línea

## Formato de entrega

La entrega de la tarea consiste en un documento en formato **PDF** con:
- Diagrama de flujo (puede ser captura del ASCII o diagrama visual)
- Capturas de ejecución de cada ejercicio
- Tabla de pruebas del ejercicio 3
- Código corregido y explicaciones del ejercicio 4
- Explicación escrita del ejercicio 5

## Criterios cumplidos

- Diagramas de flujo claros
- Código implementado correctamente
- Pruebas documentadas en tabla
- Errores identificados y corregidos
- Explicaciones claras del proceso (6-10 líneas)
- Todos los ejercicios documentados con autor, fecha y ejemplos
