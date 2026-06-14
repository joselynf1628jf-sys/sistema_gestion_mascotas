# ============================================================
# Archivo: main.py
# Programa principal (Programación Orientada a Objetos).
# Crea objetos de la clase Mascota y ejecuta sus métodos.
# ============================================================

# Se importa la clase Mascota desde el archivo mascota.py
from mascota import Mascota


def main():
    """
    Función principal: crea objetos Mascota y ejecuta sus métodos.
    """
    print("=== Sistema de gestión de mascotas (POO) ===")

    # Se crean al menos dos objetos de la clase Mascota
    mascota1 = Mascota("Firulais", "Perro", 3)
    mascota2 = Mascota("Michi", "Gato", 2)

    # Se almacenan en una lista para recorrerlos fácilmente
    mascotas = [mascota1, mascota2]

    # Se ejecutan los métodos definidos para cada objeto
    for mascota in mascotas:
        mascota.mostrar_informacion()
        mascota.hacer_sonido()


# Punto de entrada del programa
if __name__ == "__main__":
    main()
