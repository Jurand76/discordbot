import discord

import secrets
from secrets import getDiscordToken

# Inicjalizacja klienta bota
intents = discord.Intents.default()
intents.message_content = True  # Pozwala odczytywać treść wiadomości na serwerze

"""
Aby bot czytał wiadomości z kanału - w Discord Developer Portal:
- przejdź do zakładki Bot
- w sekcji Privileged Gateway Intents włącz Message Content Intent.
"""

# Przekaż intents do klienta
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Zalogowano jako {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return  # Ignoruj wiadomości wysyłane przez bota

    if message.content.startswith('!hello'):
        await message.channel.send(f'Cześć, {message.author.name}!')


# Token bota
TOKEN = secrets.getDiscordToken()
client.run(TOKEN)
