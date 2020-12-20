import discord
from discord.ext import commands
import datetime
from datetime import datetime
import json

class Config(commands.Cog, name="Configuration"):
		
		def __init__(self, bot):
			self.bot = bot
			
		@commands.Cog.listener()
		async def on_ready(self):
			print(f"{self.__class__.__name__} Cog has been loaded\n-----")
			
		@commands.command()
		async def prefix(self, ctx, new_prefix):
		          with open("./prefixes.json", "r") as f:
		          	prefixes = json.load(f)
		          	
		          	prefixes[str(ctx.guild.id)] = new_prefix
		          	
		          	with open("./prefixes.json", "w") as f:
		          		json.dump(prefixes, f, indent=4)
		          		embed = discord.Embed(
		          		colour = discord.Colour.blurple(),
		          		title="Prefix Updated",
		          		description=None,
		          		timestamp=ctx.message.created_at
		          		)
		          		embed.add_field(name="New Prefix:", value=f"{new_prefix}", inline=True)
		          		embed.add_field(name="Example", value=f"{new_prefix}help", inline=True)
		          		await ctx.send(embed=embed)
		          		
		          		
		@commands.Cog.listener()
		async def on_guild_join(self, guild):
		       with open("./prefixes.json", "r") as f:
		       	prefixes = json.load(f)
		       	prefixes[str(guild.id)] = "!*"
		       	
		       	with open("./prefixes.json", "w") as f:
		       		json.dump(prefixes, f, indent=4)

		@commands.Cog.listener()
		async def on_guild_remove(self, guild):
		    with open("./prefixes.json", "r") as f:
		    	prefixes = json.load(f)
		    	
		    	prefixes.pop(str(guild.id))
		    	
		    	with open("./prefixes.json", "w") as f:
		    					json.dump(prefixes, f, indent=4)			
									
def setup(bot):
	bot.add_cog(Config(bot))