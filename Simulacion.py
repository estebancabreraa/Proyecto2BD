import sqlite3
import random
import psycopg2
from psycopg2 import Error

try:
    connection = psycopg2.connect(user = "nchvspxozqzjnq",
                                  password = "100df41267e61758efab91f7375c74590acf34fa054d152d6f05008305470ef9",
                                  host = "ec2-107-20-230-70.compute-1.amazonaws.com",
                                  port = "5432",
                                  database = "d67vb6qc2sflcv")
    cursor = connection.cursor()
    """
    #Clientes
    
    
    nameList=['Thelma',
              'Yuriko',
              'Mathew',
              'Lavona',
              'Jamal',
              'Rochell',
              'Willia',
              'Glen',
              'Jenelle',
              'Nelson',
              'Katelyn',
              'Mackenzie',
              'Carman',
              'Lindsy',
              'Sheree',
              'Dorinda',
              'Jenae',
              'Janee',
              'Twana',
              'Yee',
              'Frederic',
              'Jaqueline',
              'Shelby',
              'Trista',
              'Daron',
              'Nikita',
              'Cristi',
              'Margrett',
              'Chanel  ']
    
    lastNList=['Wilkins',
               'Santana',
               'Henderson',
               'Sosa',
               'Price',
               'Church',
               'Branch',
               'Spencer',
               'Sampson',
               'Burton',
               'Baker',
               'Lin',
               'Sheppard',
               'Bray',
               'Haney',
               'Morales',
               'Gilbert',
               'Rosario',
               'Rocha',
               'Copeland']
    
    adress=['9072 South Leatherwood Ave.',
            'Ladson, SC 29456',
            '574 Roosevelt St.',
            'Osseo, MN 55311',
            '7704 Marsh Ave.',
            'Reidsville, NC 27320',
            '292 Fairground Street',
            'Vienna, VA 22180',
            '81 Amherst Dr.',
            'Florence, SC 29501',
            '949 Ketch Harbour Street',
            'Naugatuck, CT 06770',
            '988 Sunnyslope St.',
            'Akron, OH 44312',
            '121 North Harvey Dr.',
            'Bartlett, IL 60103',
            '8661 Lakeshore Ave.',
            'Southington, CT 06489',
            '7554 N. Arcadia St.',
            'Dearborn Heights, MI 48127',
            '173 Howard St.',
            'Graham, NC 27253',
            '525 Garfield St.',
            'Pittsford, NY 14534',
            '9259 Myrtle St.',
            'Morganton, NC 28655',
            '396 Santa Clara Dr.',
            'Murrells Inlet, SC 29576',
            '52 Henry St.',
            'Zeeland, MI 49464',
            '1 Bridge Drive',
            'Jamaica Plain, MA 02130',
            '20 Jackson St.',
            'Canonsburg, PA 15317',
            '5 Richardson Avenue',
            'Melrose, MA 02176',
            '266 La Sierra Drive',
            'Lakeville, MN 55044',
            '66 W. Essex Drive',
            'Greenville, NC 27834']
    for i in range (0,50):
        nombre=nameList[random.randint(0,len(nameList)-1)]+' '+lastNList[random.randint(0,len(lastNList)-1)]
        se=random.randint(0,1)
        if se==0:
            sexo='M'
        else:
            sexo='F'
        nit=10000001+i
        telefono=10000000+1
        direccion=adress[random.randint(0,len(adress)-1)]
        fechaNac='06/07/1998'
        query = '''INSERT INTO Cliente(Sexo, Nit, Telefono, Direccion, Nombre, FechaNac) VALUES(%s, %s, %s, %s, %s, %s);'''
        cursor.execute(query,(sexo,nit,telefono,direccion,nombre,fechaNac))
    connection.commit()
    print ('Clientes Ingresados')

    #Vendedor
    
    query='''INSERT INTO Vendedor(IDVendedor, Nombre, Direccion, Telefono, Salario, FechaContratacion, Puesto, Sexo,FechaNac) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
    IDVendedor=100000001
    Nombre='Raul Monzon'
    Direccion='Guatemala'
    Telefono='50171741'
    Salario='1000000'
    FechaContratacion='06/07/2015'
    Puesto='vendedor'
    Sexo='M'
    FechaNac='06/07/1998'
    cursor.execute(query,(IDVendedor,Nombre,Direccion,Telefono,Salario,FechaContratacion,Puesto,Sexo,FechaNac))
    
    #Marcas y Categoria
    marcaLista=['Nestle','PepsiCo','Unilever','Danone','Mars','Chanel','Versace','Prada','Gucci','Fendi','Abarth','Audi','Bentley','BMW','Bugatti']
    categoriaLista=['Comida','Ropa','Autos']
    cont=0
    for i in marcaLista:
        idc=10000000+cont
        cont=cont+1
        query='''INSERT INTO Marca (Nombre,IDMarca) VALUES(%s,%s)'''
        cursor.execute(query,(i,idc))
    cont=0
    for i in categoriaLista:
        idc=10000000+cont
        cont=cont+1
        query='''INSERT INTO Categoria (Nombre,IDCategoria) VALUES(%s,%s)'''
        cursor.execute(query,(i,idc))
    
    #Productos
    productos=['Chocomilk','Grapete','Fanta','Mirinda','Nestle','Q1','Q2','Q3','Q4','Q5','Camisa','Boxer','Playera','Sueter','Pantalon']
    for i in range (0,50):
        idc=10000000+i
        precio=random.randint(500,1000)
        nombre=productos[random.randint(0,len(productos)-1)]
        IDMarca=random.randint(10000000,10000014)
        IDCategoria=random.randint(10000000,10000002)
        query='''INSERT INTO Producto (IDProducto,Precio,Nombre,IDMarca,IDCategoria) VALUES(%s,%s,%s,%s,%s)'''
        cursor.execute(query,(idc,precio,nombre,IDMarca,IDCategoria))
    """
    
    #Factura
    for i in range(25000,1000000):
        idCliente=random.randint(10000001,10000050)
        idAusar=f"'{idCliente}'"
        query=f'''Select nombre From Cliente Where Nit ='{idCliente}' '''
        cursor.execute(query)
        nombre=cursor.fetchall()
        nombre=str(nombre[0])
        nombre=nombre[2:len(nombre)-3]
        idFactura=100+i
        query=f'''Select Direccion From Cliente Where Nit ='{idCliente}' '''
        cursor.execute(query)
        direccion=cursor.fetchall()
        direccion=str(direccion[0])
        direccion=direccion[2:len(direccion)-3]
        Abecedario=['a','e','i','o','u']
        posAb=random.randint(0,len(Abecedario)-1)
        suc=Abecedario[posAb]
        fecha='04/06/2019'
        IDVendedor='100000001'
        query=f'''INSERT INTO Facturas(Nombre,NumFactura,Direccion,Sucursal,Fecha,Nit,IDVendedor) VALUES('{nombre}','{idFactura}','{direccion}','{suc}','{fecha}','{idCliente}','{IDVendedor}')'''
        cursor.execute(query)
        cantProductosFactura=random.randint(1,3)
        for i in range (0,cantProductosFactura-1):
            cantidad=random.randint(1,5)
            IDProducto=random.randint(10000000,10000049)
            query=f'''Select Precio From Producto Where IDProducto='{IDProducto}' '''
            cursor.execute(query)
            precio=cursor.fetchall()
            precio=str(precio[0])
            precio=int(precio[2:len(precio)-3])
            total=cantidad*precio
            query=f'''INSERT INTO Compras(NumFactura,Cantidad,IDproducto,Total) VALUES('{idFactura}','{cantidad}','{IDProducto}','{total}')'''
            cursor.execute(query)
        connection.commit()
    
    
except (Exception, psycopg2.DatabaseError) as error :
    print ("No se pudo registrar debido a que ", error)
finally:
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
