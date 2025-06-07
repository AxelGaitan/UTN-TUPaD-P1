
# Trabajo práctico recuperatorio - Programación I
# alumno: Axel Gaitan
# este programa simula una gestion simple de stock de productos.

# Inicio las listas vacias
productos = []
cantidades = []

salir = False

# Bucle principal del menu
while not salir:
    print(" Menu de Gestión de Stock ")
    print("1. Agregar producto")
    print("2. Ver productos agotados")
    print("3. Actualizar stock")
    print("4. Ver todos los productos")
    print("5.Salir")

    opcion = input("Elegi una opcion(1-5):")

    if opcion == "1":
        nombre = input("Nombre del producto:")
        try:
            cantidad = int(input("Cantidad en stock: "))
            productos.append(nombre)
            cantidades.append(cantidad)
            print("Producto agregado correctamente")
        except:
            print("Por favor ingresá un número valido")

    elif opcion == "2":
        print("productos agotados:")
        hay_agotados = False
        for i in range(len(cantidades)):
            if cantidades[i] == 0:
                print("-", productos[i])
                hay_agotados = True
        if not hay_agotados:
            print("no hay productos agotados.")

    elif opcion == "3":
        nombre = input("nombre del producto a actualizar:")
        if nombre in productos:
            index = productos.index(nombre)
            try:
                nueva_cantidad = int(input("nueva cantidad:"))
                cantidades[index] = nueva_cantidad
                print("stock actualizado.")
            except:
                print("por favor ingresá un número válido.")
        else:
            print("Producto no encontrado.")

    elif opcion == "4":
        print("listado completo de productos:")
        for i in range(len(productos)):
            print(f"{productos[i]} - {cantidades[i]} unidades")

    elif opcion == "5":
        print("saliendo del sistema... Gracias!!")
        salir = True

    else:
        print("opción invalida. Intentá de nuevo.")