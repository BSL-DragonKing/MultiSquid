import discord
import datetime
import json
from discord.ext import commands

error = {}
edits = {}
member = {}

class Tentacles(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.happy = discord.utils.get(client.get_guild(694981576467021884).emojis, name='happysquid')
        self.sad = discord.utils.get(client.get_guild(694981576467021884).emojis, name='sadsquid')
        self.servers = client.get_channel(717100060000911551)
    
    @commands.Cog.listener()
    async def on_error(self, ctx, event, args, kwargs):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please put in all the things you need to work this command.')

    @commands.Cog.listener()
    async def on_guild_join(self, guild: discord.Guild):
        #with open('prefixes.json', 'r') as f:
        #    prefixes = json.load(f)
        #prefixes[str(guild.id)] = '-'
        #with open('prefixes.json', 'w') as f:
        #    json.dump(prefixes, f, indent=4)
        await self.servers.send(embed=discord.Embed(title="{} I Explored a New Ocean! {}".format(self.happy, self.happy), description='',timestamp=datetime.datetime.utcnow(), color=0x03f0fc))
    
    @commands.Cog.listener()
    async def on_guild_remove(self, guild: discord.Guild):
        #with open('prefixes.json', 'r') as f:
        #    prefixes = json.load(f)
        #prefixes.pop[str(guild.id)]
        #with open('prefixes.json', 'w') as f:
        #    json.dump(prefixes, f, indent=4)
        await self.servers.send(embed=discord.Embed(title="{}The Kraken Scared Us Away!".format(self.sad),description='{} {}'.format(guild.name, guild.id),timestamp=datetime.datetime.utcnow(),color=0x00ff00))

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        global edits
        message = reaction.message
        if reaction.message.guild is None: return
        if user.bot or len(reaction.message.embeds) == 0 or reaction.message.author.id != reaction.message.guild.me.id:
            return
        if str(reaction) == '⏰':
            setrem = discord.Embed(title='📝 Time to start setting your reminders! 📝', description='A DM has been sent to you! To continue the process please go to your DMs', timestamp=datetime.datetime.utcnow(), color=0x47ff78)
            await message.edit (embed=setrem)
            await message.remove_reaction(reaction, user)
            setup = discord.Embed(title='Setting up a reminder!')
            await user  .send(embed=setup)
            for r in ['⬅']: await message.add_reaction(r)
        if str(reaction) == '❌':
            remdel = discord.Embed(title='❌ Deleting your reminders ❌', description='This is where you can delete your reminders. All the events shown below are all the ', timestamp=datetime.datetime.utcnow(), color=0xb50d0d)
            remdel.set_footer(text='Page 1 of 1') 
            remdel.set_thumbnail(url='https://cdn.discordapp.com/attachments/697569265913692171/697569662547918858/MultiSquid_pfp.png')
            remdel.set_author(name='MultiSquid', icon_url='https://cdn.discordapp.com/attachments/697569265913692171/697569662547918858/MultiSquid_pfp.png')
            remdel.add_field(name='Set Reminders', value='Reminder 1\nReminder 2\nReminder 3\nReminder 4\nReminder 5\nReminder 6', inline=True)
            await message.edit (content=None, embed=remdel)
            await message.remove_reaction (reaction, user)
            for r in ['⬅']: await message.add_reaction(r)
        if str(reaction) == '📝':
            remlist = discord.Embed(title = '⏰ Your Set Reminders 📝', description = 'This is where all the reminders you set are', timestamp=datetime.datetime.utcnow(), color = discord.Color.orange())
            remlist.set_footer(text='Page 1 of 1') 
            remlist.set_thumbnail(url='https://cdn.discordapp.com/attachments/697569265913692171/697569662547918858/MultiSquid_pfp.png')
            remlist.set_author(name='MultiSquid', icon_url='https://cdn.discordapp.com/attachments/697569265913692171/697569662547918858/MultiSquid_pfp.png')
            remlist.add_field(name='Set Reminders', value='Reminder 1\nReminder 2\nReminder 3\nReminder 4\nReminder 5\nReminder 6', inline=True)
            await message.edit (content=None, embed=remlist)
            await message.remove_reaction (reaction, user)
            for r in ['⬅']: await message.add_reaction(r)
        if str(reaction) == '⬅':
            remhome = discord.Embed(title='⌚ Reminders Homepage ⌚', description='This is a place where you can store your important things and get reminded to do certain things!', color=discord.Color.orange())
            remhome.set_footer(text='Page 1 of 1')
            remhome.set_thumbnail(url='https://cdn.discordapp.com/attachments/697569265913692171/697569662547918858/MultiSquid_pfp.png')
            remhome.set_author(name='MultiSquid', icon_url='https://cdn.discordapp.com/attachments/697569265913692171/697569662547918858/MultiSquid_pfp.png')
            remhome.add_field(name='Emote Key', value='⏰: Set Reminder\n\n❌: Remove Reminder\n\n📝: Reminder List\n\n⬅: Brings you back to the reminders homepage', inline=True)
            await message.edit (content=None, embed=remhome)
            await message.remove_reaction (reaction, user)
            for r in ['⬅']: await message.add_reaction(r)
        

def setup(client):
    client.add_cog(Tentacles(client))