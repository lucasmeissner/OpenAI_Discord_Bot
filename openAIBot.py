import discord
import openai
from random import randint

client = discord.Client()
guild = discord.Guild
openai.api_key = "API_KEY_HERE_BUT_IM_NOT_SHARING"

@client.event
async def on_message(message):
    cmd = ''
    count = 0
    if message.author == client.user:
        return
    elif message.content.startswith('$'):
        cmd = message.content.split()[0].replace("$","")
        print(cmd)
        parameters = message.content.split(' ')[1:]
        seperator = ' '
        parameters = seperator.join(parameters)
        print(parameters)

    if cmd == 'gpt':
        response = openai.Completion.create(
            engine="davinci",
            prompt="I am a highly intelligent question answering bot. If you ask me a question that is rooted in truth, I will give you the answer. If you ask me a question that is nonsense, trickery, or has no clear answer, I will respond with \"Unknown\".\n\nQ: What is human life expectancy in the United States?\nA: Human life expectancy in the United States is 78 years.\n\nQ: Who was president of the United States in 1955?\nA: Dwight D. Eisenhower was president of the United States in 1955.\n\nQ: Which party did he belong to?\nA: He belonged to the Republican Party.\n\nQ: What is the square root of banana?\nA: Unknown\n\nQ: How does a telescope work?\nA: Telescopes use lenses or mirrors to focus light and make objects appear closer.\n\nQ: Where were the 1992 Olympics held?\nA: The 1992 Olympics were held in Barcelona, Spain.\n\nQ: How many squigs are in a bonk?\nA: Unknown\n\nQ: " + parameters + "\nA:",
            temperature=0,
            max_tokens=120,
            top_p=1,                     
            frequency_penalty=0.0,
            presence_penalty=0.0,
            stop=["\n"])
        await message.channel.send(response.choices[0].text)
            
client.run('DISCORD_BOT_ID_GOES_HERE')