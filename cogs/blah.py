import discord

from discord.ext import commands
from utils.checks import is_staff
from utils.utils import send_dm_message


class Blah(commands.Cog):
    """
    Custom Cog to make announcements.
    """
    def __init__(self, bot):
        self.bot = bot
        self.emoji = discord.PartialEmoji.from_str('🗣️')

    speak_blacklist = [
        647348710602178560,  # #minecraft-console
    ]

    @is_staff("OP")
    @commands.command()
    async def announce(self, ctx, *, inp):
        """Posts a message to the announcement channel."""
        await self.bot.channels['announcements'].send(inp, allowed_mentions=discord.AllowedMentions(everyone=True, roles=True))

    @is_staff("OP")
    @commands.command()
    async def speak(self, ctx, channel: discord.TextChannel, *, inp):
        """Sends a message to a channel."""
        if channel.id in self.speak_blacklist:
            await ctx.send(f'You cannot send a message to {channel.mention}.')
            return
        await channel.send(inp, allowed_mentions=discord.AllowedMentions(everyone=True, roles=True))

    @is_staff("OP")
    @commands.command()
    async def sendtyping(self, ctx, channel: discord.TextChannel = None):
        """Triggers typing on a channel."""
        if channel.id in self.speak_blacklist:
            await ctx.send(f'You cannot send a message to {channel.mention}.')
            return
        if channel is None:
            channel = ctx.channel
        await channel.trigger_typing()

    @is_staff("Owner")
    @commands.command()
    async def dm(self, ctx, member: discord.Member, *, inp):
        """Sends a message to the member."""
        await send_dm_message(member, inp, ctx)


def setup(bot):
    bot.add_cog(Blah(bot))
