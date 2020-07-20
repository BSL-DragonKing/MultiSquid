print('⚙ Starting Up! ⬆')
print('Starting to Import files and add-ons')
import discord
from discord.ext import commands
import Fun
import Moderation
import Reminders
from Secure import * #<=== Asterik helps recognize that it imports everything from that one file
import Tentacles
import datetime
import random
import os

client = commands.Bot(command_prefix = '-')
client.remove_command('help')

@client.event
async def on_ready():
    #await client.change_presence(status=discord.Status.idle, activity=discord.Activity(name='⛱ Diving into the ocean 🏄‍♂️'))
    cogs = ['Fun', 'Moderation', 'Reminders', 'Tentacles'] #this would be a list containing the names of the files of the cogs you want to use, as of now, like Fun, Moderation, and Reminders for example
    for cog in cogs:
        client.load_extension(cog)
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(name='🌊 with Dolphins! 🐬', type=discord.ActivityType.playing))
    print('Imported Cogs!')
    print('🌊 Swam to The Ocean! 🏄‍♂️')

@client.command()
async def help(ctx): #Brings out the list of commands a user can use with this client
    helpg = discord.Embed(title='⚙ My Commands ⚙', description='This is the place where you can view all the commands that can use me', timestamp=datetime.datetime.utcnow(), color=discord.Color.blurple())
    helpg.set_author(name='MultiSquid', icon_url='https://cdn.discordapp.com/attachments/697569265913692171/697569662547918858/MultiSquid_pfp.png')
    helpg.add_field(name='🌊 MultiSquid General Commands 🦑', value='**Help** - Gets you here\n**Invite** - Give you the invite link to invite this client to a server of your choice\n**Support** - Gives you the link to offical support server for MultiSquid\n**About** - Brings out an embed message of a brief description about the client\n**Website** - Brings up the offical MultiSquid Website', inline=False)
    helpg.add_field(name='👮‍♂️ Moderation Commands 👢', value='**Clear** - Clears a certain amount of messages and provide a number after the argument (If a number isn\'t the client default is set to clear 5 messages)\n**Kick** - Kicks a member from your server (Use the @ to kick the member)\n**Ban** - Bans a member from your server (Use the @ to ban the member)\n**Unban** - Unbans user from your server (To use type "Discord Username of banned user + Number of their Discord Discriminator")\n**Mute** - Mutes a certain member (To use this please @ the person after the command)\n**Unmute** - Unmutes a certain member (To use this please @ the person after the command)', inline=False)
    helpg.add_field(name='📅 MultiSquid Reminder Commands ⏰', value='**Reminder** - Brings up my reminders page for you\n**Date** - Brings up today\'s date\n**Time** - Brings up just the time\n**Mtime** - Similar to time but brings up the time in military form', inline=False)
    helpg.add_field(name='🔮 Fun Commands 🎱', value='**8ball** - This command is kind of like a magic eight ball 🎱 and may give you forbideen advice that no one knows about other than the ball itself 👀. (To use this command please state your question after typing in the command)\n**Ping1** - Measures the amount of ping from when you *send the message*\n**Ping2** - Measures the ping between *the client itself*', inline=False)
    await ctx.send(embed=helpg)

@client.command()
async def helpp(ctx):
    if ctx.author.id in []:
        helpf = discord.Embed(title='Friends from PVI', timestamp=datetime.datetime.utcnow(), color=0xf0ff8f)
        helpf.set_footer(text='Page 1 of 1')
        helpf.set_author(name='MultiSquid', icon_url='https://cdn.discordapp.com/attachments/697569265913692171/697569662547918858/MultiSquid_pfp.png')
        helpf.add_field(name='Commands',value='Coming soon...')
        await ctx.send(embed=helpf)

