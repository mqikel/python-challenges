# Tarea t012 — Catálogo como base de datos

**Tipo:** Tarea
**Dificultad:** Difícil
**Archivo a entregar:** `python-challenges/tasks/t012.py`
**Depende de:** `t011.py` (se importa `contar_ventas`)
**Tema:** Diccionarios de diccionarios, simulación de tabla de BD, reutilización vía imports
**Estimación:** 60–90 min
**Fecha de asignación:** 24/04/2026
**Serie:** 3 de 3

---

## Objetivo

Cerrar la serie de la tienda online construyendo una **mini base de datos en memoria**: un diccionario de diccionarios indexado por SKU. Se implementa un CRUD real (añadir, actualizar, buscar) más operaciones de analítica y una función que **cierra el círculo de reutilización** importando `contar_ventas` de `t011`.

## Descripción

El catálogo se representa así: clave = SKU (identificador único, como el `id` de una tabla SQL), valor = diccionario con `nombre`, `precio`, `stock`, `categoria`. Esto es, literalmente, la estructura mental de una fila en una base de datos.

La función estrella es `contar_por_categoria(catalogo)`: aplica exactamente el mismo patrón que `contar_ventas` de `t011`. En lugar de reimplementar, se importa y se llama con la lista de categorías extraída del catálogo. **Ese es el concepto pedagógico de esta tarea: función bien hecha + buenos imports = menos código que mantener.**

**Cómo ejecutar con imports:**

```
cd tasks
python t012.py
```

## Checklist

### Funciones del CRUD

- [ ] `anadir_producto` no sobrescribe si el SKU ya existe y avisa por pantalla
- [ ] `actualizar_stock` permite cambios positivos y negativos
- [ ] `actualizar_stock` no deja el stock por debajo de 0 (avisa y no aplica)
- [ ] `actualizar_stock` avisa si el SKU no existe
- [ ] `buscar_por_categoria` devuelve una lista de **nombres** de productos, no de SKUs
- [ ] `aplicar_descuento(catalogo, 10)` reduce todos los precios al 90%
- [ ] `valor_total_inventario` suma `precio * stock` de todos los productos

### Imports y reutilización

- [ ] Al inicio del archivo: `from t011 import contar_ventas`
- [ ] `contar_por_categoria` extrae la lista de categorías del catálogo y llama a `contar_ventas` pasándosela — **no reimplementa el patrón**
- [ ] El resultado final coincide con `{"ropa": 2, "hogar": 1, "libros": 1}` en el ejemplo

### Entrega

- [ ] Todas las funciones llevan type hints
- [ ] Cada función tiene un comentario breve de cabecera con qué hace, qué recibe y qué devuelve
- [ ] El bloque de pruebas se ejecuta completo y dispara los 3 avisos esperados (SKU duplicado, stock negativo, SKU inexistente)
- [ ] Commit: `feat(tasks): t012 catalogo como base de datos con imports de t011`

## Notas para la daily

1. El SKU es la clave del diccionario externo. ¿En qué se parece eso a una tabla SQL? Si tuvieras que pasar este catálogo a una BD real, ¿qué cambiaría y qué se mantendría?
2. `contar_por_categoria` reutiliza `contar_ventas`. ¿Qué tuviste que transformar antes de llamarla?
3. ¿Cuántas líneas te ha ahorrado importar `contar_ventas` en lugar de reescribirla? Extrapola a un proyecto con 50 archivos.

## Labels sugeridos (Trello)

`diccionarios` · `funciones` · `imports` · `reutilizacion` · `crud` · `base-de-datos` · `tarea` · `dificil` · `serie-tienda-online`
