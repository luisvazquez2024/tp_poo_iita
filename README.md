# TP POO IITA
## Ejercicio: Reproductor de Música en POO con Python

""
Descripción:
Se debe modelar un reproductor de música que puede reproducir sonido desde diferentes fuentes:

MP3 (por defecto)
CD
Consola
Cada fuente debe tener su propia forma de indicar que está reproduciendo música:

MP3: "Sonando MP3"
CD: "Sonando CD"
Consola: "Sonando Consola"
El reproductor debe tener un método reproducir() que muestre el mensaje correspondiente según la fuente activa. Además, debe contar con un método cambiar_fuente(nueva_fuente) que permita cambiar la fuente de reproducción sin utilizar estructuras condicionales (if, elif, else, match-case).

Requisitos Técnicos:
Utilizar el concepto de polimorfismo para evitar el uso de condicionales.
Crear una clase Reproductor con los métodos reproducir() y cambiar_fuente(nueva_fuente).
Crear una clase para cada fuente de sonido (MP3, CD, Consola) con su propia implementación de reproducir().
El programa debe iniciar con la fuente MP3 por defecto.

"""