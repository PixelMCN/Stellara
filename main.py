import nextcord
from nextcord.ext import commands
from config import BOT_TOKEN  


intents = nextcord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot is ready! Logged in as {bot.user}")
    print(f"-------------------------------------")

# returns the bot's latency
@bot.slash_command()
async def ping(interaction: nextcord.Interaction):
    """Returns the bot's latency."""
    latency = round(bot.latency * 1000)  # Convert latency to milliseconds
    await interaction.response.send_message(f"Pong! Latency: {latency}ms")



bot.run(BOT_TOKEN)






