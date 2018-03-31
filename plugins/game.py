from disco.bot import Plugin



class WordStoryGame(Plugin):
    

    @Plugin.command('newgame')
    def create_new_game(self, event):
        

        event.msg.reply(
            "You wanted a new game, but the stupid developers haven't implemented it yet :(")
        
