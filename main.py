import os
import discord
from discord import app_commands
import webserver

TOKEN = os.getenv('TOKEN')

# Configura gli intenti per il bot
intents = discord.Intents.default()
intents.message_content = True

# Crea l'istanza del client
class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tree = app_commands.CommandTree(self)

    async def on_ready(self):
        await self.tree.sync()  # Sincronizza i comandi slash
        print(f'{self.user} è connesso a Discord!')

client = MyClient(intents=intents)

# Comando slash che risponde con "Ciao!" quando l'utente invia il comando /ciao
@client.tree.command(name='ciao', description='Risponde con Ciao!')
async def ciao(interaction: discord.Interaction):
    await interaction.response.send_message('Ciao!')

# Avvio del bot (inserisci il tuo token del bot qui)
webserver.keep_alive()
if TOKEN is None:
    print("Errore: il token del bot non è stato trovato. Assicurati che la variabile d'ambiente 'TOKEN' sia impostata correttamente.")
else:
    # Avvio del bot utilizzando il token
    client.run(TOKEN)
