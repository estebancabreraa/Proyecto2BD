################################################################################
#                             PROYECTO 2/FASE 2                                #
################################################################################
#BASES DE DATOS
#BIDKAR POJOY
#SECCION 10

#INTEGRANTES:
#Esteban Cabrera - 17781
#Kevin Macario - 17163
#Raul Monzon - 17014

#FECHA DE ENTREGA: 16/05/2019

import tkinter as tk


#Funciones
def mostrarVentanaClientes():
    ventanaClientes = tk.Tk()
    ventanaClientes.title("CLIENTES")
    ventanaClientes.geometry("800x600")
    ventanaClientes.configure(background="dodger blue")

def mostrarVentanaProductos():
    ventanaClientes = tk.Tk()
    ventanaClientes.title("PRODUCTOS")
    ventanaClientes.geometry("800x600")
    ventanaClientes.configure(background="dodger blue")

def mostrarVentanaVentas():
    ventanaClientes = tk.Tk()
    ventanaClientes.title("VENTAS")
    ventanaClientes.geometry("800x600")
    ventanaClientes.configure(background="dodger blue")


################################################################################
#                                    MAIN                                      #
################################################################################
#GUI
gui = tk.Tk()
gui.title("TIENDA LA BENDICION")
gui.geometry('800x600')
gui.configure(background="dodger blue")

#LABELS
label1 = tk.Label(gui, text="TIENDA LA BENDICION", fg="black")
label1.pack()

#Buttons
button1 = tk.Button(gui, text="Clientes", command=mostrarVentanaClientes)
button1.pack()
button2 = tk.Button(gui, text="Productos", command=mostrarVentanaProductos)
button2.pack()
button3 = tk.Button(gui, text="Ventas", command=mostrarVentanaVentas)
button3.pack()

gui.mainloop()
