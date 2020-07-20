import discord
import datetime
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def infraction(self,ctx):
        await ctx.send('{ctx.author.mention} Please review chat and discuss with mod team abt this concern')

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount) 
        await ctx.message.delete()

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'Kicked {member.mention}')

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'Banned {member.mention}')

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if(user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.mention}')
                return

    @commands.command()
    async def muterole(self, member: discord.Member):
        SquidyMute = discord.utils.get(member.guild.roles, name='SquidyMute')
        if SquidyMute is None: SquidyMute = await member.guild.create_role(name='SquidyMute', reason='Needed a mute role!')
        if SquidyMute is True: pass

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def mute(self, ctx, member: discord.Member, *, reason=None):
        SquidyMute = discord.utils.get(member.guild.roles, name='SquidyMute')
        await member.add_roles(SquidyMute)
        await ctx.send(f'Muted {member.mention}')

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def unmute(self, ctx, member: discord.Member, *, reason=None):
        SquidyMute = discord.utils.get(member.guild.roles, name='SquidyMute')
        await member.remove_roles(SquidyMute)
        await ctx.send(f'Unmuted {member.mention}')

def setup(client):
    client.add_cog(Moderation(client))