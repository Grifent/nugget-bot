import discord
from discord.ext import commands
import asyncio

class NoVoiceClient(commands.CommandError):
  pass

class General(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command(name='hello', help='Howdy!', aliases=['hi'])
  async def hello(self,ctx):
    await ctx.send("Well howdy, nugget!")

  @commands.command(name='status', help='Change the bot\'s activity message in discord.\
                    \n\nTypes:\n0 - Playing\n1 - Streaming\n2 - Listening to\n3 - Watching'\
                    , aliases=['presence'])
  async def status(self, ctx, type: int, *, activity: str):
    try:
      await self.client.change_presence(activity = discord.Activity(name=activity, type = discord.ActivityType(type)))
      await ctx.send(f"Status updated to {discord.ActivityType(type).name} {activity}.")
      print(f"Status updated to {discord.ActivityType(type).name} {activity}.")
    except ValueError:
      await ctx.send("Enter a valid input, nugget!")

  @commands.command(name='spank', help='Spank a bad nugget for specified time, default 60 seconds. Use @user or "user" to specify the bad nugget.')
  @commands.has_guild_permissions(mute_members=True)
  async def spank(self, ctx, user: discord.Member, time = 60):
    if user.voice is None:
      raise NoVoiceClient
    else:
      print(f"Spanking {user} for {time} secs.")
      await user.edit(reason="Spanked!", mute = True)
      msg = await ctx.send(f"Consider yourself spanked, {user.mention}! Come back in {time} seconds.")
      await msg.add_reaction("🤣")
      await msg.add_reaction("🗿")
      await msg.add_reaction("💯")
      await asyncio.sleep(time)
      print(f"Unspanking {user}.")
      await user.edit(mute = False) # unmute after specified time

  @spank.error
  async def spank_error(self, ctx, error):
    print(f"Error in Spank - {error.__class__.__name__}: {error}")

    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.send("You forgot something, nugget! Try again!")
    elif isinstance(error, commands.MemberNotFound): 
      await ctx.send('Enter a real user, nugget!')
    elif isinstance(error, NoVoiceClient):
      await ctx.send("They ain't speaking, nugget!")
    elif isinstance(error, commands.CheckFailure):
      await ctx.send("We've got an imposter among us ඞඞඞඞඞඞඞඞඞඞ (You can't do that, nugget!)")
    elif isinstance(error, commands.BadArgument):
      await ctx.send("Fix your command, nugget!")
    else:
      # await ctx.send("Something went wrong!")
      pass
  
def setup(client):
  client.add_cog(General(client))