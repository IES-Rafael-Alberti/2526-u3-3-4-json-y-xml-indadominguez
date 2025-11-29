import xml.etree.ElementTree as ET
import os

# --------------------------
# Variables con las rutas de los archivos XML
# --------------------------
archivo_origen = "src/otros/datos_usuarios_orig.xml"
archivo_destino = "src/otros/datos_usuarios.xml"

#usuario: nombre: "pedro", edad:"40", habilidades: ["html", "css"],  activo: Falso

def mostrar_datos(tree):
    """
    Muestra los datos de los usuarios contenidos en el árbol XML.
    """
    usuarios = tree.findall("usuario")

    if not usuarios:
        print("ERROR: No hay usuarios en el archivo XML.")
        return

    print("\n--- Contenido Actual del XML ---")
    for usuario in usuarios:
        print(
            f"ID: {usuario.find('id').text}, "
            f"Nombre: {usuario.find('nombre').text}, "
            f"Edad: {usuario.find('edad').text}"
        )
    print("--- Fin del Contenido ---")


def crear_arbol(nodo_raiz):
    """
    Crea un árbol XML vacío con un nodo raíz especificado.
    """
    raiz = ET.Element(nodo_raiz)
    return ET.ElementTree(raiz)


def inicializar_datos():
    """
    Copia los datos del archivo origen al archivo destino sin usar shutil.
    """
    try:
        with open(archivo_origen, "r", encoding="utf-8") as origen:
            contenido = origen.read()

        with open(archivo_destino, "w", encoding="utf-8") as destino:
            destino.write(contenido)

        print(f"Datos inicializados desde '{archivo_origen}' a '{archivo_destino}'.")
    
    except FileNotFoundError:
        print(f"ERROR: El archivo origen '{archivo_origen}' no existe. No se realizó la copia.")
    
    except Exception as e:
        print(f"ERROR al inicializar datos: {e}")


def cargar_xml(nombre_fichero):
    """
    Carga un archivo XML y devuelve su árbol.
    """
    try:
        return ET.parse(nombre_fichero)
    except FileNotFoundError:
        print(f"*ERROR* El archivo {nombre_fichero} no existe.")
    except ET.ParseError:
        print(f"*ERROR* El archivo XML tiene un formato incorrecto.")
    except Exception as e:
        print(f"*ERROR* Problemas al cargar los datos: {e}")
    return None


def guardar_xml(tree, nombre_fichero):
    """
    Guarda el árbol XML en un archivo.
    """
    try:
        tree.write(nombre_fichero, encoding="utf-8", xml_declaration=True)
    except Exception as e:
        print(f"*ERROR* Problemas al guardar los datos: {e}")


def actualizar_usuario(tree, id_usuario, nueva_edad):
    """
    Actualiza la edad de un usuario dado su ID.
    """
    for usuario in tree.findall("usuario"):
        if usuario.find("id").text == str(id_usuario):
            usuario.find("edad").text = str(nueva_edad)
            print(f"Usuario con ID {id_usuario} actualizado.")
            return
    print(f"Usuario con ID {id_usuario} no encontrado.")


def insertar_usuario(tree, id_usuario, nombre, edad):
    """
    Inserta un nuevo usuario en el árbol XML.
    """
    nuevo = ET.Element("usuario")
    ET.SubElement(nuevo, "id").text = str(id_usuario)
    ET.SubElement(nuevo, "nombre").text = nombre
    ET.SubElement(nuevo, "edad").text = str(edad)
    tree.getroot().append(nuevo)
    print(f"Usuario {nombre} añadido con éxito.")


def eliminar_usuario(tree, id_usuario):
    """
    Elimina un usuario del árbol XML dado su ID.
    """
    for usuario in tree.findall("usuario"):
        if usuario.find("id").text == str(id_usuario):
            tree.getroot().remove(usuario)
            print(f"Usuario con ID {id_usuario} eliminado.")
            return
    print(f"Usuario con ID {id_usuario} no encontrado.")



def main():
    os.system("cls" if os.name == "nt" else "clear")

    # Inicializamos datos copiando desde el archivo origen
    inicializar_datos()

    # Cargamos el XML desde el archivo destino
    tree = cargar_xml(archivo_destino)
    if tree is None:
        # Inicializamos datos vacíos si hay error
        tree = crear_arbol("usuarios")

    # Mostramos el contenido inicial
    mostrar_datos(tree)
    input("Presione una tecla para continuar . . .\n")

    # Actualizar la edad de un usuario
    actualizar_usuario(tree, id_usuario=1, nueva_edad=31)
    mostrar_datos(tree)
    input("Presione una tecla para continuar . . .\n")

    # Insertar un nuevo usuario
    insertar_usuario(tree, id_usuario=3, nombre="Pedro", edad=40)
    mostrar_datos(tree)
    input("Presione una tecla para continuar . . .\n")

    # Eliminar un usuario
    eliminar_usuario(tree, id_usuario=2)
    mostrar_datos(tree)
    input("Presione una tecla para continuar . . .\n")

    # Guardar los cambios en el archivo XML
    guardar_xml(tree, archivo_destino)
    print("Operaciones completadas. Archivo actualizado.\n")


if __name__ == "__main__":
    main()
