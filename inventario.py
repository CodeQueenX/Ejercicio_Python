class Producto:
    def __init__(self, nombre, categoria, precio, cantidad):
        self._nombre = nombre
        self._categoria = categoria
        self._precio = precio
        self._cantidad = cantidad

    def actualizar_precio(self, precio):
        if precio > 0:
            self._precio = precio
        else:
            raise ValueError("El precio debe ser mayor que 0.")

    def actualizar_cantidad(self, cantidad):
        if cantidad >= 0:
            self._cantidad = cantidad
        else:
            raise ValueError("La cantidad debe ser mayor o igual que 0.")

    def __str__(self):
        return f"{self._nombre} - Categoría: {self._categoria}, Precio: {self._precio}, Cantidad: {self._cantidad}"

    # Getters
    def get_nombre(self):
        return self._nombre

    def get_categoria(self):
        return self._categoria

    def get_precio(self):
        return self._precio

    def get_cantidad(self):
        return self._cantidad

    # Setters
    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_categoria(self, categoria):
        self._categoria = categoria

    def set_precio(self, precio):
        self.actualizar_precio(precio)

    def set_cantidad(self, cantidad):
        self.actualizar_cantidad(cantidad)


class Inventario:
    def __init__(self):
        self._productos = []

    def agregar_producto(self, producto):
        # Validación de nombre vacío
        if not producto.get_nombre():
            raise ValueError("El nombre del producto no puede estar vacío.")
        
        # Validar si la cantidad del producto es mayor o igual a 0.
        if producto.get_cantidad() < 0:
            raise ValueError("La cantidad debe ser mayor o igual a 0.")
        
        # Lógica para agregar el producto si no existe
        if not any(p.get_nombre() == producto.get_nombre() for p in self._productos):
            self._productos.append(producto)
            print("Producto agregado correctamente.")
        else:
            print("El producto ya existe en el inventario.")

    def actualizar_producto(self, nombre, nuevo_precio, nueva_cantidad):
        # Validaciones de precio y cantidad
        if nuevo_precio <= 0:
            raise ValueError("El precio debe ser mayor que 0.")
        if nueva_cantidad < 0:
            raise ValueError("La cantidad debe ser mayor o igual a 0.")

        # Lógica para encontrar el producto y actualizarlo
        for producto in self._productos:
            if producto.get_nombre() == nombre:
                producto.set_precio(nuevo_precio)
                producto.set_cantidad(nueva_cantidad)
                print("Producto actualizado.")
                return
        print("El producto no existe en el inventario.")

    def eliminar_producto(self, nombre):
        producto = self.buscar_producto(nombre)
        if producto:
            self._productos.remove(producto)
            print("Producto eliminado.")
        else:
            print("Producto no encontrado.")

    def mostrar_inventario(self):
        if self._productos:
            for producto in self._productos:
                print(str(producto))
        else:
            print("El inventario está vacío.")

    def buscar_producto(self, nombre):
        return next((p for p in self._productos if p.get_nombre() == nombre), None)


def menu():
    inventario = Inventario()
    while True:
        print("\n--- Menú de Inventario ---")
        print("1. Agregar producto")
        print("2. Actualizar producto")
        print("3. Eliminar producto")
        print("4. Mostrar inventario")
        print("5. Buscar producto")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Ingrese el nombre del producto: ")
            if not nombre:  # Validación de nombre vacío
                print("El nombre del producto no puede estar vacío. Intente nuevamente.")
                continue
                
            categoria = input("Ingrese la categoría del producto: ")
            try:
                precio = float(input("Ingrese el precio del producto: "))
                if precio <= 0:  # Validación de precio negativo o cero
                    print("El precio debe ser mayor que 0. Intente nuevamente.")
                    continue
                    
                cantidad = int(input("Ingrese la cantidad en stock: "))
                if cantidad < 0:  # Validación de cantidad negativa
                    print("La cantidad debe ser mayor o igual a 0. Intente nuevamente.")
                    continue
                    
                producto = Producto(nombre, categoria, precio, cantidad)
                inventario.agregar_producto(producto)
            except ValueError:
                print("Precio o cantidad inválidos. Intente nuevamente.")
                
        elif opcion == '2':
            nombre = input("Ingrese el nombre del producto a actualizar: ")
            try:
                precio = input("Ingrese el nuevo precio (deje vacío si no desea cambiarlo): ")
                cantidad = input("Ingrese la nueva cantidad (deje vacío si no desea cambiarla): ")
                precio = float(precio) if precio else None
                cantidad = int(cantidad) if cantidad else None
                inventario.actualizar_producto(nombre, precio, cantidad)
            except ValueError:
                print("Precio o cantidad inválidos. Intente nuevamente.")

        elif opcion == '3':
            nombre = input("Ingrese el nombre del producto a eliminar: ")
            inventario.eliminar_producto(nombre)

        elif opcion == '4':
            print("\nInventario:")
            inventario.mostrar_inventario()

        elif opcion == '5':
            nombre = input("Ingrese el nombre del producto a buscar: ")
            producto = inventario.buscar_producto(nombre)
            if producto:
                print("\nProducto encontrado:")
                print(producto)
            else:
                print("Producto no encontrado.")

        elif opcion == '6':
            print("Saliendo del sistema de inventario.")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

# Ejecutar el menú
if __name__ == '__main__':
    menu()
    
# Añadir una pausa para evitar que el terminal se cierre inmediatamente
input("Presione Enter para salir...")

