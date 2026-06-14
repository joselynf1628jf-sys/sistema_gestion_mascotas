# ============================================================
# Archivo: mascota.py
# Define la clase Mascota (Programación Orientada a Objetos).
# Evidencia el uso de: clase, atributos, métodos y abstracción.
# ============================================================


class Mascota:
    """
    Clase que representa una mascota.
    Abstrae las características y comportamientos básicos de una mascota.
    """

    # Método constructor: inicializa los atributos del objeto
    def __init__(self, nombre, especie, edad):
        # Atributos de la clase
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    def mostrar_informacion(self):
        """
        Método que muestra la información de la mascota de forma organizada.
        """
        print("\n=== Información de la mascota ===")
        print(f"Nombre  : {self.nombre}")
        print(f"Especie : {self.especie}")
        print(f"Edad    : {self.edad} año(s)")
        print("================================")

    def hacer_sonido(self):
        """
        Método que muestra el sonido característico según la especie.
        Demuestra el comportamiento (método) propio del objeto.
        """
        # Diccionario que asocia cada especie con su sonido
        sonidos = {
            "perro": "Guau guau!",
            "gato": "Miau!",
            "vaca": "Muuu!",
            "pato": "Cuac cuac!",
            "pajaro": "Pío pío!",
        }

        # Se busca el sonido; si no existe, se usa un valor por defecto
        sonido = sonidos.get(self.especie.lower(), "Hace un sonido...")
        print(f"{self.nombre} dice: {sonido}")
