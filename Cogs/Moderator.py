import discord
from discord.ext import commands

class Moderator(commands.Cog, command_attrs=dict(hidden=True)):          
    def __init__(self, client):
        self.client = client

    @commands.command(brief=':Kick một thành viên!\n',aliases = ['k'])
    @commands.has_guild_permissions(kick_members = True)
    async def kick(self,ctx, member : discord.Member, *, reasons = None):
        await member.kick(reason = reasons)
        await ctx.send(f'Kicked {member.name}!')
    
    
    @commands.command(brief=':Ban một thành viên!\n')
    @commands.has_guild_permissions(ban_members = True)
    async def ban(self,ctx, member : discord.Member, * , reasons = None):
        await member.ban(reason = reasons)
        await ctx.send(f'Banned !{member.name}')
        

    
    @commands.command(brief=':Unban một thành viên!\n')
    @commands.has_guild_permissions(ban_members = True)
    async def unban(self,ctx, *, member):
        member_name, memeber_discriminator = member.split('#')
        banned_users = await ctx.guild.bans()

        for user in banned_users:
            unbanned_user = user.user
            if (unbanned_user.name, unbanned_user.discriminator) == (member_name, memeber_discriminator):
                await ctx.guild.unban(unbanned_user)
                await ctx.send(f'Unbanned {unbanned_user.mention}')
                return

    @commands.command(aliases = ['clear','reset','xóa'],brief=':xóa n tin nhắn\n')
    @commands.has_guild_permissions(manage_messages = True)
    async def purge(self,ctx, amount = 2):
        await ctx.channel.purge(limit = amount + 1) #plus one to delete the command itself

def setup(client):
    client.add_cog(Moderator(client))