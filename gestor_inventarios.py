import sqlite3
from tkinter import Tk, Label, Entry, Button, Listbox, END

# Conexión a la base de datos
def conectar_db():
    conn = sqlite3.connect("inventario.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            cantidad INTEGER NOT NULL,
            precio REAL NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# Agregar producto
def agregar_producto():
    conn = sqlite3.connect("inventario.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO productos (nombre, cantidad, precio) VALUES (?, ?, ?)",
                   (entrada_nombre.get(), entrada_cantidad.get(), entrada_precio.get()))
    conn.commit()
    conn.close()
    mostrar_productos()

# Mostrar productos
def mostrar_productos():
    conn = sqlite3.connect("inventario.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    conn.close()
    lista.delete(0, END)
    for producto in productos:
        lista.insert(END, f"{producto[0]} - {producto[1]} | Cantidad: {producto[2]} | Precio: ${producto[3]}")

# Interfaz gráfica
ventana = Tk()
ventana.title("Gestor de Inventarios")

Label(ventana, text="Nombre:").grid(row=0, column=0)
entrada_nombre = Entry(ventana)
entrada_nombre.grid(row=0, column=1)

Label(ventana, text="Cantidad:").grid(row=1, column=0)
entrada_cantidad = Entry(ventana)
entrada_cantidad.grid(row=1, column=1)

Label(ventana, text="Precio:").grid(row=2, column=0)
entrada_precio = Entry(ventana)
entrada_precio.grid(row=2, column=1)

Button(ventana, text="Agregar", command=agregar_producto).grid(row=3, column=0, columnspan=2)

lista = Listbox(ventana, width=50)
lista.grid(row=4, column=0, columnspan=2)
mostrar_productos()

conectar_db()
ventana.mainloop()
