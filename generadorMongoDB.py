import pymongo
import random
import psycopg2
from psycopg2 import Error
from random import randint


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["proyecto3"]

clientes = mydb["cliente"]
tiendas = mydb["tienda"]
compras = mydb["compra"]



nameList = [
    'Juan',  
    'Jose'  ,
    'Esteban'  ,
    'Raul'  ,
    'Jaime'  ,
    'Rocio' , 
    'Ana' , 
    'Sofia'  ,
    'Camila' , 
    'Luis' , 
    'Roberto', 
    'Jorge' , 
    'Laura' , 
    'Antonio' , 
    'Natalia' , 
    'Javier' , 
    'Francisco' , 
    'Alejandro' , 
    'Gonzalo' , 
    'Susana' , 
    'Fernando' , 
    'Rodrigo' , 
    'Cristobal' , 
    'Lucrecia' , 
    'Valeria' , 
    'Sasha' , 
    'Cristina',  
    'Mario' , 
    'Carlos'
    ]

lastnameList = [
    'Cabrera',
    'Hernandez',
    'Garcia',
    'Martinez',
    'Maldonado',
    'Arevalo',
    'Guerra',
    'Cozza',
    'Rivera',
    'Rosales',
    'Ahuat',
    'Bran',
    'Casillas',
    'Ramos',
    'Van Dyk',
    'Quezada',
    'Quinones',
    'Lopez',
    'De Leon',
    'Alvarado'
]

addressList = [
    '14 Ave A Zona 15',
    '17 Ave B Zona 2',
    '2 Ave A Zona 1',
    '15 Ave C Zona 18',
    '12 Ave B Zona 4',
    '12 Ave C Zona 6',
    '14 Ave C Zona 2',
    '16 Ave B Zona 1',
    '2 Ave B Zona 3',
    '1 Ave C Zona 15',
    '18 Ave A Zona 16',
    '3 Ave A Zona 16',
    '5 Ave C Zona 10',
    '10 Ave A Zona 11',
    '2 Ave B Zona 12',
    '5 Ave B Zona 13',
    '7 Ave A Zona 5',
    '10 Ave C Zona 1'
]



storeNameList = [
    'Cemaco',
    'Siman',
    'Modas Caramelos',
    'Paiz',
    'La Torre',
    'Clau',
    'El Duende',
    'Lacoste',
    'Adidas',
    'Nike',
    'Pull&Bear',
    'Zara',
    'Columbia',
    'Artemis Edinter',
    'Sophos',
    'Vans',
    'Do Mi Sol',
    'Casa Instrumental',
    'Kodak'
]

idsClientes = []
idsNits = []
idsTiendas = []
nombresTiendas = []

def generate_random_name():
    nombre = random.choice(nameList)
    apellido = random.choice(lastnameList)
    completo = f'{nombre} {apellido}'
    return completo

def generate_nit():
    nit = random.randint(1111111, 9999999)
    return nit

def generate_date():
    day = random.randint(0,28)
    month = random.randint(1,12)
    year = random.randint(2012, 2019)
    date = f'{day}/{month}/{year}'
    return date

def generate_bdate():
    day = random.randint(0,28)
    month = random.randint(1,12)
    year = random.randint(1940, 2001)
    date = f'{day}/{month}/{year}'
    return date

def generate_number():
    number = random.randint(50000000,59999999)
    return number

def insert_cliente(id_cliente, nit):
    nombre = generate_random_name()
    direccion = random.choice(addressList)
    date = generate_bdate()
    numero = generate_number()
    mydict = { "IDCliente": id_cliente, "nombre": nombre, "nit": nit, "fechaNac": date, "direccion": direccion, "telefono": numero}
    x = clientes.insert_one(mydict)

def insert_tienda(id_tienda):
    bandera = True
    direccion = random.choice(addressList)
    nombre = random.choice(storeNameList)
    numero = generate_number()
    mydict = { "IDTienda": id_tienda, "nombre": nombre, "direccion": direccion, "telefono": numero}
    if (not(nombre in nombresTiendas)):
        x = tiendas.insert_one(mydict)
        nombresTiendas.append(nombre)

def insert_compra(id_compra, nit, id_tienda):
    total = random.randrange(10, 10000)
    date = generate_date()
    producto = randint(000000,999999)
    mydict = { "IDCompra": id_compra, "fecha": date, "nit": nit, "IDProducto": producto, "IDTienda": id_tienda, "total": total}
    x = compras.insert_one(mydict)


if __name__ == '__main__':
    for i in range(0, 499):
        idcliente = randint(000000,999999)
        idsClientes.append(idcliente)
        idnit = randint(000000000,999999999)
        idsNits.append(idnit)
        idtienda = randint(000000,999999)
        idsTiendas.append(idtienda)     
        insert_cliente(idcliente, idnit)
        insert_tienda(idtienda)
    for i in range(0, 1499):
        insert_compra(randint(000000,999999), random.choice(idsNits), random.choice(idsTiendas))
    myresults = list(mydb.compras.aggregate([{"$sortByCount": "$nit"}]))
    print(myresults)
