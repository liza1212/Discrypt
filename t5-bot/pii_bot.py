import discord
from model import mask_prediction
import re
from dotenv import load_dotenv
import os

load_dotenv()
my_token = os.getenv("TOKEN_ID")
print(my_token)

intents = discord.Intents.default()
intents.messages = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to discord')

@client.event
async def on_message(message):
    masks = False
    if message.author == client.user:
        return
    
    print(message)
    #if message.content.startswith(".mask"):

    edited_message = mask_prediction(message.content)
    edited_message = edited_message.replace("<pad>", " ")
    edited_message = edited_message.replace("<unk>", "")
    edited_message = edited_message.replace("</s>", ".")

    r_message = re.search("\[([A-Z0-9]+)\]", edited_message)
    if (r_message):
        masks = r_message.group(1).isupper()

    if masks:
        edited_message = edited_message.replace("[", "||")
        edited_message = edited_message.replace("]", "||")
        await message.delete() #[, ] -> ||
        #await message.channel.send("@" + str(message.author) + ": " + edited_message)
        await message.channel.send(f"```{str(message.author)}'s message contained personal information:``` {edited_message}")

client.run(my_token)