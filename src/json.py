import json
import os
# --------------------------
# Variables con las rutas de los archivos JSON
# --------------------------

# Archivo origen: contiene los datos iniciales
archivo_origen = "src/otros/datos_usuarios_orig.json"

# Archivo destino: es el que se va a modificar con el programa
archivo_destino = "src/otros/datos_usuarios.json"

def mostrar_datos(datos):
    if "usuarios" not in datos or datos ["usuarios"] == []:
        print("El archivo json no contiene usuarios!")
        return 



    print("\n--- Contenido Actual del JSON ---")
    for "usuario" in datos["usarios"]:
        print("ID:", usuario["id"], ", Nombre:", usuario["nombre"], ", Edad:", usuario["edad"])
    print("--- Fin del Contenido ---")


def inicializar_datos():
    try:
        with open(archivo_origen, "r") as origen:
            datos = json.load(origen)
        with open(archivo_destino, "w") as destino:
            json.dump(datos, destino, indent = 4)
        print(f"Datos inicializados desde '{archivo_origen}' a '{archivo_destino}'.")
    except FileNotFoundError:
        print(f"ERROR: El archivo origen '{archivo_origen}' no existe. No se realizó la copia.")
    except json.JSONDecodeError:
        print(f"ERROR: El archivo origen '{archivo_origen}' tiene un formato JSON inválido.")
    except Exception as e:
        print(f"ERROR al inicializar datos: {e}")



def cargar_json(nombre_fichero: str) -> dict:
    """
    Carga el contenido de un fichero JSON.

    Args:
        nombre_fichero (str): Nombre del fichero JSON.

    Returns:
        (dict): Contenido del archivo JSON como un diccionario, o None si no se pudo cargar.
    """
    try:
        with open(nombre_fichero, "r") as archivo:
            return json.load(archivo)

    except FileNotFoundError:
        print(f"*ERROR* El archivo {nombre_fichero} no existe.")

    except json.JSONDecodeError:
        print("*ERROR* El archivo JSON tiene un formato incorrecto.")

    except Exception as e:
        print(f"*ERROR* Problemas al cargar los datos {e}.")

    return None


def guardar_json(nombre_fichero: str, datos: dict):
    """
    Guarda los datos en un fichero JSON.

    Args:
        nombre_fichero (str): Nombre del fichero JSON.
        datos (dict): Datos a guardar.
    """
    try:
        with open(nombre_fichero, "w") as archivo:
            json.dump(datos, archivo, indent = 4)

    except PermissionError:
        print(f"*ERROR* No tienes permisos para escribir en el archivo '{nombre_fichero}'.")

    except TypeError as e:
        print(f"*ERROR* Los datos no son serializables a JSON. Detalle: {e}")        

    except Exception as e:
        print(f"*ERROR* Problemas al guardar los datos: {e}")


def actualizar_usuario(datos: dict, id_usuario: int, nueva_edad: int):
    """
    Actualiza la edad de un usuario dado su ID.

    Args:
        datos (dict): Diccionario con los datos actuales.
        id_usuario (int): ID del usuario a actualizar.
        nueva_edad (int): Nueva edad del usuario.
    """
    for usuario in datos["usuarios"]:
        if usuario["id"] == id_usuario:
            usuario["edad"] = nueva_edad
            print(f"Usuario con ID {id_usuario} actualizado.")
            return

    print(f"Usuario con ID {id_usuario} no encontrado.")


def insertar_usuario(datos: dict, nuevo_usuario: dict):
    """
    Inserta un nuevo usuario.

    Args:
        datos (dict): Diccionario con los datos actuales.
        nuevo_usuario (dict): Diccionario con los datos del nuevo usuario.
    """
    datos["usuarios"].append(nuevo_usuario)
    print(f"Usuario {nuevo_usuario['nombre']} añadido con éxito.")


def eliminar_usuario(datos: dict, id_usuario: int):
    """
    Elimina un usuario dado su ID.

    Args:
        datos (dict): Diccionario con los datos actuales.
        id_usuario (int): ID del usuario a eliminar.
    """
    for usuario in datos["usuarios"]:
        if usuario["id"] == id_usuario:
            datos["usuarios"].remove(usuario)
            print(f"Usuario con ID {id_usuario} eliminado.")
            return

    print(f"Usuario con ID {id_usuario} no encontrado.")


def main():
    os.system("cls" if os.name == "nt" else "clear")

    inicializar_datos(archivo_origen, archivo_destino)
    
    # 1. Cargar datos desde el fichero JSON
    datos = cargar_json(archivo_destino)

    if datos is None:
        # Inicializamos datos vacíos si hay error
        datos = {"usuarios": []}

    mostrar_datos(datos)
    input("Presione una tecla para continuar . . .")

    # 2. Actualizar la edad de un usuario
    actualizar_usuario(datos, id_usuario=1, nueva_edad=31)
    mostrar_datos(datos)
    input("Presione una tecla para continuar . . .")

    # 3. Insertar un nuevo usuario
    nuevo_usuario = {"id": 3, "nombre": "Pedro", "edad": 40}
    insertar_usuario(datos, nuevo_usuario)
    mostrar_datos(datos)
    input("Presione una tecla para continuar . . .")
    
    # 4. Eliminar un usuario
    eliminar_usuario(datos, id_usuario=2)
    mostrar_datos(datos)
    input("Presione una tecla para continuar . . .")

    # 5. Guardar los datos de nuevo en el fichero JSON
    guardar_json(archivo_destino, datos)

    print("Operaciones completadas. Archivo actualizado.\n")


if __name__ == "__main__":
    main()