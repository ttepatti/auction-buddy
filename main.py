import discord
from discord.ext import commands
import requests
import os
import dotenv

# Load environment variables from .env file
dotenv.load_dotenv()

#db = dataset.connect("sqlite:///alerts.db")
        
description = "Auction Buddy"

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", description=description, intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}! (ID: {bot.user.id})')
    print('------')

@bot.command(
    name="addalert",
    help="Add a new alert for an item",
    require_var_positional=True
)
async def add_alert(ctx, itemname):
    print(f"Adding new alert for: {itemname}")
    await ctx.reply(f"New alert added for: {itemname}")

@add_alert.error
async def add_alert_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        print("add_alert - User did not provide item name. Returning error.")
        await ctx.reply("Error: You must provide an item name!")

@bot.command(
    name="delalert",
    help="Remove an alert for an item",
    require_var_positional=True
)
async def del_alert(ctx, itemname):
    print(f"Removing alert for {itemname}")
    await ctx.reply(f"Removed alert for: {itemname}")

@del_alert.error
async def del_alert_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        print("del_alert - User did not provide item name. Returning error.")
        await ctx.reply("Error: You must provide an item name!")

@bot.command(
    name="listalerts",
    help="List all configured alerts"
)
async def list_alerts(ctx):
    print("Listing all alerts")
    await ctx.send("Current alerts:")

bot.run(os.environ["BOT_TOKEN"])