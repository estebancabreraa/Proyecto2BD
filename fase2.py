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

    #NIT
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
