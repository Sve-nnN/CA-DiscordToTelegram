
import discord
from dotenv import load_dotenv
import os
from telegram.ext import Updater
from telegram import Update
import urllib.parse
from urllib.request import urlopen
from datetime import datetime


load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

# TELEGRAM
# token = os.environ['TOKEN']
# chatid = os.environ['CHATID']
token = os.getenv("token")
chatid = os.getenv("chatid")
updater = Updater(
    token=token, use_context=True)
dispatcher = updater.dispatcher


def webhook(endpoint):
    endpoint_parsed = urllib.parse.quote(endpoint)
    url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chatid}&text=' + str(
        endpoint_parsed)
    # return url
    return (url)


def telegramForwarder(message) -> None:
    # Abrir URL.
    r = urlopen(webhook(message))
    # Leer el contenido y e imprimir su tamaño.
    r.read()
    # Cerrar para liberar recursos.
    r.close()

# funcion para determinar que dia de la semana es


def mostrarDia():
    dt = datetime.now()
    if dt.isoweekday() == 1:
        return "Lunes"
    if dt.isoweekday() == 2:
        return "Martes"
    if dt.isoweekday() == 3:
        return "Miercoles"
    if dt.isoweekday() == 4:
        return "Jueves"
    if dt.isoweekday() == 5:
        return "Viernes"
    if dt.isoweekday() == 6:
        return "Sabado"
    if dt.isoweekday() == 7:
        return "Domingo"


@client.event
async def on_ready():
    print(f'Te has logueado como {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Si el dia es jueves y el mensaje contiene "@Scalper VIP", entra en el mensaje embedido y lo reenvia
    if mostrarDia() == "Jueves" and message.content == "@Scalper VIP":
        if message.embeds:
            embed = message.embeds[0]
            telegramForwarder(
                f"{message.author} ha enviado: {embed.title, embed.description}")
            print(embed.title)
            print(embed.description)
        print(f'Es jueves, por lo tanto he enviado: {message.content}')

    else:
        print(f"El autor es: {message.author} ")
        print(
            f"Hoy es {mostrarDia()}, por lo tanto no voy a enviar nada. ")

client.run(
    'MTA2NDMyMDA4MDU1NDUwNDI1Mg.G8pilY.8MMgRDUy3e8Z-mXVHewauKmEgU_l2Q3ybpp4pU')
