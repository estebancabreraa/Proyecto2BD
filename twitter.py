import tweepy 
import pymongo
import random

# personal information 
consumer_key ="bhGT74KTrcR5PJAfglgPmADCE"
consumer_secret ="Z47NPKL8u5WBAYkGMPbRQNFDQiFObXMNLiEJkXLBClZ8BoASBC"
access_token ="1134970237990948865-rCYB3Ygoxjo72bAZlA5RiSMcnReORu"
access_token_secret ="Eqc6AiAFs1fEALaS2gKlaAMmPhH5ZbWvoKWMszf7mH6dd"
  
# authentication 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_token, access_token_secret) 

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["proyecto3"]

clientes = mydb["cliente"]
tiendas = mydb["tienda"]
compras = mydb["compra"]

        
mayoresCompradores = compras.aggregate([{"$sortByCount": "$nit"}])

contador = 0
for x in mayoresCompradores:
    if contador < 5:
        print(x)
    elif contador == 4:
        break
    contador = contador + 1

#Cristobal Hernandez
#Lucrecia Ramos
#Natalia Alvarado
#Camila Garcia
#Gonzalo Quinones

nombres = ["Cristobal Hernandez","Lucrecia Ramos","Natalia Alvarado","Camila Garcia","Camila Garcia"]

for i in range(0,4):
    api = tweepy.API(auth) 
    tweet ="¡Felicidades " + nombres[i] + "! Has ganado un GRAN DESCUENTO." # toDo 
    image_path =str(i) + ".jpg" # toDo 
      
    # to attach the media file 
    status = api.update_with_media(image_path, tweet)  
    api.update_status(status = tweet) 
