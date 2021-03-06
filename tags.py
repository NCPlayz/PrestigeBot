import discord
from discord.ext import commands
import random
import json

class Tags:
	def __init__(self, bot: commands.Bot):
		self.bot = bot

	@commands.group(invoke_without_command=True, pass_context=True, aliases=['tags'])
	async def tag(self, ctx, nameoftag: str = None):
		if nameoftag == None:
			emb = discord.Embed(colour=0xff0c00)
			emb.add_field(name='\U0000274c Error', value='Tag name is required')
			await ctx.send(embed=emb)
		else:
			tageodict = {}
			with open('tags.json', 'r') as f:
				tageodict = json.load(f)
			if nameoftag in tageodict[str(ctx.guild.id)][0]:
				await ctx.send(tageodict[str(ctx.guild.id)][0][nameoftag]["content"])
			else:
				emb = discord.Embed(colour=0xff0c00)
				emb.add_field(name='\U0000274c Error', value="Tag doesn't exist")
				await ctx.send(embed=emb)

	@tag.command(hidden=True)
	@commands.has_permissions(administrator=True)
	async def setupserver(self, ctx):
		holderdict = {}
		with open('tags.json', 'r') as f:
			holderdict = json.load(f)
		if str(ctx.guild.id) in holderdict:
			emb = discord.Embed(colour=0xff0c00)
			emb.add_field(name='\U0000274c Error', value='Server has already been setup')
			await ctx.send(embed=emb)
		else:
			holderdict[str(ctx.guild.id)] = [{"FirstTagEver": {"author_id": "350534218998349825", "content": "This Server's First Every Tag", "aliases": [], "uses": "2"}}]
			with open('tags.json', 'w') as f:
				json.dump(holderdict, f)
			emb = discord.Embed(colour=0xC500FF)
			emb.add_field(name='Status', value="Server has been setup")
			await ctx.send(embed=emb)

	@tag.command(hidden=True, aliases=['createtag', 'tagcreate', 'create'])
	async def maketag(self, ctx, tagname: str = None, *, tagcontent: str = None):
		prefixdict = {}
		with open('tags.json', 'r') as f:
			prefixdict = json.load(f)
		if tagname == None:
			emb = discord.Embed(colour=0xff0c00)
			emb.add_field(name='\U0000274c Error', value='Tag name is required')
			await ctx.send(embed=emb)
		elif tagcontent == None:
			emb = discord.Embed(colour=0xff0c00)
			emb.add_field(name='\U0000274c Error', value='Tag content is required')
			await ctx.send(embed=emb)
		elif tagname in prefixdict[str(ctx.guild.id)][0]:
			emb = discord.Embed(colour=0xff0c00)
			emb.add_field(name='\U0000274c Error', value='Tag exists')
			await ctx.send(embed=emb)
		else:
			prefixdict[str(ctx.guild.id)] = [{tagname: {"author_id": str(ctx.author.id), "content": tagcontent, "aliases": [], "uses": "0"}}]
			with open('tags.json', 'w') as f:
				json.dump(prefixdict, f)
			emb = discord.Embed(colour=0xC500FF)
			emb.add_field(name='Status', value=tagname + " is now a new tag!")
			await ctx.send(embed=emb)

	@tag.command(hidden=True, aliases=['change'])
	async def edit(self, ctx, tagname: str = None, *, tagcontent: str = None):
		prefixdict = {}
		with open('tags.json', 'r') as f:
			prefixdict = json.load(f)
		if tagname == None:
			emb = discord.Embed(colour=0xff0c00)
			emb.add_field(name='\U0000274c Error', value='Tag name is required')
			await ctx.send(embed=emb)
		elif tagcontent == None:
			emb = discord.Embed(colour=0xff0c00)
			emb.add_field(name='\U0000274c Error', value='Tag content is required')
			await ctx.send(embed=emb)
		elif prefixdict[str(ctx.guild.id)][0][tagname]["author_id"] != str(ctx.author.id):
			emb = discord.Embed(colour=0xff0c00)
			emb.add_field(name='\U0000274c Error', value="Tag doesn't belong to you")
			await ctx.send(embed=emb)
		else:
			prefixdict[str(ctx.guild.id)] = [{tagname: {"author_id": str(ctx.author.id), "content": tagcontent, "aliases": [], "uses": "0"}}]
			with open('tags.json', 'w') as f:
				json.dump(prefixdict, f)
			emb = discord.Embed(colour=0xC500FF)
			emb.add_field(name='Status', value=tagname + " has been edited!")
			await ctx.send(embed=emb)

	@tag.command(hidden=True, aliases=['usetag'])
	async def help(self, ctx):
		emb = discord.Embed(title='\U0001f3a3 Prestige Tags', colour=0xC500FF)
		emb.add_field(name='$tag setup', value='Setup tags on your server', inline=False)
		emb.add_field(name='$tag create <tagname> <content>', value='Create a new tag', inline=False)
		emb.add_field(name='$tag edit <tagname> <content>', value='Edit an existing tag', inline=False)
		emb.add_field(name='$tag delete <tagname>', value='Delete a tag', inline=False)
		await ctx.send(embed=emb)

	@tag.command(hidden=True, aliases=['tagdelete', 'removetag', 'tagremove', 'remove'])
	async def delete(self, ctx, nameoftag: str = None):
		if nameoftag == None:
			emb = discord.Embed(colour=0xff0c00)
			emb.add_field(name='\U0000274c Error', value='Tag name is required')
			await ctx.send(embed=emb)
		else:
			tageodict = {}
			with open('tags.json', 'r') as f:
				tageodict = json.load(f)
			if nameoftag in tageodict[str(ctx.guild.id)][0]:
				if str(ctx.author.id) == tageodict[str(ctx.guild.id)][0][nameoftag]["author_id"]:
					del tageodict[str(ctx.guild.id)][0][nameoftag]
					with open('tags.json', 'w') as f:
						json.dump(tageodict, f)
					emb = discord.Embed(colour=0xC500FF)
					emb.add_field(name='Status', value="Tag has been removed")
					await ctx.send(embed=emb)
				else:
					emb = discord.Embed(colour=0xff0c00)
					emb.add_field(name='\U0000274c Error', value='You are not the owner of this tag')
					await ctx.send(embed=emb)
			else:
				emb = discord.Embed(colour=0xff0c00)
				emb.add_field(name='\U0000274c Error', value="Tag doen't exist")
				await ctx.send(embed=emb)

	@tag.command(hidden=True)
	async def test(self, ctx):
		holderdictio = {}
		with open('tags.json', 'r') as f:
			holderdictio = json.load(f)
		await ctx.send(holderdictio[str(ctx.guild.id)][0]["FirstTagEver"]["content"])

def setup(bot):
	bot.add_cog(Tags(bot))