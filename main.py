import discord

intents = discord.Intents.all()
intents.messages = True
client = discord.Client(intents=intents)
ban_list = ['https://images-ext-2.discordapp.net/external/oI2sB14yxXD8A5xKzRA2vt-XukTmKKlFiaQSyBVkBGI/https/im4.ezgif.com/tmp/ezgif-4-b9ea69a658.gif',
            'https://media.discordapp.net/attachments/1000878710041366598/1049200300868767764/caption_6.gif',
           'https://media.discordapp.net/attachments/1000878710041366598/1047281576150577192/20220410_141837.gif',
            'https://media.discordapp.net/attachments/1000878710041366598/1043123510274424832/image0-211.gif',
           'https://media2.giphy.com/media/E8M5aOqkzChemXhXwY/giphy.mp4?cid=73b8f7b15e53b4c2647cdeba781d2519bea91ede46ea87f0&rid=giphy.mp4&ct=g']


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


client.run(
    'MTA1MTI5NjQwMDk0OTkxOTgzNA.GWCM9u.upjg6ewcSXIHcKY2z5Kr8wzCvluHQkeO1FyU8g')
