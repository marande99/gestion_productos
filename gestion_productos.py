# Sistema de Gestión de Productos

productos = []

def cargar_datos():
    """Cargar datos desde el archivo productos.txt si existe."""
    try:
        with open("productos.txt", "r") as file:
            for line in file:
                nombre, precio, cantidad = line.strip().split(", ")
                productos.append({
                    "nombre": nombre,
                    "precio": float(precio),
                    "cantidad": int(cantidad)
                })
        print("Datos cargados correctamente.")
    except FileNotFoundError:
        print("Archivo de productos no encontrado. Se creará uno nuevo al guardar.")
    except ValueError:
        print("Error al cargar datos. Verifique el formato de productos.txt.")

def guardar_datos():
    """Guardar datos en el archivo productos.txt."""
    with open("productos.txt", "w") as file:
        for producto in productos:
            file.write(f"{producto['nombre']}, {producto['precio']}, {producto['cantidad']}\n")
    print("Datos guardados correctamente.")

def añadir_producto():
    """Añadir un nuevo producto a la lista."""
    nombre = input("Nombre del producto: ")
    while True:
        try:
            precio = float(input("Precio del producto: "))
            cantidad = int(input("Cantidad del producto: "))
            productos.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
            print(f"Producto '{nombre}' añadido correctamente.")
            break
        except ValueError:
            print("Error: Precio y cantidad deben ser numéricos.")

def ver_productos():
    """Mostrar todos los productos en la lista."""
    if productos:
        print("\nLista de productos:")
        for producto in productos:
            print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")
    else:
        print("No hay productos para mostrar.")

def actualizar_producto():
    """Actualizar los detalles de un producto existente."""
    nombre = input("Nombre del producto a actualizar: ")
    for producto in productos:
        if producto["nombre"].lower() == nombre.lower():
            try:
                nuevo_nombre = input("Nuevo nombre (o presiona Enter para mantener el actual): ")
                nuevo_precio = input("Nuevo precio (o presiona Enter para mantener el actual): ")
                nueva_cantidad = input("Nueva cantidad (o presiona Enter para mantener el actual): ")
                
                if nuevo_nombre:
                    producto["nombre"] = nuevo_nombre
                if nuevo_precio:
                    producto["precio"] = float(nuevo_precio)
                if nueva_cantidad:
                    producto["cantidad"] = int(nueva_cantidad)
                
                print(f"Producto '{nombre}' actualizado correctamente.")
                return
            except ValueError:
                print("Error: Precio y cantidad deben ser numéricos.")
                return
    print(f"Producto '{nombre}' no encontrado.")

def eliminar_producto():
    """Eliminar un producto de la lista basado en el nombre."""
    nombre = input("Nombre del producto a eliminar: ")
    for producto in productos:
        if producto["nombre"].lower() == nombre.lower():
            productos.remove(producto)
            print(f"Producto '{nombre}' eliminado correctamente.")
            return
    print(f"Producto '{nombre}' no encontrado.")

def menu():
    cargar_datos()  # Cargar datos al inicio del programa

    while True:
        print("\nMenú de Gestión de Productos")
        print("1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            añadir_producto()
        elif opcion == '2':
            ver_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            guardar_datos()
            break
        else:
            print("Por favor, selecciona una opción válida.")

# Ejecutar el menú principal
menu()
