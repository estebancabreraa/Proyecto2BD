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
import psycopg2
from psycopg2 import Error


#FUNCIONES
def mostrarVentanaClientes():
    ventanaClientes = tk.Tk()
    ventanaClientes.title("CLIENTES")
    ventanaClientes.geometry("800x600")
    ventanaClientes.configure(background="dodger blue")
    
    #LABELS
    label2 = tk.Label(ventanaClientes, text="CLIENTES", bg="dodger blue", fg="black")
    label2.config(font=("Courier", 44), pady=40)
    label2.pack()

    label5 = tk.Label(ventanaClientes, text="REGISTRAR NUEVO CLIENTE", bg="dodger blue", fg="black")
    label5.config(font=("Courier", 24))
    label5.pack(side=tk.TOP, anchor=tk.NW)

    #NOMBRE
    nombre = tk.Frame(ventanaClientes)
    
    label6 = tk.Label(nombre, text="Nombre:", bg="dodger blue", fg="black")
    label6.config(font=("Courier", 12))
    label6.pack(side=tk.LEFT)

    edit1 = tk.Text(nombre, width=30, height=1)
    edit1.pack(side=tk.LEFT)
    nombre.pack(side=tk.TOP, anchor=tk.NW)

    #FECHA NACIMIENTO
    fecha = tk.Frame(ventanaClientes)
    
    label7 = tk.Label(fecha, text="Fecha Nacimiento:", bg="dodger blue", fg="black")
    label7.config(font=("Courier", 12))
    label7.pack(side=tk.LEFT)

    edit2 = tk.Text(fecha, width=15, height=1)
    edit2.pack(side=tk.LEFT)
    
    fecha.pack(side=tk.TOP, anchor=tk.NW)

    #SEXO
    sexo = tk.Frame(ventanaClientes)
    
    label8 = tk.Label(sexo, text="SEXO (M/F):", bg="dodger blue", fg="black")
    label8.config(font=("Courier", 12))
    label8.pack(side=tk.LEFT)

    edit3 = tk.Text(sexo, width=3, height=1)
    edit3.pack(side=tk.LEFT)
    
    sexo.pack(side=tk.TOP, anchor=tk.NW)

    #DIRECCION
    direccionFrame = tk.Frame(ventanaClientes)
    
    label9 = tk.Label(direccionFrame, text="Direccion:", bg="dodger blue", fg="black")
    label9.config(font=("Courier", 12))
    label9.pack(side=tk.LEFT)

    edit4 = tk.Text(direccionFrame, width=60, height=1)
    edit4.pack(side=tk.LEFT)
    
    direccionFrame.pack(side=tk.TOP, anchor=tk.NW)

    #TELEFONO
    telefonoFrame = tk.Frame(ventanaClientes)
    
    label10 = tk.Label(telefonoFrame, text="Telefono:", bg="dodger blue", fg="black")
    label10.config(font=("Courier", 12))
    label10.pack(side=tk.LEFT)

    edit5 = tk.Text(telefonoFrame, width=15, height=1)
    edit5.pack(side=tk.LEFT)
    
    telefonoFrame.pack(side=tk.TOP, anchor=tk.NW)

    #NIT
    nitFrame = tk.Frame(ventanaClientes)
    
    label11 = tk.Label(nitFrame, text="NIT:", bg="dodger blue", fg="black")
    label11.config(font=("Courier", 12))
    label11.pack(side=tk.LEFT)

    edit6 = tk.Text(nitFrame, width=15, height=1)
    edit6.pack(side=tk.LEFT)
    
    nitFrame.pack(side=tk.TOP, anchor=tk.NW)

    #BOTONES
    registrarborrarFrame = tk.Frame(ventanaClientes, bg="dodger blue")
    
    button4 = tk.Button(registrarborrarFrame, text="REGISTRAR", command=mostrarVentanaClientes, bg="green")
    button4.config(font=("Courier", 20))
    button4.pack(side=tk.LEFT, padx=20, pady=10, ipadx=8)

    button5 = tk.Button(registrarborrarFrame, text="BORRAR", command=mostrarVentanaClientes, bg="red")
    button5.config(font=("Courier", 20))
    button5.pack(side=tk.LEFT, padx=20, pady=10, ipadx=8)
    
    registrarborrarFrame.pack(side=tk.TOP, anchor=tk.NW)

