# Tell me a story, Discord.
Discord bot developed for LAHacks.

A config.json file is needed to run the bot, but I did not provide it because it had a secret key.

# What does the bot do?
The bot provides the implementation of a game where participating users on a server input one word each in a given text server. The goal of the game is to construct a story from user messages. After a certain number of sentences,  the game ends and everyone gets to read the story they've created. 

A (rudimentary) example of the game:

User1: The

User2: quick

User3: fox

User4: jumped

User5: over

User6: the

User7: lazy

User1: dog.

All commands are listed using the !help command. 

With the way the bot is currently set up, there is a hardcoded limit on the number of sentences available. Moreover, to end a sentence, users must have a period after the final word of the sentence. 

# Additional details
Disco.py framework for Discord API was used to develop the bot, and the bot is usually hosted on an Amazon AWS-EC2 virtual machine. As mentioned before, if one were to run the bot on their own server, they would need a config.json file(which includes details on the secret key along with other details on bot implementation). More information can be found on Disco.py's documentation site.

# Final thoughts
I would like to consider revamping the structures used to store data regarding games across servers, along with additional rules that users can set for each personal game. Such rules involve a required/forbidden letter, a required word length, a required first/last letter, or even have the first user start the story off with an unlimited amount of words. 

I also considered the implementation of parsing words from a dictionary database so users can input a random noun/verb/adjective of their choice, but considering the time limit we had at the hackathon, we were unable to do so. However, there's a good chance I will revisit this project in the near future to fix things and add more features.
