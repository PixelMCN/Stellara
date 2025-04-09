import nextcord
from nextcord.ext import commands
from config import BOT_TOKEN  # Import the bot token from config.py

# Intents are required for the bot to function properly
intents = nextcord.Intents.default()
intents.message_content = True

# Create a bot instance
bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot is ready! Logged in as {bot.user}")
    print(f"-------------------------------------")

@bot.slash_command()
async def ping(interaction: nextcord.Interaction):
    """Returns the bot's latency."""
    latency = round(bot.latency * 1000)  # Convert latency to milliseconds
    await interaction.response.send_message(f"Pong! Latency: {latency}ms")


# Run the bot using the token from config.py
if BOT_TOKEN:
    bot.run(BOT_TOKEN)
else:
    print("Error: BOT_TOKEN is not set in config.py")