def mostrarVentanaProductos():
    ventanaProductos = tk.Tk()
    ventanaProductos.title("PRODUCTOS")
    ventanaProductos.geometry("800x600")
    ventanaProductos.configure(background="dodger blue")

    #LABELS
    label3 = tk.Label(ventanaProductos, text="PRODUCTOS", bg="dodger blue", fg="black")
    label3.config(font=("Courier", 44), pady=40)
    label3.pack()

    label6 = tk.Label(ventanaProductos, text="REGISTRAR NUEVO PRODUCTO", bg="dodger blue", fg="black")
    label6.config(font=("Courier", 24))
    label6.pack(side=tk.TOP, anchor=tk.NW)

    #NOMBRE
    nombreFrame = tk.Frame(ventanaProductos)
    
    label12 = tk.Label(nombreFrame, text="Nombre:", bg="dodger blue", fg="black")
    label12.config(font=("Courier", 12))
    label12.pack(side=tk.LEFT)

    edit7 = tk.Text(nombreFrame, width=30, height=1)
    edit7.pack(side=tk.LEFT)
    nombreFrame.pack(side=tk.TOP, anchor=tk.NW)

    #DESCRIPCION
    descripcionFrame = tk.Frame(ventanaProductos)
    
    label13 = tk.Label(descripcionFrame, text="Descripcion:", bg="dodger blue", fg="black")
    label13.config(font=("Courier", 12))
    label13.pack(side=tk.LEFT)

    edit8 = tk.Text(descripcionFrame, width=70, height=1)
    edit8.pack(side=tk.LEFT)
    
    descripcionFrame.pack(side=tk.TOP, anchor=tk.NW)

    #CATEGORIA
    categoriaFrame = tk.Frame(ventanaProductos)
    
    label14 = tk.Label(categoriaFrame, text="Categoria:", bg="dodger blue", fg="black")
    label14.config(font=("Courier", 12))
    label14.pack(side=tk.LEFT)

    edit9 = tk.Text(categoriaFrame, width=30, height=1)
    edit9.pack(side=tk.LEFT)
    
    categoriaFrame.pack(side=tk.TOP, anchor=tk.NW)

    #PRECIO
    precioFrame = tk.Frame(ventanaProductos)
    
    label15 = tk.Label(precioFrame, text="Precio:", bg="dodger blue", fg="black")
    label15.config(font=("Courier", 12))
    label15.pack(side=tk.LEFT)

    edit10 = tk.Text(precioFrame, width=15, height=1)
    edit10.pack(side=tk.LEFT)
    
    precioFrame.pack(side=tk.TOP, anchor=tk.NW)

    #BOTONES
    registrarborrarFrame = tk.Frame(ventanaProductos, bg="dodger blue")
    
    button6 = tk.Button(registrarborrarFrame, text="REGISTRAR", command=mostrarVentanaClientes, bg="green")
    button6.config(font=("Courier", 20))
    button6.pack(side=tk.LEFT, padx=20, pady=10, ipadx=8)

    button7 = tk.Button(registrarborrarFrame, text="BORRAR", command=mostrarVentanaClientes, bg="red")
    button7.config(font=("Courier", 20))
    button7.pack(side=tk.LEFT, padx=20, pady=10, ipadx=8)
    
    registrarborrarFrame.pack(side=tk.TOP, anchor=tk.NW)

def mostrarVentanaVentas():
    ventanaVentas = tk.Tk()
    ventanaVentas.title("VENTAS")
    ventanaVentas.geometry("800x600")
    ventanaVentas.configure(background="dodger blue")
    
    #LABELS
    label4 = tk.Label(ventanaVentas, text="VENTAS", bg="dodger blue", fg="black")
    label4.config(font=("Courier", 44), pady=40)
    label4.pack()

    label7 = tk.Label(ventanaVentas, text="FACTURAR", bg="dodger blue", fg="black")
    label7.config(font=("Courier", 24))
    label7.pack(side=tk.TOP, anchor=tk.NW)

    #NIT
    nitFrame = tk.Frame(ventanaVentas)
    
    label18 = tk.Label(nitFrame, text="NIT:", bg="dodger blue", fg="black")
    label18.config(font=("Courier", 12))
    label18.pack(side=tk.LEFT)

    edit11 = tk.Text(nitFrame, width=30, height=1)
    edit11.pack(side=tk.LEFT)
    nitFrame.pack(side=tk.TOP, anchor=tk.NW)

    #NOMBRE
    nombreFrame = tk.Frame(ventanaVentas)
    
    label19 = tk.Label(nombreFrame, text="Nombre:", bg="dodger blue", fg="black")
    label19.config(font=("Courier", 12))
    label19.pack(side=tk.LEFT)

    edit12 = tk.Text(nombreFrame, width=30, height=1)
    edit12.pack(side=tk.LEFT)
    nombreFrame.pack(side=tk.TOP, anchor=tk.NW)

    #DESCRIPCION
    descripcionFrame = tk.Frame(ventanaProductos)
    
    label13 = tk.Label(descripcionFrame, text="Descripcion:", bg="dodger blue", fg="black")
    label13.config(font=("Courier", 12))
    label13.pack(side=tk.LEFT)

    edit8 = tk.Text(descripcionFrame, width=70, height=1)
    edit8.pack(side=tk.LEFT)
    
    descripcionFrame.pack(side=tk.TOP, anchor=tk.NW)

    #CATEGORIA
    categoriaFrame = tk.Frame(ventanaProductos)
    
    label14 = tk.Label(categoriaFrame, text="Categoria:", bg="dodger blue", fg="black")
    label14.config(font=("Courier", 12))
    label14.pack(side=tk.LEFT)

    edit9 = tk.Text(categoriaFrame, width=30, height=1)
    edit9.pack(side=tk.LEFT)
    
    categoriaFrame.pack(side=tk.TOP, anchor=tk.NW)

    #PRECIO
    precioFrame = tk.Frame(ventanaProductos)
    
    label15 = tk.Label(precioFrame, text="Precio:", bg="dodger blue", fg="black")
    label15.config(font=("Courier", 12))
    label15.pack(side=tk.LEFT)

    edit10 = tk.Text(precioFrame, width=15, height=1)
    edit10.pack(side=tk.LEFT)
    
    precioFrame.pack(side=tk.TOP, anchor=tk.NW)

    #BOTONES
    registrarborrarFrame = tk.Frame(ventanaProductos, bg="dodger blue")
    
    button6 = tk.Button(registrarborrarFrame, text="REGISTRAR", command=mostrarVentanaClientes, bg="green")
    button6.config(font=("Courier", 20))
    button6.pack(side=tk.LEFT, padx=20, pady=10, ipadx=8)

    button7 = tk.Button(registrarborrarFrame, text="BORRAR", command=mostrarVentanaClientes, bg="red")
    button7.config(font=("Courier", 20))
    button7.pack(side=tk.LEFT, padx=20, pady=10, ipadx=8)
    
    registrarborrarFrame.pack(side=tk.TOP, anchor=tk.NW)
    

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
