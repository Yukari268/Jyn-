import discord
from discord.ext import commands

class Cog(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    @commands.command(brief=':Tải lên một cái cogs\n')
    async def load(self, ctx, extension):
        self.client.load_extension(f'Cogs.{extension}')

    @commands.command(brief=':Không tải cogs nữa\n')
    async def unload(self, ctx, extension):
        self.client.unload_extension(f'Cogs.{extension}')

    @commands.command(brief=":Tải lại một cái cogs\n")
    async def reload(self, ctx, extension):
        self.client.unload_extension(f'Cogs.{extension}')
        self.client.load_extension(f'Cogs.{extension}')


def setup(client):
    client.add_cog(Cog(client))