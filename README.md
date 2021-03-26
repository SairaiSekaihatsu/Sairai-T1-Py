# Sairai-T1-Py

Simple bot created for learning and testing purpose on https://replit.com/@Sairai/Sairai-T1-Py

Based on the following tutorial: https://www.freecodecamp.org/news/create-a-discord-bot-with-python/

To use it, just invite to your Discord server with the following link:

https://discord.com/api/oauth2/authorize?client_id=824384631893393448&permissions=24640&scope=bot

Bot name: **Sairai-T1-Bot#2924**

## Commands
* $hello - Says hello <user>
* $inspire - Presents inspirational message from https://zenquotes.io/api/random
* $responding <bool: true | bool: false> - enables/disables encouragements, defaults to false if anything other then true is the argument
* $new <string: encouragement> - Adds new encouragements to the userdefined list
* $del <int: index>
* $list - Shows the list of userdefined encouragements
* $handi - Shows a middle finger
* $handw - Live long and in peace
* $hando - Look for yourself

## Addiontal features
### Encouragements
Bot will listen on following list of words: "sad", "depressed", "unhappy", "angry", "miserable"

And reply with a user maintained set of encouragements.

Predefined encouragements: "Cheer up!", "Hang in there.", "You are a great person / bot!"

More can be added by anyone with "$new <encouragement>" They can also be removed by anyone with "$del <index>"
  
