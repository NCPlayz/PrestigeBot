import discord
from discord.ext import commands
import random
import json
import time

class Currency:
	def __init__(self, bot: commands.Bot):
		self.bot = bot

	@commands.command(hidden=True, aliases=['dailyclaim', 'claim', 'dailybalance', 'atmclaim'])
	async def daily(self, ctx):
		userinfo = {}
		with open('userbalance.json', 'r') as f:
			userinfo = json.load(f)
		if str(ctx.author.id) not in userinfo:
			userinfo[str(ctx.author.id)] = {}
			userinfo[str(ctx.author.id)]["balance"] = 250
			userinfo[str(ctx.author.id)]["lastclaimed"] = time.time()
			balance = userinfo[str(ctx.author.id)]["balance"]
			with open('userbalance.json', 'w') as f:
				json.dump(userinfo, f)
			emb = discord.Embed(title='\U0001f3e7 Royal Bank of Prestige', colour=0xC500FF)
			emb.add_field(name='Amount Claimed', value="250 \U0001f4b3", inline=False)
			emb.add_field(name='Balance', value=str(balance) + ' \U0001f4b3', inline=False)
			await ctx.send(embed=emb)
		elif str(ctx.author.id) in userinfo:
			timesince = userinfo[str(ctx.author.id)]["lastclaimed"] + 86400
			if timesince < time.time():
				initialbalance = userinfo[str(ctx.author.id)]["balance"]
				newbalance = initialbalance + 250
				userinfo[str(ctx.author.id)]["balance"] = newbalance
				userinfo[str(ctx.author.id)]["lastclaimed"] = time.time()
				with open('userbalance.json', 'w') as f:
					json.dump(userinfo, f)
				balance = userinfo[str(ctx.author.id)]["balance"]
				emb = discord.Embed(title='\U0001f3e7 Royal Bank of Prestige', colour=0xC500FF)
				emb.add_field(name='Amount Claimed', value="250 \U0001f4b3", inline=False)
				emb.add_field(name='Balance', value=str(balance) + ' \U0001f4b3', inline=False)
				await ctx.send(embed=emb)
			else:
				balance = userinfo[str(ctx.author.id)]["balance"]
				timeclaimed = userinfo[str(ctx.author.id)]["lastclaimed"]
				timems = 0
				timems = timeclaimed + 86400
				timefinal = 0
				timefinal = timems - time.time()
				timehours = 0
				timehours = timefinal / 3600
				timeminutes = 0
				timehold = 0

				timehold = timefinal % 3600
				timeminutes = timehold / 60

				timefinalhours = int(timehours)
				timefinalminutes = int(timeminutes)

				if timefinalhours < 1:
					timefinalhours = 0

				if timefinalminutes < 1:
					timefinalminutes = 0
				emb = discord.Embed(title='\U0001f3e7 Royal Bank of Prestige', colour=0xC500FF)
				emb.add_field(name='Next Claim For User', value=str(timefinalhours) + 'H ' + str(timefinalminutes) + 'M', inline=False)
				await ctx.send(embed=emb)

	@commands.command(hidden=True, aliases=['currentbalance'])
	async def balance(self, ctx, accountID: discord.Member = None):
		userinfo = {}
		with open('userbalance.json', 'r') as f:
			userinfo = json.load(f)
		if accountID == None:
			'''
			So.... Over here you see loads of jumble... if you don't like it... well...
			I don't really give a shit.... I'm crap with numbers and you need to  get used to it...
			Numbers in jumble... Well expect it in my code
			'''
			balance = userinfo[str(ctx.author.id)]["balance"]
			timeclaimed = userinfo[str(ctx.author.id)]["lastclaimed"]
			timems = 0
			timems = timeclaimed + 86400
			timefinal = 0
			timefinal = timems - time.time()
			timehours = 0
			timehours = timefinal / 3600
			timeminutes = 0
			timehold = 0

			timehold = timefinal % 3600
			timeminutes = timehold / 60

			timefinalhours = int(timehours)
			timefinalminutes = int(timeminutes)

			if timefinalhours < 1:
				timefinalhours = 0

			if timefinalminutes < 1:
				timefinalminutes = 0

			emb = discord.Embed(title='\U0001f3e7 Royal Bank of Prestige', colour=0xC500FF)
			emb.add_field(name='Balance', value=str(balance) + ' \U0001f4b3', inline=False)
			emb.add_field(name='Next Claim', value=str(timefinalhours) + 'H ' + str(timefinalminutes) + 'M', inline=False)
			await ctx.send(embed=emb)
		else:
			try:
				balance = userinfo[str(accountID.id)]["balance"]
				timeclaimed = userinfo[str(accountID.id)]["lastclaimed"]
				timems = 0
				timems = timeclaimed + 86400
				timefinal = 0
				timefinal = timems - time.time()
				timehours = 0
				timehours = timefinal / 3600
				timeminutes = 0
				timehold = 0

				timehold = timefinal % 3600
				timeminutes = timehold / 60

				timefinalhours = int(timehours)
				timefinalminutes = int(timeminutes)

				if timefinalhours < 1:
					timefinalhours = 0

				if timefinalminutes < 1:
					timefinalminutes = 0

				emb = discord.Embed(title='\U0001f3e7 Royal Bank of Prestige', colour=0xC500FF)
				emb.add_field(name='User', value=accountID)
				emb.add_field(name='Balance', value=str(balance) + ' \U0001f4b3', inline=False)
				emb.add_field(name='Next Claim', value=str(timefinalhours) + 'H ' + str(timefinalminutes) + 'M', inline=False)
				await ctx.send(embed=emb)
			except:
				emb = discord.Embed(title='\U0001f3e7 Royal Bank of Prestige', colour=0xC500FF)
				emb.add_field(name='Create Account', value="The user doesn't have an account but can easily create one via claiming their daily reward. Simply run the command $daily (change the prefix to the relevant server prefix!")
				await ctx.send(embed=emb)

	@commands.command(hidden=True)
	async def testing(self, ctx):
		userinfo = {}
		with open('userbalance.json', 'r') as f:
			userinfo = json.load(f)
		if str(ctx.author.id) in userinfo:
			initialbalance = userinfo[ctx.author.id]["balance"]
			newbalance = initialbalance + 250
			userinfo[ctx.author.id]["balance"] = newbalance
			userinfo[ctx.author.id]["lastclaimed"] = time.time()
			print(time.time())

	@commands.command(hidden=True, aliases=['haxor', 'haxthesystem', 'cheat', 'cheatcode', '1337leet', '1337leethaxor', '1337haxor', '1337haxorgive'])
	@commands.is_owner()
	async def haxorsomep(self, ctx, user: discord.Member, amount: int = None):
		holder = {}
		if amount == None:
			emb = discord.Embed(colour=0xff0c00)
			emb.add_field(name='\U0000274c Error', value='Amount is a required argument')
			await ctx.send(embed=emb)
		with open('userbalance.json', 'r') as f:
			holder = json.load(f)
		if str(user.id) not in holder:
			emb = discord.Embed(title='\U0001f3e7 Royal Bank of Prestige', colour=0xC500FF)
			emb.add_field(name='Create Account', value="The user doesn't have an account but can easily create one via claiming their daily reward. Simply run the command $daily (change the prefix to the relevant server prefix!")
			await ctx.send(embed=emb)
		else:
			originalbalance = holder[str(user.id)]["balance"]
			holder[str(user.id)]["balance"] = originalbalance + amount
			with open('userbalance.json', 'w') as f:
				json.dump(holder, f)
			newbalance = holder[str(user.id)]["balance"]
			emb = discord.Embed(title='\U0001f3e7 Royal Bank of Prestige', colour=0xC500FF)
			emb.add_field(name='User', value=user)
			emb.add_field(name='Original Balance', value=str(originalbalance) + ' \U0001f4b3', inline=False)
			emb.add_field(name='New Balance', value=str(newbalance) + ' \U0001f4b3', inline=False)
			await ctx.send(embed=emb)

	@commands.command(hidden=True, aliases=['haxordel', 'haxthesystemdel', 'cheatdel', 'cheatcodedel', '1337leetdel', '1337leethaxordel', '1337haxordel', '1337haxorgivedel'])
	@commands.is_owner()
	async def haxorsomepdel(self, ctx, user: discord.Member, amount: int = None):
		holder = {}
		if amount == None:
			emb = discord.Embed(colour=0xff0c00)
			emb.add_field(name='\U0000274c Error', value='Amount is a required argument')
			await ctx.send(embed=emb)
		with open('userbalance.json', 'r') as f:
			holder = json.load(f)
		if str(user.id) not in holder:
			emb = discord.Embed(title='\U0001f3e7 Royal Bank of Prestige', colour=0xC500FF)
			emb.add_field(name='Create Account', value="The user doesn't have an account but can easily create one via claiming their daily reward. Simply run the command $daily (change the prefix to the relevant server prefix!")
			await ctx.send(embed=emb)
		else:
			originalbalance = holder[str(user.id)]["balance"]
			holder[str(user.id)]["balance"] = originalbalance - amount
			with open('userbalance.json', 'w') as f:
				json.dump(holder, f)
			newbalance = holder[str(user.id)]["balance"]
			emb = discord.Embed(title='\U0001f3e7 Royal Bank of Prestige', colour=0xC500FF)
			emb.add_field(name='User', value=user)
			emb.add_field(name='Original Balance', value=str(originalbalance) + ' \U0001f4b3', inline=False)
			emb.add_field(name='New Balance', value=str(newbalance) + ' \U0001f4b3', inline=False)
			await ctx.send(embed=emb)

	@commands.group(invoke_without_command=True, pass_context=True, invoke_without_command=True)
	async def fish(self, ctx):
		emb = discord.Embed(title='\U0001f3a3 Prestige Fishing Association', colour=0xC500FF)
		emb.add_field(name='Help', value='Help Desc', inline=False)
		emb.add_field(name='Help', value='Help Desc', inline=False)
		emb.add_field(name='Help', value='Help Desc', inline=False)
		await ctx.send(embed=emb)

	@fish.command(pass_context=True, aliases=[''])
	async def test(self, ctx):
		ctx.send("This works boys")

	@fish.command(hidden=True)
	async def catch(self, ctx, bet: int = None):
		if bet == None:
			emb = discord.Embed(colour=0xff0c00)
			emb.add_field(name='\U0000274c Error', value='Bet is a required argument')
			await ctx.send(embed=emb)
		elif bet < 1:
			emb = discord.Embed(colour=0xff0c00)
			emb.add_field(name='\U0000274c Error', value='Bet is required to be a positive number')
			await ctx.send(embed=emb)
		else:
			#In progress

	@commands.command(hidden=True)
	async def slots(self, ctx, bet: int = None):
		if bet = None:
			emb = discord.Embed(colour=0xff0c00)
			emb.add_field(name='\U0000274c Error', value='Bet is a required argument')
			await ctx.send(embed=emb)
		elif bet < 1:
			emb = discord.Embed(colour=0xff0c00)
			emb.add_field(name='\U0000274c Error', value='Bet is required to be a positive number')
			await ctx.send(embed=emb)
		else:
			#In progress

def setup(bot):
	bot.add_cog(Currency(bot))
