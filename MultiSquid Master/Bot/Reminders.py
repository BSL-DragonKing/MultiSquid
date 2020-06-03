import discord
import time
import datetime
from datetime import timezone, tzinfo, timedelta
from discord.ext import commands

#print('Current date and time: ', datetime.datetime.now())
#print("Current year: ", datetime.date.today().strftime("%Y"))
#print("Month of year: ", datetime.date.today().strftime("%B"))
#print("Week number of the year: ", datetime.date.today().strftime("%W"))
#print("Weekday of the week: ", datetime.date.today().strftime("%w"))
#print("Day of year: ", datetime.date.today().strftime("%j"))
#print("Day of the month : ", datetime.date.today().strftime("%d"))
#print("Day of week: ", datetime.date.today().strftime("%A"))

edits = {}

class Reminders(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @commands.command()
    async def reminders(self, ctx):
        embed = discord.Embed(title='😄 Your Reminders 📝', description='This is a place where you can store your important things and get reminded to do certain things!', timestamp=datetime.datetime.utcnow(), color=discord.Color.orange())
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/697569265913692171/697569662547918858/MultiSquid_pfp.png')
        embed.set_author(name='MultiSquid', icon_url='https://cdn.discordapp.com/attachments/697569265913692171/697569662547918858/MultiSquid_pfp.png')
        embed.add_field(name='Emote Key', value='⏰: Set Reminder\n\n❌: React with this to remove any reminder\'s you\'ve setup with me\n\n📝: Shows all the reminders that you have setup with me', inline=True)
        m = await ctx.send(embed=embed)
        for r in ['⏰', '❌', '📝']: await m.add_reaction(r)

    @commands.command()
    async def date (self, ctx):
        current = datetime.datetime.now()
        await ctx.send(current.strftime('%A, %B %d, %Y'))
    
    @commands.command(aliases=['time'])
    async def ctime (self, ctx):
        current = datetime.datetime.now()
        await ctx.send(current.strftime('%Ih:%Mm:%Ss %p'))

    @commands.command()
    async def mtime (self, ctx):
        current = datetime.datetime.now()
        await ctx.send(current.strftime('%Hh:%Mm:%Ss %p'))
    
    @commands.is_owner()
    @commands.command(aliases=['startup'])
    async def boott (self, ctx):
        start = datetime.datetime.now()
        await ctx.send(start)
        
def setup(client):
    client.add_cog(Reminders(client))