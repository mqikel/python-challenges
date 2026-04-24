# Tarea t011 — Top de ventas

**Tipo:** Tarea
**Dificultad:** Medio
**Archivo a entregar:** `python-challenges/tasks/t011.py`
**Depende de:** `t010.py` (se importa)
**Tema:** Diccionarios como contadores de frecuencias + introducción a imports
**Estimación:** 30–40 min
**Fecha de asignación:** 24/04/2026
**Serie:** 2 de 3

---

## Objetivo

Consolidar el uso de diccionarios aplicando el patrón más común del mundo real: **contar frecuencias**. A la vez se introduce el concepto de **imports entre archivos**: se reutilizan funciones de `t010` (`crear_cliente`, `registrar_pedido`) sin reescribirlas.

## Descripción

En `t011.py` hay un docstring con el enunciado completo. Se trabaja sobre una lista de ventas del día (nombres de productos) y se construyen 4 operaciones de analítica + 1 función de integración que conecta con `t010`.

La función `registrar_compra(cliente, producto, recuento)` es el punto clave: combina el patrón contador con una llamada a `registrar_pedido` **importada de t010**. Esto es exactamente lo que pasa en un proyecto real: cada módulo usa utilidades de otros.

**Cómo ejecutar con imports:** desde la carpeta `tasks/`:

```
cd tasks
python t011.py
```

Si se ejecuta desde la raíz del repo, Python no encontrará `t010` y el import fallará. Este detalle se explica en la daily.

## Checklist

### Funciones principales

- [ ] `contar_ventas(ventas)` construye `{producto: cantidad}` recorriendo la lista con `for`
- [ ] Maneja correctamente productos nuevos (clave inexistente) sin lanzar `KeyError`
- [ ] `producto_mas_vendido(recuento)` devuelve la clave con mayor valor, calculada desde el dict
- [ ] `productos_con_minimo(recuento, minimo)` devuelve lista con productos cuya cantidad es `>=` al mínimo
- [ ] `total_unidades(recuento)` coincide con `len(ventas)` en el ejemplo (= 7)

### Imports y reutilización

- [ ] Al inicio del archivo: `from t010 import crear_cliente, registrar_pedido`
- [ ] `registrar_compra(cliente, producto, recuento)` incrementa el contador del producto **y** llama a `registrar_pedido(cliente)` para sumar al contador de pedidos del cliente
- [ ] El bloque de pruebas crea un cliente con `crear_cliente` (importada de t010) y registra 3 compras; al final `cliente["pedidos"]` debe valer 3

### Entrega

- [ ] Todas las funciones llevan type hints
- [ ] Cada función tiene un comentario breve de cabecera
- [ ] El archivo se ejecuta sin errores desde `tasks/` con `python t011.py`
- [ ] Commit: `feat(tasks): t011 top de ventas con patron contador e imports de t010`

## Notas para la daily

1. En el contador de ventas, ¿qué pasa si haces `recuento[producto] += 1` directamente sin comprobar antes si la clave existe? ¿Cómo lo resolviste?
2. `registrar_compra` no devuelve nada pero sí modifica los dos diccionarios que recibe. ¿Por qué funciona eso? (→ mutabilidad, paso por referencia)
3. Si ejecutas `python t011.py` desde la raíz del repo en lugar de desde `tasks/`, el import falla. ¿Por qué?

## Labels sugeridos (Trello)

`diccionarios` · `funciones` · `imports` · `reutilizacion` · `tarea` · `medio` · `serie-tienda-online`
