# Ejercicio en Python

## Consigna

Crear una convertidor minimalista de markdown a HTML que soporte tantas características de la sintaxis definida en https://en.wikipedia.org/wiki/Markdown#Example como se desee.

El input es un archivo markdown y el output un archivo html.

Ante cualquier falta de definición tomar una decisión y argumentarla en el README del proyecto o en comentarios en el código.

## Resolución

Ejecutar el archivo main.py

Traduce de markdown a HTML y soporta los siguientes markups:

* Párrafos separados por lineas en blanco a tags <p>
* Líneas que comienzan con # a tags <h1> ... <h6>
* Línea sucedidas por una línea solo con el caracter '=' a tag <h1>
* Texto entre doble '*' a tags <strong>
* Texto entre comillas invertidas '`' a tags <code>
* Texto entre guión bajo '_' a tags <em>