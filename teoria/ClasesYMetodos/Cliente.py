class Cliente:
    def __init__(self, nombre, direccion, edad):
        self.nombre = nombre
        self.direccion = direccion
        self.edad = edad
def imprimirDetalles(persona):
    print("Nombre:", persona.nombre, "Dirección:", persona.direccion, "Edad:", persona.edad)

