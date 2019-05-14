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
    
    #LABELS
    label2 = tk.Label(ventanaClientes, text="CLIENTES", bg="dodger blue", fg="black")
    label2.config(font=("Courier", 44), pady=40)
    label2.pack()

def mostrarVentanaProductos():
    ventanaProductos = tk.Tk()
    ventanaProductos.title("PRODUCTOS")
    ventanaProductos.geometry("800x600")
    ventanaProductos.configure(background="dodger blue")

    #LABELS
    label3 = tk.Label(ventanaProductos, text="PRODUCTOS", bg="dodger blue", fg="black")
    label3.config(font=("Courier", 44), pady=40)
    label3.pack()

def mostrarVentanaVentas():
    ventanaVentas = tk.Tk()
    ventanaVentas.title("VENTAS")
    ventanaVentas.geometry("800x600")
    ventanaVentas.configure(background="dodger blue")
    
    #LABELS
    label4 = tk.Label(ventanaVentas, text="VENTAS", bg="dodger blue", fg="black")
    label4.config(font=("Courier", 44), pady=40)
    label4.pack()


################################################################################
#                                    MAIN                                      #
################################################################################
#GUI
gui = tk.Tk()
gui.title("TIENDA LA BENDICION")
gui.geometry('800x600')
gui.configure(background="dodger blue")

#LABELS
label1 = tk.Label(gui, text="TIENDA LA BENDICION", bg="dodger blue", fg="black")
label1.config(font=("Courier", 44), pady=40)
label1.pack()

#Buttons
button1 = tk.Button(gui, text="Clientes", command=mostrarVentanaClientes)
button1.config(font=("Courier", 20))
button1.pack(pady=10, ipadx=8)
button2 = tk.Button(gui, text="Productos", command=mostrarVentanaProductos)
button2.config(font=("Courier", 20))
button2.pack(pady=10)
button3 = tk.Button(gui, text="Ventas", command=mostrarVentanaVentas)
button3.config(font=("Courier", 20))
button3.pack(pady=10, ipadx=24)

gui.mainloop()
