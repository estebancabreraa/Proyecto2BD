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
from random import randint


'''
Conexion en computadora de Esteban Cabrera:
        user = "postgres",
        password = "esteban1998",
        host = "127.0.0.1",
        port = "5433",
        database = "BDPROYECTO2"
'''

'''
Conexion en computadora de Raul Monzon:
        user = "postgres",
        password = "esteban1998",
        host = "127.0.0.1",
        port = "5432",
        database = "tienda"
'''

def insertarCliente(sexo, nit, telefono, direccion, nombre, fechanac):
    try:
    
        connection = psycopg2.connect(user = "postgres",
                                      password = "esteban1998",
                                      host = "127.0.0.1",
                                      port = "5432",
                                      database = "tienda")
        cursor = connection.cursor()
        
        create_table_query = '''INSERT INTO Cliente(Sexo, Nit, Telefono, Direccion, Nombre, FechaNac) VALUES(%s, %s, %s, %s, %s, %s);'''
        
        cursor.execute(create_table_query, (sexo, nit, telefono, direccion, nombre, fechanac))
        
        connection.commit()
        
        print("Registro exitoso!")
    except (Exception, psycopg2.DatabaseError) as error :
        print ("No se pudo registrar cliente.", error)
    finally:
        #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")

def insertarProducto(nombre, precio, marca, categoria):
    try:

        IDMarca = ''
        IDCategoria = ''
        
        connection = psycopg2.connect(user = "postgres",
                                      password = "esteban1998",
                                      host = "127.0.0.1",
                                      port = "5432",
                                      database = "tienda")
        cursor = connection.cursor()

        create_table_query = '''SELECT * FROM Marca WHERE Nombre = %s;'''

        cursor.execute(create_table_query, (marca.upper(),))

        resultado = cursor.fetchall()

        
        for row in resultado:
            IDMarca = row[1]

        create_table_query = '''SELECT * FROM Categoria WHERE Nombre = %s;'''

        cursor.execute(create_table_query, (categoria.upper(),))

        resultado = cursor.fetchall()

        for row in resultado:
            IDCategoria = row[1]

        IDProducto = randint(100000, 999999)
        print(IDProducto)
        
        create_table_query = '''INSERT INTO Producto(IDProducto, Precio, Nombre, IDMarca, IDCategoria) VALUES(%s, %s, %s, %s, %s);'''
        
        cursor.execute(create_table_query, (IDProducto, precio, nombre, IDMarca, IDCategoria))
        
        connection.commit()
        
        print("Registro exitoso!")
    except (Exception, psycopg2.DatabaseError) as error :
        print ("No se pudo registrar producto.", error)
    finally:
        #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")



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

    def registrarCliente():
        vNombre = edit1.get("1.0",'end-1c')
        vFecha = edit2.get("1.0",'end-1c')
        vSexo = edit3.get("1.0",'end-1c')
        vDireccion = edit4.get("1.0",'end-1c')
        vTelefono = edit5.get("1.0",'end-1c')
        vNit = edit6.get("1.0",'end-1c')

        insertarCliente(vSexo, vNit, vTelefono, vDireccion, vNombre, vFecha)

    #BOTONES
    registrarborrarFrame = tk.Frame(ventanaClientes, bg="dodger blue")
    
    button4 = tk.Button(registrarborrarFrame, text="REGISTRAR", command=registrarCliente, bg="green")
    button4.config(font=("Courier", 20))
    button4.pack(side=tk.LEFT, padx=20, pady=10, ipadx=8)

    button5 = tk.Button(registrarborrarFrame, text="BORRAR", command=registrarCliente, bg="red")
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

    #MARCA
    marcaFrame = tk.Frame(ventanaProductos)
    
    label13 = tk.Label(marcaFrame, text="Marca:", bg="dodger blue", fg="black")
    label13.config(font=("Courier", 12))
    label13.pack(side=tk.LEFT)

    edit8 = tk.Text(marcaFrame, width=40, height=1)
    edit8.pack(side=tk.LEFT)
    
    marcaFrame.pack(side=tk.TOP, anchor=tk.NW)

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

    def registrarProducto():
        vNombre = edit7.get("1.0",'end-1c')
        vMarca = edit8.get("1.0",'end-1c')
        vCategoria = edit9.get("1.0",'end-1c')
        vPrecio = edit10.get("1.0",'end-1c')

        insertarProducto(vNombre, vPrecio, vMarca, vCategoria)
        
    #BOTONES
    registrarborrarFrame = tk.Frame(ventanaProductos, bg="dodger blue")
    
    button6 = tk.Button(registrarborrarFrame, text="REGISTRAR", command=registrarProducto, bg="green")
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

    label16 = tk.Label(ventanaVentas, text="FACTURAR", bg="dodger blue", fg="black")
    label16.config(font=("Courier", 24))
    label16.pack(side=tk.TOP, anchor=tk.NW)

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

    #FECHA
    fechaFrame = tk.Frame(ventanaVentas)
    
    label20 = tk.Label(fechaFrame, text="Fecha:", bg="dodger blue", fg="black")
    label20.config(font=("Courier", 12))
    label20.pack(side=tk.LEFT)

    edit13 = tk.Text(fechaFrame, width=15, height=1)
    edit13.pack(side=tk.LEFT)
    
    fechaFrame.pack(side=tk.TOP, anchor=tk.NW)

    #VENDEDOR
    vendedorFrame = tk.Frame(ventanaVentas)
    
    label21 = tk.Label(vendedorFrame, text="Nombre vendedor:", bg="dodger blue", fg="black")
    label21.config(font=("Courier", 12))
    label21.pack(side=tk.LEFT)

    edit14 = tk.Text(vendedorFrame, width=60, height=1)
    edit14.pack(side=tk.LEFT)
    
    vendedorFrame.pack(side=tk.TOP, anchor=tk.NW)

    

    #BOTONES
    registrarborrarFrame = tk.Frame(ventanaVentas, bg="dodger blue")
    
    button8 = tk.Button(registrarborrarFrame, text="REGISTRAR", command=mostrarVentanaClientes, bg="green")
    button8.config(font=("Courier", 20))
    button8.pack(side=tk.LEFT, padx=20, pady=10, ipadx=8)

    button9 = tk.Button(registrarborrarFrame, text="BORRAR", command=mostrarVentanaClientes, bg="red")
    button9.config(font=("Courier", 20))
    button9.pack(side=tk.LEFT, padx=20, pady=10, ipadx=8)
    
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
