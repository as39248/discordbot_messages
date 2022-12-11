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
    file1 = open('ChatHistory.txt', 'a')
    file1.write(f'{username} sent: "{sent_content}" in {channel} \n')
    file1.close()
    print(f'{username} sent: "{sent_content}" in {channel}')

# add discord bot token 
client.run()