@client.command()
async def helpj(ctx):
    if ctx.author.id in [507002318420574208, 661258412721438762]:
        helpj = discord.Embed(title='Friend Commands Help', timestamp=datetime.datetime.utcnow(), color=0xffaf8f)
        helpj.set_author(name='MultiSquid', icon_url='https://cdn.discordapp.com/attachments/697569265913692171/697569662547918858/MultiSquid_pfp.png')
        helpj.add_field(name=f'@661258412721438762', value=f'**Pup** - Brings you puppy commands for when your sad 😭')
        await ctx.send(embed=helpj)
    elif not ctx.author.id in [507002318420574208, 661258412721438762]:
        await ctx.send('Sorry this command is not avaliable to you! 😢')

@client.command()
async def support(ctx):
    await ctx.send(f'Here is the link to my support server if you have any trouble with me\nhttps://discord.gg/g69T4pU')

@client.command()
async def invite(ctx):
    await ctx.send(f'https://discord.com/api/oauth2/authorize?client_id=693885422136197210&permissions=8&scope=bot')

@client.command()
async def website(ctx):
    await ctx.send(f'http://tylerwu.com/')

@client.command()
async def github(ctx):
    await ctx.send(f'https://github.com/BSL-DragonKing/MultiSquid')


@client.command()
async def vote(ctx):
    waves = client.get_emoji(713896753815879692)
    await ctx.send(f'{waves}Coming Soon...{waves}')

@client.command()
async def about(ctx):
    embed = discord.Embed(title = 'About MultiSquid', description = 'The information below is some information you can learn a little about MultiSquid.', timestamp=datetime.datetime.utcnow(), color = discord.Color.magenta())
    embed.set_image(url='https://cdn.discordapp.com/attachments/697569265913692171/697569662547918858/MultiSquid_pfp.png7')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/697569265913692171/697569662547918858/MultiSquid_pfp.png')
    embed.set_author(name='MultiSquid', icon_url='https://cdn.discordapp.com/attachments/697569265913692171/697569662547918858/MultiSquid_pfp.png')
    embed.add_field(name='**Creation Date**', value='3/28/2020', inline=False)
    embed.add_field(name='**Creator**', value=f'@BSL_DragonKing#2355', inline=False)
    embed.add_field(name='**Website**', value='http://tylerwu.com/')
    embed.add_field(name='**GitHub**', value='https://github.com/BSL-DragonKing/MultiSquid')
    embed.url(name='**Support Server**', value='https://discord.gg/g69T4pU', inline=False)
    embed.add_field(name='**Top.gg Page**', value='Coming soon...', inline=False)
    await ctx.send(embed=embed)

@client.command()
async def ticket(self, ctx):
    pass

@client.event #This shows a message when something is incomplete and the bot needs a 'clarification' its kind of like a reminder
async def on_commands_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please put in all the things you need to work this command.')

#Everything below this line is more for the bot to sending pictures to certian people

WinWumpus = 'G:/My Drive/Pictures/Wumpus'
WinOMGITSAPUP = 'G:/My Drive/Pictures/Puppies'
WinPVIFAM = 'G:/My Drive/Pictures/PVI Friends/iCloud Photos'

MacWumpus = '/Volumes/GoogleDrive/My Drive/Pictures/Wumpus'
MacOMGITSAPUP = '/Volumes/GoogleDrive/My Drive/Pictures/Puppies'
MacPVIFAM = '/Volumes/GoogleDrive/My Drive/Pictures/PVI Friends'

#Note that these extra variables are used for when you switch from Windows and Mac OS's please make sure that they're inputed correctly otherwise the code will run into an error

@client.command()
async def dm(ctx):
    await ctx.author.send(f'This is your DM!')

@commands.is_owner()
@client.command()
async def wumpus(ctx):
    if ctx.author.id in [507002318420574208]:
        image = False
        directory = os.listdir(WinWumpus)
        while not image:
            result = random.randint(0, len(directory) - 1)
            if '.ini' not in directory[result]: image = True
        path = f'{WinWumpus}/{directory[result]}'
        f = discord.File(path)
        e = discord.Embed(title=f'The Discord Wumpus',color=0x129cff)
        e.set_image(url=f'attachment://{f.filename}')
        await ctx.send(embed=e,file=f)
    elif not ctx.author.id in [507002318420574208]:
        await ctx.send('Sorry this command is not avaliable to you! 😢')

