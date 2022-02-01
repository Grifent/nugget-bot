import discord
from discord.ext import commands

class General(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def hello(self,ctx):
    await ctx.send("Well howdy, nugget!")

  @commands.command(name='status', help='Change the bot\'s activity message in discord.\
                    \n\nTypes:\n0 - Playing\n1 - Streaming\n2 - Listening to\n3 - Watching'\
                    , aliases=['presence'])
  async def status(self,ctx,type: int,*,activity: str):
    try:
      await self.client.change_presence(activity = discord.Activity(name=activity, type = discord.ActivityType(type)))
      await ctx.send(f"Status updated to {discord.ActivityType(type).name} {activity}.")
      print(f"Status updated to {discord.ActivityType(type).name} {activity}.")
    except ValueError:
      await ctx.send("Enter a valid input, nugget!")
  
def setup(client):
  client.add_cog(General(client))