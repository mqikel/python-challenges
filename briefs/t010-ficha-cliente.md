# Tarea t010 — Ficha de cliente

**Tipo:** Tarea
**Dificultad:** Fácil
**Archivo a entregar:** `python-challenges/tasks/t010.py`
**Tema:** Diccionarios en Python (primera toma de contacto)
**Estimación:** 20–30 min
**Fecha de asignación:** 24/04/2026
**Serie:** 1 de 3 (continúa en `t011` y `t012`)

---

## Objetivo

Primer contacto con diccionarios usándolos para representar "un registro con propiedades" — un cliente de una tienda online. Se practican las 4 operaciones básicas: crear, mostrar, actualizar y contar. Todo encapsulado en funciones con type hints.

Esta tarea es la **base de una serie de tres**: las funciones que se implementen aquí se importarán desde `t011` y `t012` para introducir el concepto de reutilización vía imports.

## Descripción

En `t010.py` hay un docstring con el enunciado completo: contexto, funciones a implementar con firma exacta, y ejemplo de entrada/salida. Un cliente se representa con 4 claves: `nombre`, `email`, `ciudad`, `pedidos` (entero que arranca en 0).

**Regla de oro:** todo el código va dentro de funciones. Antes de teclear cada función, escribir un comentario de 2–4 líneas con qué hace, qué recibe y qué devuelve.

## Checklist

- [ ] `crear_cliente(nombre, email, ciudad)` devuelve dict con las 4 claves y `pedidos` a 0
- [ ] `mostrar_cliente(cliente)` imprime los 4 campos, uno por línea
- [ ] `actualizar_ciudad(cliente, nueva_ciudad)` modifica la clave y devuelve el dict
- [ ] `registrar_pedido(cliente)` incrementa `pedidos` en 1 y devuelve el dict
- [ ] Las 4 funciones llevan type hints
- [ ] Cada función tiene un comentario breve de cabecera
- [ ] El bloque de pruebas se ejecuta sin errores y muestra `Pedidos: 2` al final
- [ ] Commit: `feat(tasks): t010 ficha de cliente con operaciones basicas sobre dict`

## Notas para la daily

1. ¿Por qué un diccionario y no una lista para representar un cliente?
2. La función `actualizar_ciudad` devuelve el diccionario, pero si lo modificas dentro, ¿hace falta devolverlo? (spoiler: hablaremos de mutabilidad y paso por referencia)

## Labels sugeridos (Trello)

`diccionarios` · `funciones` · `tarea` · `facil` · `serie-tienda-online`
