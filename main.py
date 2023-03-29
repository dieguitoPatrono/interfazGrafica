import tkinter as tk
from tkinter import PhotoImage
from tkinter import *
# conectar a la base de datos en postgres
import psycopg2 as psycopg2
import ventana as ventana


def conectar_bd():
    # Conectar a la base de datos
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="agentes",
        user="konecta",
        password="11051994"
    )

    # Crear un cursor
    cur = conn.cursor()

    # Devolver la conexión y el cursor
    return conn, cur


def agregar_persona():
    # Obtener los valores de los campos de entrada
    id = id_entry.get().upper()
    nombre = nombre_entry.get().upper()
    apellidos = apellidos_entry.get().upper()
    dni = dni_entry.get().upper()
    horas_contratadas = horas_entry.get()
    mail = mail_entry.get().upper()

    # Conectar a la base de datos
    conn, cur = conectar_bd()

    # Ejecutar la consulta para agregar la persona
    cur.execute(
        "INSERT INTO agente (meta, nombre, apellidos, dni, horas_contratadas, mail) VALUES (%s, %s, %s, %s, %s, %s)",
        (id, nombre, apellidos, dni, horas_contratadas, mail))

    # Confirmar la transacción
    conn.commit()

    # Cerrar el cursor y la conexión
    cur.close()
    conn.close()

    # Actualizar la etiqueta de estado
    status_label.config(text="Se agregó la persona con éxito.")


def eliminar_persona():
    id_eliminar = eliminar_entry.get().upper()
    # Conectar a la base de datos
    conn, cur = conectar_bd()
    # Consultar si el ID existe en la base de datos
    cur.execute("SELECT * FROM agente WHERE meta=%s", (id_eliminar,))
    persona = cur.fetchone()

    if persona is not None:
        # Si el ID existe, eliminar la persona de la base de datos
        cur.execute("DELETE FROM agente WHERE meta=%s", (id_eliminar,))
        conn.commit()
        status_label.config(text="Persona eliminada con éxito.")
        # Borrar los campos de entrada
        eliminar_entry.delete(0, tk.END)
        id_entry.delete(0, tk.END)
        nombre_entry.delete(0, tk.END)
        apellidos_entry.delete(0, tk.END)
        dni_entry.delete(0, tk.END)
        horas_entry.delete(0, tk.END)
        mail_entry.delete(0, tk.END)
    else:
        # Si el ID no existe, mostrar un mensaje de error
        status_label.config(text="La persona con ese ID no existe en la base de datos.")


root = tk.Tk()
root.iconbitmap("carpeta.ico")
root.wm_iconbitmap("carpeta.ico")
root.title("Base De Datos Agentes")
root.resizable(False, False)
# Crear los campos de entrada

# Cargar la imagen
logo = PhotoImage(file="LogoKBIOS.png")
logo = logo.subsample(2, 2)
logo_label = Label(root, image=logo)

id_label = tk.Label(root, text="ID:")
id_entry = tk.Entry(root)
nombre_label = tk.Label(root, text="Nombre:")
nombre_entry = tk.Entry(root)
apellidos_label = tk.Label(root, text="Apellidos:")
apellidos_entry = tk.Entry(root)
dni_label = tk.Label(root, text="DNI:")
dni_entry = tk.Entry(root)
horas_label = tk.Label(root, text="Horas contratadas:")
horas_entry = tk.Entry(root)
mail_label = tk.Label(root, text="Mail:")
mail_entry = tk.Entry(root)
eliminar_label = tk.Label(root, text="ID de la persona a eliminar:")
eliminar_entry = tk.Entry(root)

# Crear el botón para agregar la persona
agregar_button = tk.Button(root, text="Agregar", command=agregar_persona)
eliminar_button = tk.Button(root, text="Eliminar persona", command=eliminar_persona)

# Crear una etiqueta para mostrar el estado de la operación
status_label = tk.Label(root, text="")

# Ubicar los elementos en la ventana
logo_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="w")
id_label.grid(row=1, column=0, sticky="w", padx=10, pady=10)
id_entry.grid(row=1, column=1, padx=10, pady=10)
nombre_label.grid(row=2, column=0, sticky="w", padx=10, pady=10)
nombre_entry.grid(row=2, column=1, padx=10, pady=10)
apellidos_label.grid(row=3, column=0, sticky="w", padx=10, pady=10)
apellidos_entry.grid(row=3, column=1, padx=10, pady=10)
dni_label.grid(row=4, column=0, sticky="w", padx=10, pady=10)
dni_entry.grid(row=4, column=1, padx=10, pady=10)
horas_label.grid(row=5, column=0, sticky="w", padx=10, pady=10)
horas_entry.grid(row=5, column=1, padx=10, pady=10)
mail_label.grid(row=6, column=0, sticky="w", padx=10, pady=10)
mail_entry.grid(row=6, column=1, padx=10, pady=10)
eliminar_label.grid(row=7, column=0, sticky="w", padx=10, pady=10)
eliminar_entry.grid(row=7, column=1, padx=10, pady=10)

# botones
agregar_button.grid(row=8, column=0, columnspan=2, padx=10, pady=10)
eliminar_button.grid(row=8, column=1, padx=10, pady=10)
status_label.grid(row=9, column=0, columnspan=2, padx=10, pady=10)

conectar_bd()
root.geometry("370x400+0+0")
root.mainloop()
