import discord
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive

client = discord.Client()
sad_words = ["sad", "depressed", "unhappy", "angry", "miserable"]
starter_encouragements = [
    "Cheer up!", "Hang in there.", "You are a great person / bot!"
]

#Name
part1 = ["Adam", "Sabrina", "Daniel", "Philipp", "Julia", "Shi", "Zero", "Fabi", "Sven", "Nils"]
#Anrede
part2 = ["halt dich fest,", "gönn dir,", "du Opfer,", "du Fisch,", "du Slutnugget,", "ma Nigga,", "mein Lieblingsfaggot,"]
#Aussage 1
part3 = ["es ist Obst im Haus", "was willst du machen", "es ist hart", "wir lieben dich", "Deutschland schafft sich ab"]
#Aussage 2
part4 = ["und es wird sich hier nichts ändern, egal ob du hier bist oder nicht.", "und die Illuminaten stecken dahinter.", "und jemand hats verkackt.", "und überall sind Kanacken."]
#Gruß
part5 = ["Ma Nigga", "Peace bro", "Liebe Grüße, Marcel Davis", "Deine Mama", "Keep smoking", "Geh dir einen Wichsen"]

starter_phrases = []
starter_phrases = [part1, part2, part3, part4, part5]


if "responding" not in db.keys():
    db["responding"] = True


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return (quote)


def update_encouragements(encouraging_message):
    if "encouragements" in db.keys():
        encouragements = db["encouragements"]
        encouragements.append(encouraging_message)
        db["encouragements"] = encouragements
    else:
        db["encouragements"] = [encouraging_message]


def delete_encouragements(index):
    encouragements = db["encouragements"]
    if len(encouragements) > index:
        del encouragements[index]
    db["encouragements"] = encouragements


def update_p1(phrase):
    if "p1" in db.keys():
        p1 = db["p1"]
        p1.append(phrase)
        db["p1"] = p1
    else:
        db["p1"] = [phrase]


def delete_p1(index):
    p1 = db["p1"]
    if len(p1) > index:
        del p1[index]
    db["p1"] = p1


def update_p2(phrase):
    if "p2" in db.keys():
        p2 = db["p2"]
        p2.append(phrase)
        db["p2"] = p2
    else:
        db["p2"] = [phrase]


def delete_p2(index):
    p2 = db["p2"]
    if len(p2) > index:
        del p2[index]
    db["p2"] = p2


def update_p3(phrase):
    if "p3" in db.keys():
        p3 = db["p3"]
        p3.append(phrase)
        db["p3"] = p3
    else:
        db["p3"] = [phrase]


def delete_p3(index):
    p3 = db["p3"]
    if len(p3) > index:
        del p3[index]
    db["p3"] = p3


def update_p4(phrase):
    if "p4" in db.keys():
        p4 = db["p4"]
        p4.append(phrase)
        db["p4"] = p4
    else:
        db["p4"] = [phrase]


def delete_p4(index):
    p4 = db["p4"]
    if len(p4) > index:
        del p4[index]
    db["p4"] = p4


def update_p5(phrase):
    if "p5" in db.keys():
        p5 = db["p5"]
        p5.append(phrase)
        db["p5"] = p5
    else:
        db["p5"] = [phrase]


