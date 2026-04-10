import os
import re
import discord
TOKEN = os.environ["DISCORD_BOT_TOKEN"]
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
user_counts: dict[int, int] = {}
TRIGGERS = re.compile(
    r"\b(?:"
    r"bat[\s.]*man"
    r"|super[\s]*man"
    r"|supergirl"
    r"|(?:the\s+)?flash"
    r"|green\s+arrow"
    r"|ultraman"
    r"|conquest"
    r"|lex\s+luth[eo]r"
    r")\b",
    re.IGNORECASE,
)
@client.event
async def on_ready():
    await client.change_presence(
        activity=discord.CustomActivity(name="You wanna say Batman soooo bad 🦇.")
    )
    print(f"Logged in as {client.user}")
@client.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return
    hits = len(TRIGGERS.findall(message.content))
    if hits == 0:
        return
    user_id = message.author.id
    user_counts[user_id] = user_counts.get(user_id, 0) + hits
    total = user_counts[user_id]
    await message.channel.send(
        f"You owe the LadyDevilofHell'sKitchen {total} nickels, {message.author.mention}!"
    )
client.run(TOKEN)