@client.command()
async def pup(ctx):
    if ctx.author.id in [507002318420574208, 661258412721438762]:
        image = False
        directory = os.listdir(WinOMGITSAPUP)
        while not image:
            result = random.randint(0, len(directory) - 1)
            if '.ini' not in directory[result]: image = True
        path = f'{WinOMGITSAPUP}/{directory[result]}'
        f = discord.File(path)
        e = discord.Embed(title=f'🐕  Puppies!  🐶',color=0x61fa37)
        e.set_image(url=f'attachment://{f.filename}')
        await ctx.send(embed=e,file=f)
    elif not ctx.author.id in [507002318420574208, 661258412721438762]:
        await ctx.send('Sorry this command is not avaliable to you! 😢')

@client.command() #All of this is an example for an embed message
async def embedex(ctx):
    embed = discord.Embed(title = 'Title', description = 'This is a description.', timestamp=datetime.datetime.utcnow(), color = discord.Color.blue())
    embed.set_footer(text='This is a footer.')
    embed.set_image(url='https://cdn.discordapp.com/attachments/697569265913692171/697569662547918858/MultiSquid_pfp.png7')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/697569265913692171/697569662547918858/MultiSquid_pfp.png')
    embed.set_author(name='Author name', icon_url='https://cdn.discordapp.com/attachments/697569265913692171/697569662547918858/MultiSquid_pfp.png')
    embed.set_image(url='https://cdn.discordapp.com/attachments/697569265913692171/697569662547918858/MultiSquid_pfp.png')
    embed.add_field(name='Field Name', value='Field Value', inline=False)
    embed.add_field(name='Field Name', value='Field Value', inline=False)
    embed.add_field(name='Field Name', value='Field Value', inline=True)

    await ctx.send(embed=embed)

#Everything below this line is most likely to be past code, references, or things I can use later on  in bot code

#@client.event #This will send a message when the member joins ur server
#async def on_member_join(member):
#    channel = discord.utils.get(member.guild.channels, name='join-and-leave')
#    await channel.send(f'Welcome to {member.guild.name} Discord Server, {member.mention}')

#@client.event #This will send a message when the member leaves your server
#async def on_member_remove(member):
#    channel = discord.utils.get(member.guild.channels, name='join-and-leave')
#    await channel.send(f'{member.name} has left the Discord Server')

#@client.command()
#async def #whatever you want to name the command (ctx):
#    if ctx.author.id in [#put the user ID's/channel ID's in this section]:
#        image = False
#        directory = os.listdir(#files from the images)
#        while not image:
#            result = random.randint(0, len(directory) - 1)
#            if '.ini' not in directory[result]: image = True
#        path = f'{#file from the images}/{directory[result]}'
#        f = discord.File(path)
#        e = discord.Embed(title=f'#the title', description=f'#the description',color=#choose the color)
#        e.set_image(url=f'attachment://{f.filename}')
#        await ctx.send(embed=e,file=f)

# KeyWords when typing python
#False      await      else       import     pass
#None       break      except     in         raise
#True       class      finally    is         return
#and        continue   for        lambda     try
#as         def        from       nonlocal   while
#assert     del        global     not        with
#async      elif       if         or         yield

# easterAnnouncement.start()
# @tasks.loop(minutes=1)#example on how to get the bot to make an announcment on every server it is available on a certain day
# async def easterAnnouncement():
#     if datetime.datetime.now().strftime('%m %d %y %H:%M') == '04 12 20 06:00':
#         for server in bot.guilds:
#             try: await (await database.CalculateAnnouncementsChannel(server, True)).send('🐰🥚✝ Happy Easter! ✝🥚🐰\n\nWishing every one of you a happy and blessed day filled with new life no matter what the state of the world may be right now,\nRicoViking9000, the developer of Disguard')

client.run(token)#This is the line that takes the token from another file in order to run this bot code. If I included my bot token here anyone can use the bot however they want