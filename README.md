# discordbot
Python discord bot. Generates jokes, images and upscales last generated image.
Enter "!help" in discord channel to get info about commands

What do you need to do?
1. Generate Discord Bot Token. 
2. Generate StabilityAI API KEY.

3. Create own "secrets.py" file with code:

def getDiscordToken():
    return "YOUR_DISCORD_BOT_TOKEN"

def getStabilityToken():
    return "YOUR_STABILITY_AI_KEY"

4. In Discord Developer Portal in Bot/Privileged Gateway Intents enable Message Content Intent
5. Let go your bot into your Discord server
