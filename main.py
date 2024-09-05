import os
import discord
from discord import app_commands
from discord.ext import commands
import webserver

TOKEN = os.getenv('TOKEN')

# Configura gli intenti per il bot
intents = discord.Intents.default()
intents.message_content = True

# Crea l'istanza del bot
bot = commands.Bot(command_prefix='!', intents=intents)

# Definisce un albero di comandi slash
tree = bot.tree

# Evento che viene chiamato quando il bot si connette e si è connesso a Discord
@bot.event
async def on_ready():
    await tree.sync()  # Sincronizza i comandi slash
    print(f'{bot.user} è connesso a Discord!')

# Comando slash che risponde con "Ciao!" quando l'utente invia il comando /ciao
@tree.command(name='ciao', description='Risponde con Ciao!')
async def ciao(interaction: discord.Interaction):
    await interaction.response.send_message('Ciao!')

# Avvio del bot (inserisci il tuo token del bot qui)
webserver.keep_alive()
if TOKEN is None:
    print("Errore: il token del bot non è stato trovato. Assicurati che la variabile d'ambiente 'TOKEN' sia impostata correttamente.")
else:
    # Avvio del bot utilizzando il token
    bot.run(TOKEN)
