# Discord Bot
Python discord bot. Generates jokes, images and upscales last generated image.
Enter "!help" in discord channel to get info about commands

## What do you need to do?

### 1. Generate Discord Bot Token. 
- go to [Discord Developer Portal](https://discord.com/developers/applications)
- add new application, next add bot to application
- copy  **Discord Bot Token**

### 2. Generate StabilityAI API KEY.
- register at [Stability AI Platform](https://platform.stability.ai/)
- copy **StabilityAI API Key**
- 
### 3. Create own "secrets.py" file with code:

- create 'secrets.py' file in main catalog of project:

```python
def getDiscordToken():
    return "YOUR_DISCORD_BOT_TOKEN"

def getStabilityToken():
    return "YOUR_STABILITY_AI_KEY"
```

### 4. In Discord Developer Portal in Bot/Privileged Gateway Intents enable Message Content Intent

### 5. Let go your bot into your Discord server
- select OAuth2 > URL Generator
- select bot permissions
- generate invitation link for your bot and invite him at selected server

