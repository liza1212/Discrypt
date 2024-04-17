import discord
import re
import requests

from dotenv import load_dotenv
import os

load_dotenv()
my_token = os.getenv("TOKEN_ID")
# print(my_token)

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
    
    url="http://0.0.0.0:106/"
    length1= len(message.content.split(" "))
    res=requests.get(url, params={"data":message.content}).text
    
#   Extracting the output message 
    out_put=re.search("### Masked Output: ", res)
    result = str(res[out_put.span()[1]:])
    # result= result.replace("<MSG>", " ")
    r_message = re.search("\[([A-Z0-9]+)\]", result)
    if (r_message):
        masks = r_message.group(1).isupper()

    if masks:
        result = result.replace("[", "||")
        result = result.replace("]", "||")
        
        # length2=len(result.split(" "))
        
        new_result= result.split(" ")[:length1]
        new_result=" ".join(new_result)
        await message.delete() #[, ] -> ||
        #await message.channel.send("@" + str(message.author) + ": " + edited_message)
        await message.channel.send(f"```{str(message.author)}'s message contained personal information:``` {new_result}")
        
    # await message.channel.send(result)
    

client.run(my_token)