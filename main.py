class Producto:
    def __init__(self, id_producto,nombre, precio,cantidad):
        self.id_producto=id_producto
        self.nombre = nombre
        self.precio = precio
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


class Agregar:
    def agregar(self):
        print("Agregando...")

class AgregarProducto(Agregar):

    def agregar(self):
        diccionario_producto = {}
        print("--- Registro de Productos ---")
        id_producto = input("Ingresa el id producto: ")
        nombre_producto = input("Ingresa el nombre del producto: ")
        precio_producto = float(input("Ingresa el precio del producto: Q"))
        cantidad = int(input("Ingresa el cantidad del producto: "))
        producto = Producto(id_producto, nombre_producto, precio_producto, cantidad)
        diccionario_producto[id_producto] = {producto}





def Menu():
    print("--- Menu ---")
    print("1. Agregar Productos")
    print("2. Lista de Productos")
    print("4. Realizar Venta")
    print("5. Salir")

agregar_producto = AgregarProducto()
while True:
    Menu()
    try:
        opciones = int(input("Seleccione una opcion"))
        if opciones == 1:
            agregar_producto.agregar()
        elif opciones == 2:
            print("Lista de Productos")
        elif opciones ==3:
            print("Realizar Venta")
        elif opciones == 4:
            print("Gracias por utilizar el programa")
            break
        else:
            print("Opcion no valida")
    except ValueError:
        print("Solo es permitido el ingreso numerico")