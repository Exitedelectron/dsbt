import os
import discord
from discord.ext import commands
import webserver

TOKEN = os.getenv('TOKEN')
# Configura gli intenti per il bot
intents = discord.Intents.default()
intents.message_content = True  # Abilita l'accesso al contenuto dei messaggi

# Se hai bisogno di intenti per membri o presenze, usa anche questi
# intents.members = True
# intents.presences = True

# Crea l'istanza del bot con il prefisso dei comandi e gli intenti specificati
bot = commands.Bot(command_prefix='!', intents=intents)

# Evento che viene chiamato quando il bot si connette e si è connesso a Discord
@bot.event
async def on_ready():
    print(f'{bot.user} è connesso a Discord!')

# Comando semplice che risponde con "Ciao!" quando l'utente invia il comando !ciao
@bot.command(name='ciao')
async def ciao(ctx):
    await ctx.send('Ciao!')

# Avvio del bot (inserisci il tuo token del bot qui)
webserver.keep_alive()
bot.run(TOKEN)
