import os
import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
import webserver

TOKEN = os.getenv('TOKEN')
# Configura gli intenti per il bot
intents = discord.Intents.default()
intents.message_content = True

# Crea l'istanza del bot
bot = commands.Bot(command_prefix='!', intents=intents)

# Crea l'istanza per i comandi slash
slash = SlashCommand(bot, sync_commands=True)

# Evento che viene chiamato quando il bot si connette e si è connesso a Discord
@bot.event
async def on_ready():
    print(f'{bot.user} è connesso a Discord!')

# Comando slash che risponde con "Ciao!" quando l'utente invia il comando /ciao
@slash.slash(name='ciao', description='Risponde con Ciao!')
async def ciao(ctx: SlashContext):
    await ctx.send('Ciao!')

# Avvio del bot (inserisci il tuo token del bot qui)
webserver.keep_alive()
if TOKEN is None:
    print("Errore: il token del bot non è stato trovato. Assicurati che la variabile d'ambiente 'TOKEN' sia impostata correttamente.")
else:
    # Avvio del bot utilizzando il token
    bot.run(TOKEN)