def delete_p5(index):
    p5 = db["p5"]
    if len(p5) > index:
        del p5[index]
    db["p5"] = p5


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if msg.startswith('$hello'):
        await message.channel.send('```Hello ' + str(message.author).split("#")[0] + '!```')
        return
    
    if msg.startswith('$looki'):
        with open('handi.txt', 'r') as file:
            msg = file.read(1900).strip()
            while len(msg) > 0:
                await message.channel.send('```' + msg + '```')
                msg = file.read(1900).strip()
        return

    if msg.startswith('$lookw'):
        with open('handw.txt', 'r') as file:
            msg = file.read(1900).strip()
            while len(msg) > 0:
                await message.channel.send('```' + msg + '```')
                msg = file.read(1900).strip()
        return
    
    if msg.startswith('$look'):
        with open('hando.txt', 'r') as file:
            msg = file.read(1900).strip()
            while len(msg) > 0:
                await message.channel.send('```' + msg + '```')
                msg = file.read(1900).strip()
        return

    if msg.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send('```' + quote + '```')
        return

    if db["responding"]:
        options = starter_encouragements
        if "encouragements" in db.keys():
            options = options + db["encouragements"]

        if any(word in msg for word in sad_words):
            await message.channel.send('```' + random.choice(options) + '```')
            return
    
    if msg.startswith('$tell'):
        options = starter_phrases
        if "p1" in db.keys():
            options[0] = options[0] + db["p1"]
        
        if "p2" in db.keys():
            options[1] = options[1] + db["p2"]

        if "p3" in db.keys():
            options[2] = options[2] + db["p3"]

        if "p4" in db.keys():
            options[3] = options[3] + db["p4"]

        if "p5" in db.keys():
            options[4] = options[4] + db["p5"]
        
        s = []

        for i in range(0, 5):
            r= random.randint(0, len(options[i]) - 1)
            s.append(options[i][r])

        result = " ".join(s) + "!"

        await message.channel.send('```' + result + '```')
        return

    if msg.startswith("$newName"):
        phrase = msg.split("$newName ", 1)[1]
        update_p1(phrase)
        await message.channel.send("```New name added.```")
        return

    if msg.startswith("$delName"):
        phrasesA = []
        if "p1" in db.keys():
            index = int(msg.split("$delName ", 1)[1])
            delete_p1(index)
            phrasesA = db["p1"]
        await message.channel.send('```' + str(phrasesA) + '```')
        return

    if msg.startswith("$listName"):
        phrasesA = []
        if "p1" in db.keys():
            phrasesA = db["p1"]
        await message.channel.send('```' + str(phrasesA) + '```')
        return

    if msg.startswith("$newDesc"):
        phrase = msg.split("$newDesc ", 1)[1]
        update_p2(phrase)
        await message.channel.send("```New description added.```")
        return

    if msg.startswith("$delDesc"):
        phrasesA = []
        if "p2" in db.keys():
            index = int(msg.split("$delDesc ", 1)[1])
            delete_p2(index)
            phrasesA = db["p2"]
        await message.channel.send('```' + str(phrasesA) + '```')
        return

    if msg.startswith("$listDesc"):
        phrasesA = []
        if "p2" in db.keys():
            phrasesA = db["p2"]
        await message.channel.send('```' + str(phrasesA) + '```')
        return

    if msg.startswith("$newState1"):
        phrase = msg.split("$newState1 ", 1)[1]
        update_p3(phrase)
        await message.channel.send("```New statement1 added.```")
        return

    if msg.startswith("$delState1"):
        phrasesA = []
        if "p3" in db.keys():
            index = int(msg.split("$delState1 ", 1)[1])
            delete_p3(index)
            phrasesA = db["p3"]
        await message.channel.send('```' + str(phrasesA) + '```')
        return

    if msg.startswith("$listState1"):
        phrasesA = []
        if "p3" in db.keys():
            phrasesA = db["p3"]
        await message.channel.send('```' + str(phrasesA) + '```')
        return

    if msg.startswith("$newState2"):
        phrase = msg.split("$newState2 ", 1)[1]
        update_p4(phrase)
        await message.channel.send("```New statement2 added.```")
        return

    if msg.startswith("$delState2"):
        phrasesA = []
        if "p4" in db.keys():
            index = int(msg.split("$delState2 ", 1)[1])
            delete_p4(index)
            phrasesA = db["p4"]
        await message.channel.send('```' + str(phrasesA) + '```')
        return

    if msg.startswith("$listState2"):
        phrasesA = []
        if "p4" in db.keys():
            phrasesA = db["p4"]
        await message.channel.send('```' + str(phrasesA) + '```')
        return

    if msg.startswith("$newBye"):
        phrase = msg.split("$newBye ", 1)[1]
        update_p5(phrase)
        await message.channel.send("```New bye message added.```")
        return

    if msg.startswith("$delBye"):
        phrasesA = []
        if "p5" in db.keys():
            index = int(msg.split("$delBye ", 1)[1])
            delete_p5(index)
            phrasesA = db["p5"]
        await message.channel.send('```' + str(phrasesA) + '```')
        return

    if msg.startswith("$listBye"):
        phrasesA = []
        if "p5" in db.keys():
            phrasesA = db["p5"]
        await message.channel.send('```' + str(phrasesA) + '```')
        return

    if msg.startswith("$new"):
        encouraging_message = msg.split("$new ", 1)[1]
        update_encouragements(encouraging_message)
        await message.channel.send("```New encouraging message added.```")
        return

    if msg.startswith("$del"):
        encouragements = []
        if "encouragements" in db.keys():
            index = int(msg.split("$del ", 1)[1])
            delete_encouragements(index)
            encouragements = db["encouragements"]
        await message.channel.send('```' + str(encouragements) + '```')
        return

    if msg.startswith("$list"):
        encouragements = []
        if "encouragements" in db.keys():
            encouragements = db["encouragements"]
        await message.channel.send('```' + str(encouragements) + '```')
        return

    if msg.startswith("$responding"):
        value = msg.split("$responding ", 1)[1]

        if value.lower() == "true":
            db["responding"] = True
            await message.channel.send("```Responding is on.```")
        else:
            db["responding"] = False
            await message.channel.send("```Responding is off.```")
        return

keep_alive()
client.run(os.getenv('TOKEN'))