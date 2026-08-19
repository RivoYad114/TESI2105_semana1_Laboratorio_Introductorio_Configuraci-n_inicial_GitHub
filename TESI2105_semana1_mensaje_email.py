print("--------JCOB_Mail--------")

def guardar_mensaje():
    nombre = input("Ingrese su nombre: ")
    fecha = input("Ingrese la fecha: ")
    mensaje = input("Ingrese su mensaje: ")

    with open("mensajes.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"Usuario: {nombre}\n")
        archivo.write(f"Fecha: {fecha}\n")
        archivo.write(f"Mensaje: {mensaje}\n")
        archivo.write("-" * 30 + "\n")

    print("¡Mensaje guardado correctamente!")

if __name__ == "__main__":
    guardar_mensaje()