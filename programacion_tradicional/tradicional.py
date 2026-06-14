# ============================================================
# Programa 1: Programación Tradicional
# Sistema de gestión de mascotas usando funciones y variables.
# NO se utilizan clases ni objetos.
# ============================================================


def registrar_mascota():
    """
    Solicita los datos de la mascota por teclado y los devuelve.
    Utiliza variables simples para almacenar cada dato.
    """
    print("=== Registro de mascota ===")

    # Se solicitan los datos mediante teclado
    nombre = input("Ingrese el nombre de la mascota: ")
    especie = input("Ingrese la especie (perro, gato, etc.): ")

    # Validación sencilla de la edad para evitar errores
    edad = input("Ingrese la edad (en años): ")
    while not edad.isdigit():
        print("La edad debe ser un número entero. Intente nuevamente.")
        edad = input("Ingrese la edad (en años): ")
    edad = int(edad)

    # Se devuelven los datos para usarlos en otra función
    return nombre, especie, edad


def mostrar_informacion(nombre, especie, edad):
    """
    Muestra la información registrada de la mascota de forma organizada.
    Recibe los datos como parámetros.
    """
    print("\n=== Información de la mascota ===")
    print(f"Nombre  : {nombre}")
    print(f"Especie : {especie}")
    print(f"Edad    : {edad} año(s)")
    print("================================\n")


def main():
    """
    Función principal que coordina el registro y la muestra de datos.
    """
    # Se registran los datos llamando a la función correspondiente
    nombre, especie, edad = registrar_mascota()

    # Se muestran los datos registrados
    mostrar_informacion(nombre, especie, edad)


# Punto de entrada del programa
if __name__ == "__main__":
    main()
