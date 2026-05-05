import tkinter as tk
from tkinter import messagebox
from gui.componentes import boton_sidebar, limpiar_frame

#COLORES PARA USAR
BG = "#121212"
SIDEBAR = "#1f1f1f"
CARD = "#1e1e1e"
FG = "#ffffff"
ACCENT = "#4CAF50"

#IMPORTS
try:
    from core.cliente import Cliente
    from core.reserva import Reserva
except:
    #Clases Temporales
    class Cliente:
        def __init__(self, nombre):
            if nombre == "":
                raise ValueError("Nombre vacío")
            self.nombre = nombre

    class Reserva:
        def __init__(self, cliente, fecha):
            if fecha == "":
                raise ValueError("Fecha vacía")
            self.cliente = cliente
            self.fecha = fecha

#APP PRINCIPAL
def iniciar_app():
    ventana = tk.Tk()
    ventana.title("Sistema de Gestión")
    ventana.geometry("800x500")
    ventana.configure(bg=BG)

    #BarraLateral
    sidebar = tk.Frame(ventana, bg=SIDEBAR, width=200)
    sidebar.pack(side="left", fill="y")

    #Contenido
    contenido = tk.Frame(ventana, bg=BG)
    contenido.pack(side="right", expand=True, fill="both")

    tk.Label(
        sidebar,
        text="MENÚ",
        bg=SIDEBAR,
        fg=FG,
        font=("Arial", 14, "bold")
    ).pack(pady=20)

    boton_sidebar(sidebar, "Clientes", lambda: vista_clientes(contenido)).pack(fill="x")
    boton_sidebar(sidebar, "Reservas", lambda: vista_reservas(contenido)).pack(fill="x")

    ventana.mainloop()


#VISTA DE CLIENTES
def vista_clientes(frame):
    limpiar_frame(frame)

    tk.Label(
        frame,
        text="Gestión de Clientes",
        bg=BG,
        fg=FG,
        font=("Arial", 16, "bold")
    ).pack(pady=20)

    card = tk.Frame(frame, bg=CARD, padx=20, pady=20)
    card.pack(pady=10)

    tk.Label(card, text="Nombre", bg=CARD, fg=FG).grid(row=0, column=0, pady=5)
    entrada = tk.Entry(card)
    entrada.grid(row=0, column=1, pady=5)

    def guardar():
        try:
            cliente = Cliente(entrada.get())
            messagebox.showinfo("Éxito", f"{cliente.nombre} guardado")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    tk.Button(
        frame,
        text="Guardar Cliente",
        bg=ACCENT,
        fg="white",
        relief="flat",
        padx=10,
        pady=5,
        command=guardar
    ).pack(pady=15)


#VISTA DE RESERVAS
def vista_reservas(frame):
    limpiar_frame(frame)

    tk.Label(
        frame,
        text="Gestión de Reservas",
        bg=BG,
        fg=FG,
        font=("Arial", 16, "bold")
    ).pack(pady=20)

    card = tk.Frame(frame, bg=CARD, padx=20, pady=20)
    card.pack(pady=10)

    tk.Label(card, text="Cliente", bg=CARD, fg=FG).grid(row=0, column=0, pady=5)
    entrada_cliente = tk.Entry(card)
    entrada_cliente.grid(row=0, column=1, pady=5)

    tk.Label(card, text="Fecha", bg=CARD, fg=FG).grid(row=1, column=0, pady=5)
    entrada_fecha = tk.Entry(card)
    entrada_fecha.grid(row=1, column=1, pady=5)

    def guardar():
        try:
            reserva = Reserva(
                entrada_cliente.get(),
                entrada_fecha.get()
            )
            messagebox.showinfo("Éxito", "Reserva creada")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    tk.Button(
        frame,
        text="Guardar Reserva",
        bg=ACCENT,
        fg="white",
        relief="flat",
        padx=10,
        pady=5,
        command=guardar
    ).pack(pady=15)
