import discord
import random
import os
import datetime
from discord.ext import commands

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping1(self, ctx):
        await ctx.send(f'Pong! {round((datetime.datetime.utcnow() - ctx.message.created_at).microseconds / 1000)}ms')

    @commands.command()
    async def ping2(self, ctx):
        await ctx.send(f'Pong! {round(self.client.latency *1000)}ms')

    @commands.command()
    async def shrug(self, ctx):
        await ctx.send(f'🤷‍♂️🤷‍♂️🤷‍♂️🤷‍♂️🤷‍♂️🤷‍♂️🤷‍♂️')
        await ctx.message.delete()
        
    @commands.command()
    async def gaypride(self, ctx):
        await ctx.send(f'🌈 Don\'t worry it\'s okay to be gay 🏳‍🌈' )
        await ctx.message.delete()

    @commands.command()
    async def nou(self, ctx):
        await ctx.send(f'no u' )
        await ctx.message.delete()

    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, *, question):
        responses  = ['As I see it, yes.', 'Ask again later.', 'Better not tell you now.', 'Cannot predict now.', 'Concentrate and ask again.', 'Don’t count on it.', 'It is certain.', 'It is decidedly so.', 'Most likely.', 'My reply is no.', 'My sources say no.', 'Outlook not so good.', 'Outlook good.', 'Reply hazy, try again.', 'Signs point to yes.', 'Very doubtful.', 'Without a doubt.', 'Yes.', 'Yes – definitely.', 'You may rely on it.']
        await ctx.send(f'Question: {question}\nAnswers: {random.choice(responses)}')

def setup(client):
    client.add_cog(Fun(client))