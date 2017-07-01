import discord, json
from discord.ext import commands
from platform import python_version

global startup_exts
startup_exts = ['runes', 'monsters']
jsonpath = "./summoner.json"

try:
    with open(jsonpath, 'r+') as security:
        sec = json.load(security)
        botToken = sec["bot"]["token"]
        ownerid = sec["bot"]["ownerid"]
except FileNotFoundError:
    exit("{0} not found. Exiting...".format(jsonpath))

description = "SummonersBot Discord Bot by Rising Lightmagic."
bot_prefix = "?"

client = commands.Bot(description=description, command_prefix=bot_prefix)


@client.event
async def on_ready():
    onlineMSG = "* Logged in as '{0}' ({1}). *".format(client.user.name, client.user.id)
    dversionMSG = "Discord API v{0}".format(discord.__version__)
    pversionMSG = "Python3 v{0}".format(python_version())
    onDIV = '*'
    while len(onDIV) < len(onlineMSG):
        onDIV = onDIV + '*'
    onLEN = len(onlineMSG) - 2
    while len(dversionMSG) < onLEN:
        dversionMSG = ' ' + dversionMSG
        if len(dversionMSG) < onLEN:
            dversionMSG = dversionMSG + ' '
    dversionMSG = '*' + dversionMSG + '*'
    while len(pversionMSG) < onLEN:
        pversionMSG = ' ' + pversionMSG
        if len(pversionMSG) < onLEN:
            pversionMSG = pversionMSG + ' '
    pversionMSG = '*' + pversionMSG + '*'
    print("{0}\n{1}\n{2}\n{3}\n{0}".format(onDIV, onlineMSG, dversionMSG, pversionMSG))
    if __name__ == '__main__':
        for extension in startup_exts:
            try:
                client.load_extension(extension)
                print('Loaded extension: {}'.format(extension))
            except Exception as e:
                exc = '{}: {}'.format(type(e).__name__, e)
                print('Failed to load extension: {}\n{}'.format(extension, exc))
    await client.change_presence(game=discord.Game(name="?monster"))

#def is_owner_check(message):
#    return message.author.id == ownerid

#def is_owner() -> object:
#    return commands.check(lambda ctx: is_owner_check(ctx.message))

#@client.command(pass_context=True,hidden=True)
#@is_owner()
#async def status(ctx):
#    await client.change_status(game=discord.Game(name="?monster"))
#    return

@client.command(pass_context=True)
async def ping(ctx):
    await client.say('Pong')
    return

client.run(botToken)