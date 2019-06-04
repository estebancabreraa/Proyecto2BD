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
from tkinter import messagebox
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
        database = "tiendaFinal"
'''
#def simulacionClientes(cant):
def simulacionCompras(cantFacturas,fecha):
    try:
    
        connection = psycopg2.connect(user = "postgres",
                                      password = "esteban1998",
                                      host = "127.0.0.1",
                                      port = "5432",
                                      database = "tiendaFinal")
        cursor = connection.cursor()
        clientesList=("Raul Monzon","Kevin Macario","Esteban Cabrera","Miguel Valle","Gustavo de Leon","Alan Do Santos","Camila Ahuat","Luis Salazar","Luis Esturban")
        nitList=("123456789-00","123456789-01","123456789-04","123456789-02","123456789-03","123456789-05","123456789-06","123456789-07")
        sucursales=["a","b","c","d","e","f","g","h","i","j","k","l"]
        idProductosList=["123456","123457","123484","123459","123450"]
        
        
        for i in range(cantFacturas):

            
            NumFactura=randint(100000, 999999)
            indexSuc=randint(0,10)
            cantidad=randint(0,10)
            indexPro=randint(0,4)
            indexCli=randint(1,6)
            direccion=("Ciudad")
            total=randint(10,100)
            create_table_query = '''INSERT INTO Compras(NumFactura, Sucursal, Cantidad, IDProducto, Total) VALUES(%s, %s, %s, %s, %s);'''
            cursor.execute(create_table_query, (NumFactura, sucursales[indexSuc], randint(0,10), idProductosList[indexPro], total))
            
            create_table_query = '''INSERT INTO Facturas(Nombre, NumFactura, Direccion, Sucursal,Fecha, Nit, IDVendedor) VALUES(%s, %s, %s, %s, %s, %s, %s);'''
            cursor.execute(create_table_query, (clientesList[indexCli], NumFactura, "ciudad", sucursales[indexSuc], fecha, nitList[indexCli], 123456))
            
            connection.commit()
        
        messagebox.showinfo(message="Se ha registrado la simulacion exitosamente.", title="Registro")
    except (Exception, psycopg2.DatabaseError) as error :
        messagebox.showerror(message="No se pudo registrar la simulacion..", title="Registro fallido")
        print ("No se pudo registrar cliente.", error)
    finally:
        #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")
    

def buscarCliente(nombre):
    try:
    
        connection = psycopg2.connect(user = "postgres",
                                      password = "esteban1998",
                                      host = "127.0.0.1",
                                      port = "5432",
                                      database = "tiendaFinal")
        cursor = connection.cursor()
        
        create_table_query = '''SELECT * FROM Cliente WHERE Nombre=%s;'''
        
        cursor.execute(create_table_query, (nombre,))

        result = cursor.fetchall()

        nit = ""
        sexo = ""
        telefono = ""
        direccion = ""
        fechanac = ""
        
        
        for row in result:
            sexo = row[0]
            nit = row[1]
            telefono = row[2]
            direccion = row[3]
            fechanac = row[5]
            
            
        
        connection.commit()
        
        mensaje = "NIT: " + nit + ".\n" + "Nombre: " + nombre + ".\n" + "Direccion: " + direccion + ".\n" + "Telefono: " + telefono + ".\n" + "Fecha de nacimiento: " + fechanac + ".\n" + "Sexo: " + sexo + ".\n"
        
        messagebox.showinfo(message=mensaje, title="Consulta")
    except (Exception, psycopg2.DatabaseError) as error :
        messagebox.showerror(message="No se encontro el cliente.", title="Consulta fallida")
        print ("No se pudo registrar cliente.", error)
    finally:
        #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")


def buscarProducto(nombre):
    try:
    
        connection = psycopg2.connect(user = "postgres",
                                      password = "esteban1998",
                                      host = "127.0.0.1",
                                      port = "5432",
                                      database = "tiendaFinal")
        cursor = connection.cursor()
        
        create_table_query = '''SELECT * FROM Producto WHERE Nombre=%s;'''
        
        cursor.execute(create_table_query, (nombre.upper(),))

        result = cursor.fetchall()

        idproducto =""
        precio = ""
        
        
        for row in result:
            idproducto = row[0]
            precio = row[1]
            
        
        connection.commit()
        
        mensaje = "ID: " + idproducto + ".\n" + "Nombre: " + nombre + ".\n" + "Precio: " + precio + ".\n"
        
        messagebox.showinfo(message=mensaje, title="Consulta")
    except (Exception, psycopg2.DatabaseError) as error :
        messagebox.showerror(message="No se encontro el producto.", title="Consulta fallida")
        print ("No se pudo registrar cliente.", error)
    finally:
        #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")

def buscarFactura(numero):
    try:
    
        connection = psycopg2.connect(user = "postgres",
                                      password = "esteban1998",
                                      host = "127.0.0.1",
                                      port = "5432",
                                      database = "tiendaFinal")
        cursor = connection.cursor()
        
        create_table_query = '''SELECT * FROM Facturas WHERE NumFactura= %s;'''
        
        cursor.execute(create_table_query, (numero,))

        result = cursor.fetchall()

        direccion = ""
        nombre = ""
        sucursal = ""
        fecha = ""
        nit = ""
        fecha = ""
        
        for row in result:
            nombre = row[0]
            direccion = row[2]
            sucursal = row[3]
            fecha = row[4]
            nit = row[5]
        
        connection.commit()
        
        mensaje = "ID: " + numero + ".\n" + "Nombre: " + nombre + ".\n" + "Nit: " + nit + ".\n" + "Direccion: " + direccion + ".\n" + "Sucursal: " + sucursal + ".\n"  + "Fecha: " + fecha + ".\n"
        
        messagebox.showinfo(message=mensaje, title="Consulta")
    except (Exception, psycopg2.DatabaseError) as error :
        messagebox.showerror(message="No se encontro la factura.", title="Consulta fallida")
        print ("No se pudo registrar cliente.", error)
    finally:
        #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")



def insertarCliente(sexo, nit, telefono, direccion, nombre, fechanac):
    try:
    
        connection = psycopg2.connect(user = "postgres",
                                      password = "esteban1998",
                                      host = "127.0.0.1",
                                      port = "5432",
                                      database = "tiendaFinal")
        cursor = connection.cursor()
        
        create_table_query = '''INSERT INTO Cliente(Sexo, Nit, Telefono, Direccion, Nombre, FechaNac) VALUES(%s, %s, %s, %s, %s, %s);'''
        
        cursor.execute(create_table_query, (sexo, nit, telefono, direccion, nombre, fechanac))
        
        connection.commit()
        
        messagebox.showinfo(message="Se ha registrado el cliente exitosamente.", title="Registro")
    except (Exception, psycopg2.DatabaseError) as error :
        messagebox.showerror(message="No se pudo registrar el cliente..", title="Registro fallido")
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
                                      database = "tiendaFinal")
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

        if (len(IDMarca) < 1):
            IDMarca = randint(100000, 999999);
            
            create_table_query = '''INSERT INTO Marca(Nombre, IDMarca) VALUES(%s, %s);'''
            
            cursor.execute(create_table_query, (marca.upper(), IDMarca))

        if (len(IDCategoria) < 1):
            IDCategoria = randint(100000, 999999);
            
            create_table_query = '''INSERT INTO Categoria(Nombre, IDCategoria) VALUES(%s, %s);'''
            
            cursor.execute(create_table_query, (categoria.upper(), IDCategoria))
            
        
        
        create_table_query = '''INSERT INTO Producto(IDProducto, Precio, Nombre, IDMarca, IDCategoria) VALUES(%s, %s, %s, %s, %s);'''
        
        cursor.execute(create_table_query, (IDProducto, precio, nombre.upper(), IDMarca, IDCategoria))
        
        connection.commit()
        
        messagebox.showinfo(message="Se ha registrado el producto exitosamente.", title="Registro")
    except (Exception, psycopg2.DatabaseError) as error :
        messagebox.showerror(message="No se pudo registrar el cliente..", title="Registro fallido")
        print ("No se pudo registrar producto.", error)
    finally:
        #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")

def insertarFacturaCompra(nit, nombreCliente, fecha, sucursal, nombreVendedor, nombreSucursal, cantidad, nombreProducto):
    try:
        connection = psycopg2.connect(user = "postgres",
                                      password = "esteban1998",
                                      host = "127.0.0.1",
                                      port = "5432",
                                      database = "tiendaFinal")
        cursor = connection.cursor()
        #####
        create_table_query = '''SELECT * FROM Vendedor WHERE Nombre = %s;'''

        cursor.execute(create_table_query, (nombreVendedor,))

        resultado = cursor.fetchall()

        IDVendedor = ""
        
        for row in resultado:
            IDVendedor = row[0]

        if (len(IDVendedor) < 1):
            IDVendedor = randint(100000, 999999);
        #####

        #####
        create_table_query = '''SELECT * FROM Producto WHERE Nombre = %s;'''

        cursor.execute(create_table_query, (nombreProducto.upper(),))

        resultado = cursor.fetchall()

        IDProducto = ""
        precio =""
        for row in resultado:
            IDProducto = row[0]
            precio = row[1]

        if (len(IDProducto) < 1):
            IDProducto = randint(100000, 999999);
            precio ="5.00"
        #####

        total = float(cantidad)*float(precio)
        tot = str(total)
        print(tot)

        NumFactura = randint(100000, 999999)
        
        direccion="ciudad"
        create_table_query = '''INSERT INTO Compras(NumFactura, Sucursal, Cantidad, IDProducto, Total) VALUES(%s, %s, %s, %s, %s);'''
                
        cursor.execute(create_table_query, ("483939", str(sucursal), str(cantidad), IDProducto, str(tot)))

        create_table_query = '''INSERT INTO Facturas(Nombre, NumFactura, Direccion, Sucursal, Fecha, Nit, IDVendedor) VALUES(%s, %s, %s, %s, %s, %s, %s);'''
                
        cursor.execute(create_table_query, (str(nombreCliente), str(NumFactura), direccion, str(sucursal), str(fecha), str(nit), IDVendedor))

       
        
        connection.commit()
                
        messagebox.showinfo(message="Se ha registrado el factura exitosamente.", title="Registro")
    except (Exception, psycopg2.DatabaseError) as error :
        messagebox.showerror(message="No se pudo registrar la factura..", title="Registro fallido")
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

    def borrarCampos1():
        edit1.delete('1.0', 'end-1c')
        edit2.delete('1.0', 'end-1c')
        edit3.delete('1.0', 'end-1c')
        edit4.delete('1.0', 'end-1c')
        edit5.delete('1.0', 'end-1c')
        edit6.delete('1.0', 'end-1c')
        
    def registrarCliente():
        vNombre = edit1.get("1.0",'end-1c')
        vFecha = edit2.get("1.0",'end-1c')
        vSexo = edit3.get("1.0",'end-1c')
        vDireccion = edit4.get("1.0",'end-1c')
        vTelefono = edit5.get("1.0",'end-1c')
        vNit = edit6.get("1.0",'end-1c')

        insertarCliente(vSexo, vNit, vTelefono, vDireccion, vNombre, vFecha)

        borrarCampos1()


    #BOTONES
    registrarborrarFrame = tk.Frame(ventanaClientes, bg="dodger blue")
    
    button4 = tk.Button(registrarborrarFrame, text="REGISTRAR", command=registrarCliente, bg="green")
    button4.config(font=("Courier", 20))
    button4.pack(side=tk.LEFT, padx=20, pady=10, ipadx=8)

    button5 = tk.Button(registrarborrarFrame, text="BORRAR", command=borrarCampos1, bg="red")
    button5.config(font=("Courier", 20))
    button5.pack(side=tk.LEFT, padx=20, pady=10, ipadx=8)
    
    registrarborrarFrame.pack(side=tk.TOP, anchor=tk.NW)

    buscarFrame = tk.Frame(ventanaClientes, bg="dodger blue")

    label31 = tk.Label(buscarFrame, text="Buscar por nombre:", bg="dodger blue", fg="black")
    label31.config(font=("Courier", 12))
    label31.pack(side=tk.LEFT)

    edit26 = tk.Text(buscarFrame, width=15, height=1)
    edit26.pack(side=tk.LEFT)

    def consultarCliente():
        n = edit26.get("1.0",'end-1c')

        buscarCliente(n)
    
    button12 = tk.Button(buscarFrame, text="BUSCAR", command=consultarCliente, bg="green")
    button12.config(font=("Courier", 20))
    button12.pack(side=tk.LEFT, padx=20, pady=10, ipadx=8)
    
    buscarFrame.pack(side=tk.TOP, anchor=tk.NW)

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

    def borrarCampos2():
        edit7.delete('1.0', 'end-1c')
        edit8.delete('1.0', 'end-1c')
        edit9.delete('1.0', 'end-1c')
        edit10.delete('1.0', 'end-1c')

    def registrarProducto():
        vNombre = edit7.get("1.0",'end-1c')
        vMarca = edit8.get("1.0",'end-1c')
        vCategoria = edit9.get("1.0",'end-1c')
        vPrecio = edit10.get("1.0",'end-1c')

        insertarProducto(vNombre, vPrecio, vMarca, vCategoria)

        borrarCampos2()

    def borrarCampos1():
        edit7.delete('1.0', 'end-1c')
        edit8.delete('1.0', 'end-1c')
        edit9.delete('1.0', 'end-1c')
        edit10.delete('1.0', 'end-1c')

    #BOTONES
    registrarborrarFrame = tk.Frame(ventanaProductos, bg="dodger blue")
    
    button6 = tk.Button(registrarborrarFrame, text="REGISTRAR", command=registrarProducto, bg="green")
    button6.config(font=("Courier", 20))
    button6.pack(side=tk.LEFT, padx=20, pady=10, ipadx=8)

    button7 = tk.Button(registrarborrarFrame, text="BORRAR", command=borrarCampos2, bg="red")
    button7.config(font=("Courier", 20))
    button7.pack(side=tk.LEFT, padx=20, pady=10, ipadx=8)
    
    registrarborrarFrame.pack(side=tk.TOP, anchor=tk.NW)

    buscarFrame = tk.Frame(ventanaProductos, bg="dodger blue")

    label30 = tk.Label(buscarFrame, text="Buscar por nombre:", bg="dodger blue", fg="black")
    label30.config(font=("Courier", 12))
    label30.pack(side=tk.LEFT)

    edit25 = tk.Text(buscarFrame, width=15, height=1)
    edit25.pack(side=tk.LEFT)

    def consultarProducto():
        n = edit25.get("1.0",'end-1c')
        
        buscarProducto(n)
    
    button11 = tk.Button(buscarFrame, text="BUSCAR", command=consultarProducto, bg="green")
    button11.config(font=("Courier", 20))
    button11.pack(side=tk.LEFT, padx=20, pady=10, ipadx=8)
    
    buscarFrame.pack(side=tk.TOP, anchor=tk.NW)

def mostrarVentanaVentas():
    ventanaVentas = tk.Tk()
    ventanaVentas.title("VENTAS")
    ventanaVentas.geometry("800x600")
    ventanaVentas.configure(background="dodger blue")

    #nombreCliente, nit, fecha, sucursal, total, nombreVendedor, nombreProducto
    
    #LABELS
    label4 = tk.Label(ventanaVentas, text="VENTAS", bg="dodger blue", fg="black")
    label4.config(font=("Courier", 44), pady=40)
    label4.pack()

    label16 = tk.Label(ventanaVentas, text="FACTURAR", bg="dodger blue", fg="black")
    label16.config(font=("Courier", 24))
    label16.pack(side=tk.TOP, anchor=tk.NW)

    #PRODUCTOS
    productosFrame = tk.Frame(ventanaVentas, bg="dodger blue")

    label22 = tk.Label(productosFrame, text="Cantidad:", bg="dodger blue", fg="black")
    label22.config(font=("Courier", 12))
    label22.pack(side=tk.LEFT)

    edit16 = tk.Text(productosFrame, width=10, height=1)
    edit16.pack(side=tk.LEFT)

    label23 = tk.Label(productosFrame, text="Nombre producto:", bg="dodger blue", fg="black")
    label23.config(font=("Courier", 12))
    label23.pack(side=tk.LEFT)

    edit17 = tk.Text(productosFrame, width=35, height=1)
    edit17.pack(side=tk.LEFT)
    
    productosFrame.pack(side=tk.TOP, anchor=tk.NW)
    
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

    #VENDEDOR
    sucursalFrame = tk.Frame(ventanaVentas)
    
    label22 = tk.Label(sucursalFrame, text="Sucursal:", bg="dodger blue", fg="black")
    label22.config(font=("Courier", 12))
    label22.pack(side=tk.LEFT)

    edit15 = tk.Text(sucursalFrame, width=40, height=1)
    edit15.pack(side=tk.LEFT)
    
    sucursalFrame.pack(side=tk.TOP, anchor=tk.NW)

    def borrarCampos3():
        edit11.delete('1.0', 'end-1c')
        edit12.delete('1.0', 'end-1c')
        edit13.delete('1.0', 'end-1c')
        edit14.delete('1.0', 'end-1c')
        edit15.delete('1.0', 'end-1c')
        edit16.delete('1.0', 'end-1c')
        edit17.delete('1.0', 'end-1c')

    def registrarVenta():
        vNit = edit11.get("1.0",'end-1c')
        vNombre = edit12.get("1.0",'end-1c')
        vFecha = edit13.get("1.0",'end-1c')
        vNombreVendedor = edit14.get("1.0",'end-1c')
        vSucursal = edit15.get("1.0",'end-1c')
        vCantidad = edit16.get("1.0",'end-1c')
        vNombreProducto = edit17.get("1.0",'end-1c')
        
        insertarFacturaCompra(vNit, vNombre, vFecha, vSucursal,vNombreVendedor, vSucursal, vCantidad, vNombreProducto)

        borrarCampos3()
    
    #BOTONES
    registrarborrarFrame = tk.Frame(ventanaVentas, bg="dodger blue")
    
    button8 = tk.Button(registrarborrarFrame, text="REGISTRAR", command=registrarVenta, bg="green")
    button8.config(font=("Courier", 20))
    button8.pack(side=tk.LEFT, padx=20, pady=10, ipadx=8)

    button9 = tk.Button(registrarborrarFrame, text="BORRAR", command=borrarCampos3, bg="red")
    button9.config(font=("Courier", 20))
    button9.pack(side=tk.LEFT, padx=20, pady=10, ipadx=8)
    
    registrarborrarFrame.pack(side=tk.TOP, anchor=tk.NW)
    
    buscarFrame = tk.Frame(ventanaVentas, bg="dodger blue")
    
    label32 = tk.Label(buscarFrame, text="Buscar por nombre:", bg="dodger blue", fg="black")
    label32.config(font=("Courier", 12))
    label32.pack(side=tk.LEFT)

    edit27 = tk.Text(buscarFrame, width=15, height=1)
    edit27.pack(side=tk.LEFT)

    def consultarFactura():
        n = edit27.get("1.0",'end-1c')
        
        buscarFactura(n)
    
    button16 = tk.Button(buscarFrame, text="BUSCAR", command=consultarFactura, bg="green")
    button16.config(font=("Courier", 20))
    button16.pack(side=tk.LEFT, padx=20, pady=10, ipadx=8)
    
    buscarFrame.pack(side=tk.TOP, anchor=tk.NW)
    

################################################################################
#                                    MAIN                                      #
################################################################################
#Simulacion
#simulacionCompras(10000,"2019/05/16")
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
