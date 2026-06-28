import json
import requests
import csv

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
def obtener_empleados_api():
    url = "https://6a40ba581ff1d27becc0eb5c.mockapi.io/empleados"

    try:
        respuesta = requests.get(url)

        if respuesta.status_code == 200:
            usuarios = respuesta.json()

            print("\n===== EMPLEADOS OBTENIDOS DESDE LA API =====\n")

            for usuario in usuarios:
                print(f"ID      : {usuario.get('id', usuario.get('ID', ''))}")
                print(f"Nombre  : {usuario['nombre']}")
                print(f"Cargo   : {usuario['cargo']}")
                print(f"Correo  : {usuario['correo']}")
                print(f"Ciudad  : {usuario['ciudad']}")
                print(f"Estado  : {usuario['estado']}")
                print("-" * 40)

        else:
            print(f"No fue posible obtener los datos. Código: {respuesta.status_code}")

    except Exception as e:
        print("Error al conectar con la API:", e)

def exportar_csv():

    with open("reportes/empleados.csv", "w", newline="", encoding="utf-8") as archivo:

        escritor = csv.writer(archivo)

        escritor.writerow([
            "ID",
            "Nombre",
            "Cargo",
            "Correo",
            "Estado"
        ])

        for empleado in empleados:
            escritor.writerow([
                empleado["id"],
                empleado["nombre"],
                empleado["cargo"],
                empleado["correo"],
                empleado["estado"]
            ])

    print("\n✅ Reporte generado correctamente.")
    print("Ubicación: reportes/empleados.csv")
while True:

    print("\n==============================")
    print(" SISTEMA DE GESTIÓN DEL PERSONAL TI")
    print("==============================")
    print("1. Ver empleados")
    print("2. Buscar empleado")
    print("3. Contar empleados")
    print("4. obtener empleados desde la API")
    print("5. Exportar reporte CSV")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        mostrar_empleados()

    elif opcion == "2":
        buscar_empleado()

    elif opcion == "3":
        contar_empleados()

    elif opcion == "4":
        obtener_empleados_api()

    elif opcion == "5":
         exportar_csv()

    elif opcion == "6":
         print("Hasta Luego.")
         break
    else:
        print("Opción no válida.")

