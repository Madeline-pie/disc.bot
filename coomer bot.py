import discord
import random

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    #if message.content.startswith('$hello'):
    try:
        message_lowercase = ''
        message_lowercase_but_not_awesome = message.content.split('?')

        ## print("dicks", message_lowercase_but_not_awesome) ##
        
        for i in message_lowercase_but_not_awesome:
          message_lowercase += i
          ## print(message_lowercase)##
        
        message_lowercase = message_lowercase.lower()
        print(message_lowercase)
              
        if message_lowercase.startswith('should i beat off'):
            if random.randint(1,3) == 1:
                await message.channel.send('Yes, baby~')
            else:
                await message.channel.send('No, horny whore!')
        else:
            return None
    except:
        return None
      

client.run('NzY2MzQ3MTUzNTQ3MTk4NDY0.X4iCZw.J4C-PeD_B9dJ3JcZh7MZRoxqeHY')
