# Archivos de Datos

Este directorio contiene archivos de datos utilizados por los ejercicios y ejemplos del proyecto.

## Archivos

- **archivo.txt**: Archivo de texto para ejercicios de lectura/escritura
- **seudoCodigo.txt**: Ejemplos de pseudocódigo para referencia

## Uso

Los scripts en las diferentes unidades pueden referenciar estos archivos usando rutas relativas desde la raíz del proyecto.

Ejemplo:
```python
with open('data/archivo.txt', 'r') as f:
    contenido = f.read()
```
