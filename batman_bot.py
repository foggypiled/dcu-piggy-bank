import os
import re
import discord

TOKEN = os.environ["DISCORD_BOT_TOKEN"]

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

batman_counts: dict[int, int] = {}

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
    re.IGNORECASE
)

def count_triggers(text: str) -> int:
    return len(TRIGGERS.findall(text))

def ordinal_nickels(count: int) -> str:
    return f"{count} nickel{'s' if count != 1 else ''}"

@client.event
async def on_ready():
    await client.change_presence(activity=discord.CustomActivity(
        name="You wanna say Batman soooo bad 🦇."
    ))
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return

    occurrences = count_triggers(message.content)
    if occurrences == 0:
        return

    user_id = message.author.id
    batman_counts[user_id] = batman_counts.get(user_id, 0) + occurrences
    total = batman_counts[user_id]

    await message.channel.send(
        f"You owe the LadyDevilofHell'sKitchen {total} nickels, {message.author.mention}!"
    )

client.run(MTQ5MjExNjc0NzEwMzI0MDQwMw.GPArJU.yFxNYmTppkxsGRbrD0ew3rOzhmujUXgRXTh-no)
