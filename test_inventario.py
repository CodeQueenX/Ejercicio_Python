import unittest
from unittest.mock import patch
from inventario import Producto, Inventario

class TestInventario(unittest.TestCase):

    # Probar la adición de un productos
    def setUp(self):
        # Crear un inventario y agregar productos
        self.inventario = Inventario()
        self.inventario.agregar_producto(Producto("Laptop", "Electrónica", 1000, 10))
        self.inventario.agregar_producto(Producto("Celular", "Electrónica", 500, 20))

    # Probar a mostrar el inventario
    def test_mostrar_inventario(self):
        # Usamos patch para capturar lo que se imprime en la salida estándar (stdout)
        with patch('builtins.print') as mocked_print:
            # Llamamos al método que queremos probar
            self.inventario.mostrar_inventario()

            # Capturamos todo lo que fue impreso
            printed_output = [call[0][0] for call in mocked_print.call_args_list]

            # Verificamos si las cadenas correctas están en la salida
            self.assertIn("Laptop - Categoría: Electrónica, Precio: 1000, Cantidad: 10", printed_output)
            self.assertIn("Celular - Categoría: Electrónica, Precio: 500, Cantidad: 20", printed_output)

    # Probar la adición de un producto duplicado
    def test_agregar_producto_duplicado(self):
        # Intentamos agregar un producto que ya existe
        producto_duplicado = Producto("Laptop", "Electrónica", 1000, 10)
        self.inventario.agregar_producto(producto_duplicado)  # Producto ya agregado
        # Verificamos si la cantidad sigue siendo 10 (no se debería haber agregado de nuevo)
        self.assertEqual(len(self.inventario._productos), 2)
        self.assertEqual(self.inventario._productos[0].get_cantidad(), 10)
        
    # Probar la actualización de precio y cantidad de un producto
    def test_actualizar_producto(self):
        # Actualizamos el precio y la cantidad del producto "Laptop"
        self.inventario.actualizar_producto("Laptop", nuevo_precio=1200, nueva_cantidad=15)
        
        # Verificamos que los valores se hayan actualizado correctamente
        producto = self.inventario.buscar_producto("Laptop")
        self.assertEqual(producto.get_precio(), 1200)
        self.assertEqual(producto.get_cantidad(), 15)
        
    # Probar la eliminación de un producto    
    def test_eliminar_producto(self):
        # Eliminamos el producto "Celular"
        self.inventario.eliminar_producto("Celular")
        
        # Verificamos que el producto ha sido eliminado
        producto = self.inventario.buscar_producto("Celular")
        self.assertIsNone(producto)
        self.assertEqual(len(self.inventario._productos), 1)  # Solo queda un producto

    # Probar la búsqueda de un producto
    def test_buscar_producto(self):
        # Buscamos el producto "Laptop"
        producto = self.inventario.buscar_producto("Laptop")
        
        # Verificamos que el producto encontrado es el correcto
        self.assertEqual(producto.get_nombre(), "Laptop")
        self.assertEqual(producto.get_categoria(), "Electrónica")
        self.assertEqual(producto.get_precio(), 1000)
        self.assertEqual(producto.get_cantidad(), 10)
        
        # Verificamos que un producto no encontrado devuelva None
        producto_no_encontrado = self.inventario.buscar_producto("Televisor")
        self.assertIsNone(producto_no_encontrado)

    # Probar la lista de productos cuando el inventario está vacío
    def test_mostrar_inventario_vacio(self):
        # Creamos un inventario vacío
        inventario_vacio = Inventario()
        
        # Usamos patch para capturar lo que se imprime
        with patch('builtins.print') as mocked_print:
            inventario_vacio.mostrar_inventario()
            printed_output = [call[0][0] for call in mocked_print.call_args_list]
            
            # Verificamos que el mensaje de inventario vacío se muestra
            self.assertIn("El inventario está vacío.", printed_output)
    
    # Probar la actualización de un producto con valores inválidos
    def test_actualizar_producto_valores_invalidos(self):
        # Crear el producto con un precio válido, cantidad válida y categoria
        producto = Producto(nombre="Laptop", precio=1000, cantidad=10, categoria="Electrónica")
        self.inventario.agregar_producto(producto)
        
        # Intentar actualizar con un precio negativo
        with self.assertRaises(ValueError) as context:
            self.inventario.actualizar_producto("Laptop", nuevo_precio=-100, nueva_cantidad=15)
            
        # Verificar que el mensaje de error es el esperado
        self.assertEqual(str(context.exception), "El precio debe ser mayor que 0.")
    
    # Probar la adición de un producto con un nombre vacío
    def test_agregar_producto_nombre_vacio(self):
        # Crear un producto con nombre vacío
        producto_vacio = Producto(nombre="", precio=1000, cantidad=10, categoria="Electrónica")
        
        # Intentar agregar el producto con nombre vacío
        with self.assertRaises(ValueError) as context:
            self.inventario.agregar_producto(producto_vacio)
            
        # Verificar que el mensaje de error es el esperado
        self.assertEqual(str(context.exception), "El nombre del producto no puede estar vacío.")

    # Probar la adición de un producto con una cantidad negativa
    def test_agregar_producto_cantidad_negativa(self):
        # Intentamos agregar un producto con cantidad negativa
        producto = Producto("Tablet", "Electrónica", 300, -5)
        
        # Verificamos que se lance el ValueError
        with self.assertRaises(ValueError) as context:
            self.inventario.agregar_producto(producto)
            
        # Verificar que el mensaje de error es el esperado
        self.assertEqual(str(context.exception), "La cantidad debe ser mayor o igual a 0.")

if __name__ == '__main__':
    # Usar unittest directamente sin 'input' al final, pero invocar manualmente la pausa
    unittest.TextTestRunner().run(unittest.defaultTestLoader.loadTestsFromTestCase(TestInventario))
    input("Presiona Enter para salir...")  # Pausa al final para evitar que la ventana se cierre