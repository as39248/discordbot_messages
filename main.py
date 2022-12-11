import discord

intents = discord.Intents.all()
intents.messages = True
client = discord.Client(intents=intents)
# add contents that you want to ban in the list in String form
ban_list = []


@client.event
async def on_message(message):
    sent_content = message.content
    for i in range(len(ban_list)):
        if ban_list[i] in sent_content:
            await message.delete()

    username = str(message.author)
    channel = str(message.channel)
    msg_time = str(message.created_at)

    chat_log = open(f'{channel}.txt', 'a+')
    chat_log.write(f'{username} sent: "{sent_content}" at {msg_time} \n')
    chat_log.close()

    print(f'{username} sent: "{sent_content}" at {msg_time}')
    
# add discord bot token 
client.run()
