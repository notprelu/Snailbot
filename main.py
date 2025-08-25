import discord
from discord import app_commands, message
import os
import requests
from requests.api import request
import asyncio




def detirmen_le_snail(Person, Message):
    print(Person)
    print(Message)
    prompt = ":3"
    chat = [
        {"role": "system", "content": prompt},
        {"role": "user", "content": f"Message from Person: {Person} Message:{Message}"}
    ]
    response = requests.post(
        "http://localhost:11434/api/chat",
        json={
            "model": "llama3",
            "messages": chat,
            "stream": False
        }
    )
    decision = response.json()["message"]["content"].strip().lower()
    return decision == "yes"

TOKEN = str(os.environ.get('snail_auth')) #SNAIL AUTH >:D
GUILD_ID = ":3"

import json
token = ""
guildid = int
with open("creds.json","r") as file:
    data = json.load(file)
    TOKEN = data["TOKEN"]
    GUILD_ID = data["GUILD_ID"]




intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
    await tree.sync(guild=discord.Object(id=GUILD_ID))
    print("Context command synced.")
    await client.change_presence(status=discord.Status.online, activity=discord.Game(name="Snailing it up in this bitch"))





@tree.context_menu(name="Snail", guild=discord.Object(id=GUILD_ID))
async def snail_log(interaction: discord.Interaction, message: discord.Message):
    await interaction.response.defer(thinking=True)
    await asyncio.sleep(4)
    if (detirmen_le_snail(message.author.name, message.content)) == True:
        await message.add_reaction("🐌")
        await interaction.followup.send("I do say this is a snail worthy message 🐌")
    else:
        await interaction.followup.send("fuck you not 🐌 worthy")



client.run(TOKEN)
