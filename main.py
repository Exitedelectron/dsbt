import discord
from discord.ext import commands
import os
import webserver


# Imposta il prefisso dei comandi del bot (es. !comando)
bot = commands.Bot(command_prefix='!')

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
bot.run('MTIxMTQwNzg5NjA0NzUyNTg5OA.GyC-l6.3psAg364K2ku-1iQ1HbqM_AARVkrbPPrlDujcA')
