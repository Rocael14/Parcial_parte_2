class Producto:
    def __init__(self, id_producto,nombre, precio,cantidad):
        self.id_producto=id_producto
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def listar(self):
        print(f"{self.id_producto} - {self.nombre} - Q{self.precio} - {self.cantidad}")

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

class Notificaciones:
    def __init__(self, tipo_notificacion, mensaje):
        self.tipo_notifcacion = tipo_notificacion
        self.mensaje = mensaje
    def notificar(self):
        print(f"{self.tipo_notifcacion}:")
        print(self.mensaje)

class NotificacionUrgencia:
    def notificar(self):
        print("Urgencia")
        print("Pedidos atrasados")

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


class AgregarCliente(Agregar):
    def agregar(self, nit):
        diccionario_cliente = {}
        id_cliente = nit
        nombre_cliente = input("Ingresa el nombre del cliente: ")
        cliente = Cliente(id_cliente, nombre_cliente)
        diccionario_cliente[id_cliente] = cliente
        print("Cliente Agregado Exitosamente")


class AgregarVenta(Agregar):
    def agregar(self):
        agregar_cliente = AgregarCliente()
        print("--- Realizar Venta ---")
        id_cliente = input("Nit del cliente o CF:").upper()
        if id_cliente == "CF":
            nombre_cliente = input("Ingrese el nombre del cliente: ")
        elif id_cliente != "CF":
            agregar_cliente.agregar(id_cliente)

        id_producto = input("Ingrese el id del producto: ")
        cantidad_producto = int(input("Ingrese la cantidad a llevar del producto: "))
        while True:
            seleccion_estado_pedido = int(input("Seleccione el estado del pedido (1.Normal o 2.Urgente): "))
            if seleccion_estado_pedido == 1:
                estado = "Normal"
                break
            elif seleccion_estado_pedido == 2:
                estado = "Urgente"
                break
            else:
                print("Seleccione un estado de pedido valido")

def Menu():
    print("--- Menu ---")
    print("1. Agregar Productos")
    print("2. Lista de Productos")
    print("3. Realizar Venta")
    print("4. Cambiar Notificacion")
    print("5. Salir")

agregar_producto = AgregarProducto()
agregar_venta = AgregarVenta()
notificar_urgencia =NotificacionUrgencia()
while True:
    #Aqui tendria que ir la notificaciones en dado caso exista un prodcuto con estado de URGENCIA!!!
    notificar_urgencia.notificar()
    Menu()
    try:
        opciones = int(input("Seleccione una opcion: "))
        if opciones == 1:
            agregar_producto.agregar()
        elif opciones == 2:
            print("Listar")
        elif opciones ==3:
            agregar_venta.agregar()
        elif opciones == 4:
            print("Notificacion")
        elif opciones == 5:
            print("Gracias por utilizar el programa")
            break
        else:
            print("Opcion no valida")
    except ValueError:
        print("Solo es permitido el ingreso numerico")