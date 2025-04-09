import nextcord
from nextcord.ext import commands

class General(commands.Cog):
    """General commands for the bot."""

    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command()
    async def ping(self, interaction: nextcord.Interaction):
        """Returns the bot's latency."""
        latency = round(self.bot.latency * 1000)  # Convert latency to milliseconds
        await interaction.response.send_message(f"Pong! Latency: {latency}ms")

def setup(bot):
    bot.add_cog(General(bot))