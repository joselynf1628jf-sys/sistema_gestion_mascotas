# Sistema de Gestión de Mascotas

**Nombre completo del estudiante:** Joselyn Yomaira Fuentes Rosero

## Descripción del proyecto

Este proyecto implementa un pequeño sistema de gestión de mascotas que resuelve el
mismo problema —registrar y mostrar la información básica de una mascota
(**nombre**, **especie** y **edad**)— utilizando **dos enfoques de programación
diferentes**: Programación Tradicional y Programación Orientada a Objetos (POO).

### Programa 1: Programación Tradicional
Ubicado en la carpeta `programacion_tradicional/`, archivo `tradicional.py`.

Resuelve el problema usando únicamente **variables y funciones**, sin clases ni
objetos. El programa solicita los datos de la mascota mediante el teclado a través
de la función `registrar_mascota()` y los presenta de forma organizada con la
función `mostrar_informacion()`. La función `main()` coordina la ejecución.

### Programa 2: Programación Orientada a Objetos
Ubicado en la carpeta `programacion_poo/`, dividido en dos archivos:

- `mascota.py`: define la clase **`Mascota`**, con los atributos `nombre`,
  `especie` y `edad`, y los métodos `mostrar_informacion()` y `hacer_sonido()`.
- `main.py`: crea **dos objetos** de la clase `Mascota` y ejecuta sus métodos
  para mostrar la información y el sonido de cada una.

Este programa evidencia los conceptos de **clase, objeto, atributos, métodos y
abstracción**.

## Estructura del repositorio

```
Repositorio GitHub
├── programacion_tradicional/
│   └── tradicional.py
├── programacion_poo/
│   ├── main.py
│   └── mascota.py
└── README.md
```

## Cómo ejecutar los programas

Se requiere tener **Python 3** instalado.

**Programa tradicional** (pide datos por teclado):
```bash
cd programacion_tradicional
python tradicional.py
```

**Programa orientado a objetos:**
```bash
cd programacion_poo
python main.py
```

## Reflexión: diferencias entre Programación Tradicional y POO

Al desarrollar el mismo problema con ambos enfoques pude observar varias
diferencias importantes:

- **Organización del código:** En la programación tradicional los datos
  (variables) y las acciones (funciones) están separados; los datos viajan como
  parámetros de una función a otra. En la POO, los datos y los comportamientos se
  agrupan dentro de un mismo objeto, lo que mantiene todo más unido y ordenado.

- **Reutilización y escalabilidad:** En el enfoque tradicional, registrar varias
  mascotas implica manejar muchas variables sueltas o estructuras adicionales. Con
  POO basta con crear nuevos objetos de la clase `Mascota`, lo que hace el código
  mucho más fácil de ampliar y reutilizar.

- **Abstracción:** La POO permite representar una mascota como una entidad del
  mundo real con sus propias características (atributos) y acciones (métodos),
  mientras que el enfoque tradicional se centra más en el "paso a paso" de las
  instrucciones.

- **Mantenimiento:** Si en el futuro se quisiera agregar un nuevo dato o
  comportamiento, en POO solo se modifica la clase `Mascota` y todos los objetos
  se benefician del cambio; en el enfoque tradicional habría que ajustar varias
  funciones.

En conclusión, la programación tradicional resulta sencilla y directa para
problemas pequeños, mientras que la programación orientada a objetos ofrece una
estructura más clara, reutilizable y fácil de mantener a medida que el programa
crece.
