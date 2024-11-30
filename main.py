import discord

from joke_api import generate_joke
from secrets import getDiscordToken
from stability_api import generate_image
from stability_api import generate_upscaled_image

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

    if message.content.startswith('!joke'):
        result = generate_joke()
        await message.channel.send(result)

    if message.content.startswith('!image'):
        prompt = message.content[len("!image "):].strip()
        if not prompt:
            await message.channel.send("Podaj opis obrazu, np. `!image Lighthouse on a cliff`.")
            return
        await message.channel.send("Generuję obraz, proszę czekać...")
        image_path = generate_image(prompt)
        if not image_path.startswith("Error"):
            # Wysyłanie obrazu do kanału
            await message.channel.send(file=discord.File(image_path))
        else:
            await message.channel.send(f"Nie udało się wygenerować obrazu. {image_path}. Spróbuj ponownie.")

    if message.content.startswith('!upscale'):
        await message.channel.send("Upscaling wygenerowanego obrazu, proszę czekać...")
        image_path = generate_upscaled_image()
        if not image_path.startswith("Error"):
            # Wysyłanie obrazu do kanału
            await message.channel.send(file=discord.File(image_path))
        else:
            await message.channel.send(f"Nie udało się wygenerować obrazu. {image_path}. Spróbuj ponownie.")

    if message.content.startswith('!help'):
        result = '''
            Commands for bot:
                - !help - shows all commands for bot, 
                - !joke - generates joke
                - !hello - welcome
                - !image description_of_image, --ar aspect_ratio - generates image
                Example: !image cat inside car, driving, --ar 16:9
                - !upscale - 4x upscale of generated image 
        '''
        await message.channel.send(result)


# Token bota
TOKEN = getDiscordToken()
client.run(TOKEN)
