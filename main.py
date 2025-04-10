import nextcord
from nextcord.ext import commands  
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

intents = nextcord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True  

bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot is ready! Logged in as {bot.user}")
    print(f"-------------------------------------")

# Load cogs
initial_extensions = ["cogs.general", "cogs.moderation"]

if __name__ == "__main__":
    for extension in initial_extensions:
        bot.load_extension(extension)

bot.run(BOT_TOKEN)
