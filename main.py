class Producto:
    def __init__(self, id_producto,nombre, cantidad):
        self.id_producto=id_producto
        self.nombre = nombre
        self.cantidad = cantidad


class Cliente:
    def __init__(self, id_cliente, nombre):
        self.id_cliente=id_cliente
        self.nombre = nombre


class Factura:
    def __init__(self, id_factura, nombre):
        self.id_factura=id_factura

class Guardar:
    def guardar(self):
        print("Guardando...")

def Menu():
    print("--- Menu ---")
    print("1. Agregar Productos")
    print("2. Lista de Productos")
    print("4. Realizar Venta")
    print("5. Salir")

while True:
    Menu()