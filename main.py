import os
import discord
from dotenv import load_dotenv

load_dotenv()

client = discord.Client()
token =  os.environ['DISCORD_TOKEN'] 

@client.event
async def on_ready():
  print('We have logged in as {0.user}'
  .format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return 
  
  if message.content.startswith('&'):
    await resolve_message(message)


async def resolve_message(message):
  try: 
    if message.content.startswith('&help'):
      availableCommands = [ 
        "&pin <message id> -- A message with that id will be pinned. To get this ID, simply click on the triple dots and select 'Copy ID' at the dropdown.",
        "&unpin <message id> -- A Message that id will be unpinned. See above."
      ]
      await message.channel.send(""" 
      I'm capable of the following: 
      `&pin <message id> --- A message with that id will be pinned. To get this ID, simply click on the triple dots and select 'Copy ID' at the dropdown.
      &unpin <message id> --- A message with that id will be unpinned. See above.` """)
    if message.content.startswith('&pin'):
      await resolve_pin(message)
    if message.content.startswith('&unpin'):
      await resolve_unpin(message)
  except: 
    await message.channel.send("Well now, *something* was wrong with that query. Have you checked the &help?")
async def resolve_pin(message):
  messageArray = message.content.split(' ')
  messageId = messageArray[1]
  messageToPin = await message.channel.fetch_message(int(messageId))
  if messageToPin:
    await messageToPin.pin()
  else:
    await message.channel.send("That message doesn't seem to exist. Are you sure that format is correct?")
async def resolve_unpin(message):
  messageArray = message.content.split(' ')
  messageId = messageArray[1]
  messageToPin = await message.channel.fetch_message(int(messageId))
  if messageToPin:
    await messageToPin.unpin()
  else:
    await message.channel.send("That message doesn't seem to exist. Are you sure that format is correct?")

print
client.run(token)