import json


with open("datos/empleados.json", "r", encoding="utf-8") as archivo:
    empleados = json.load(archivo)

def mostrar_empleados():
    print("\n===== LISTA DE EMPLEADOS =====")
    for empleado in empleados:
        print(f"ID: {empleado['id']}")
        print(f"Nombre: {empleado['nombre']}")
        print(f"Cargo: {empleado['cargo']}")
        print(f"Correo: {empleado['correo']}")
        print(f"Estado: {empleado['estado']}")
        print("-" * 40)

def buscar_empleado():
    nombre = input("Ingrese el nombre del empleado: ").lower()

    encontrado = False

    for empleado in empleados:
        if nombre in empleado["nombre"].lower():
            print("\nEmpleado encontrado:")
            print(f"ID: {empleado['id']}")
            print(f"Nombre: {empleado['nombre']}")
            print(f"Cargo: {empleado['cargo']}")
            print(f"Correo: {empleado['correo']}")
            print(f"Estado: {empleado['estado']}")
            encontrado = True

    if not encontrado:
        print("Empleado no encontrado.")


def contar_empleados():
    print(f"\nTotal de empleados: {len(empleados)}")


while True:

    print("\n==============================")
    print(" SISTEMA DE GESTIÓN DEL PERSONAL TI")
    print("==============================")
    print("1. Ver empleados")
    print("2. Buscar empleado")
    print("3. Contar empleados")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        mostrar_empleados()

    elif opcion == "2":
        buscar_empleado()

    elif opcion == "3":
        contar_empleados()

    elif opcion == "4":
        print("Hasta luego.")
        break

    else:
        print("Opción no válida.")
