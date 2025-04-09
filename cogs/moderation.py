import nextcord
from nextcord.ext import commands

class Moderation(commands.Cog):
    """Moderation commands for the bot."""

    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(guild_ids=[1358804712018804916])  
    async def ban(self, interaction: nextcord.Interaction, member: nextcord.Member, reason: str = "No reason provided"):
        """Bans a member from the server."""
        if not interaction.user.guild_permissions.ban_members:
            await interaction.response.send_message("You don't have permission to use this command.", ephemeral=True)
            return

        await member.ban(reason=reason)
        await interaction.response.send_message(f"{member} has been banned. Reason: {reason}")

    @nextcord.slash_command(guild_ids=[1358804712018804916])  
    async def kick(self, interaction: nextcord.Interaction, member: nextcord.Member, reason: str = "No reason provided"):
        """Bans a member from the server."""
        if not interaction.user.guild_permissions.kick_members:
            await interaction.response.send_message("You don't have permission to use this command.", ephemeral=True)
            return

        await member.kick(reason=reason)
        await interaction.response.send_message(f"{member} has been banned. Reason: {reason}")

def setup(bot):
    bot.add_cog(Moderation(bot))