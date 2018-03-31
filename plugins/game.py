from disco.bot import Plugin
from .game_object import WordGameObject


class WordStoryGame(Plugin):

    def load(self, ctx):
        self.games = {}

    @Plugin.command('newgame')
    def create_new_game(self, event):
        channel_id = event.msg.channel_id
        self.games.update({
            event.msg.channel_id: WordGameObject(
                channel_id, event.msg.channel.name)})
        event.msg.reply("Created a new game in this channel")
        #self.games[channel_id].playing.append(event.msg.author)
        self.games[channel_id]._add_player(event.msg.author)
        event.msg.reply("Currently playing: {}".format(event.msg.author))

    @Plugin.command('joingame')
    def command_join_game(self, event):
        if event.msg.channel_id not in self.games:
            event.msg.reply(
                "No game in this channel created yet! Try using !newgame")
        else:
            this_game = self.games[event.msg.channel_id]
            maximum = this_game._get_max_players()
            if this_game._count_players() == maximum:
                event.msg.reply("Sorry! The lobby is full")
            else:
                if event.msg.author not in this_game._get_players():
                    self.games[event.msg.channel_id]._add_player(
                        event.msg.author)
                    event.msg.reply("{} has joined the game".format(
                        event.msg.author.mention))
                    event.msg.reply("Currently playing: {} ".format(
                        ', '.join(
                            p.mention for p in self.games[event.msg.channel_id]
                            ._get_players())))
                    if (this_game._count_players() == maximum):
                        event.msg.reply(
                            "Maximum players reached." +
                            "Type !startgame to start.")
                else:
                    event.msg.reply(
                        "{}, you already signed up for this game!".format(
                            event.msg.author.mention))

    @Plugin.command('startgame')
    def command_start_game(self, event):
        if event.msg.channel_id not in self.games:
            event.msg.reply(
                "A game for this channel has not been created yet." +
                "Try using !newgame")
        else:
            this_game = self.games[event.msg.channel_id]
            if this_game._count_players() < 2:
                event.msg.reply("Not enough players!")
            event.msg.reply(
                "Developers haven't figured it out yet sorry")

    @Plugin.command('listplayers')
    def command_list_players(self, event):
        if event.msg.channel_id in self.games:
            event.msg.reply("Playing: {}".format(', '.join(
                p.mention for p in
                self.games[event.msg.channel_id]._get_players())))
        else:
            event.msg.reply("No game created for this channel!")




