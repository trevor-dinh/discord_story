from disco.bot import Plugin
from .game_object import WordGameObject


class WordStoryGame(Plugin):

    def load(self, ctx):
        self.games = {}

    @Plugin.command('newgame')
    def create_new_game(self, event):
        channel_id = event.msg.channel_id
        if channel_id in self.games:
            event.msg.reply(
                "A game in this channel already exists!" +
                "Use !cleargame to reset and try again")
            return
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
                return
            this_game.game_started = True
            this_game._set_turn_order()
            this_game._change_turn()
            event.msg.reply("Game has started. It is now {}'s turn".format(
                this_game.current_turn.mention))

    @Plugin.command('listplayers')
    def command_list_players(self, event):
        #if event.msg.channel_id in self.games:
        if self.verify_game_exists(event.msg.channel_id):
            event.msg.reply("Playing: {}".format(', '.join(
                p.mention for p in
                self.games[event.msg.channel_id]._get_players())))
        else:
            event.msg.reply("No game created for this channel!")

    @Plugin.command('word', '<content:str>')
    def command_enter_word(self, event, content):
        if event.msg.channel_id not in self.games:
            event.msg.reply("No game made for this channel!")
            return
        this_game = self.games[event.msg.channel_id]

        if not this_game.game_started:
            event.msg.reply("The game hasn't started yet!")

        if this_game.current_turn != event.msg.author:
            event.msg.reply("It's not your turn, {}".format(
                event.msg.author.mention))
        else:
            this_game.current_sentence.append(content)
            print("MSG CONTENT TYPE IS {}".format(type(content)))
            if content[-1] == '.':
                this_game.story.append(
                    ' '.join(word for word in this_game.current_sentence))
                print(this_game.story)
                this_game._clear_current_sentence()
                #handle when story has 64 sentences

            this_game._change_turn()
            event.msg.reply("It's now your turn, {}".format(
                this_game._get_current_turn().mention))

    @Plugin.command('playerorder')
    def command_get_turn_order(self, event):
        if self.verify_game_exists_and_running(event.msg.channel_id):
            event.msg.reply("The current order is {}".format(
                self.games[event.msg.channel_id].turn_queue))

    def verify_game_exists(self, channel_id):
        return channel_id in self.games

    def verify_game_exists_and_running(self, channel_id):
        return self.verify_game_exists(
            channel_id) and self.games[channel_id].game_started

    @Plugin.command('getstory')
    def command_get_story(self, event):
        if self.verify_game_exists_and_running(event.msg.channel_id):
            print(self.games[event.msg.channel_id]._get_story())
            if len(self.games[event.msg.channel_id._get_story]) > 0:
                event.msg.reply("```{}```".format(
                    self.games[event.msg.channel_id]._get_story()))
            else:
                event.msg.reply("The story has not been created yet!" +
                                " Create a sentence to start it off.")
        else:
            event.msg.reply("Game not created or started yet!")

    @Plugin.command('currentsentence')
    def command_get_current_sentence(self, event):
        if self.verify_game_exists_and_running(event.msg.channel_id):
            if len(
                self.games[event.msg.channel_id]
                    ._get_current_sentence()) > 0:
                event.msg.reply(
                    self.games[event.msg.channel_id]._get_current_sentence())
            else:
                event.msg.reply("The current sentence is empty!")
        else:
            event.msg.reply("Game not created or started yet!")

    @Plugin.command('whoseturn')
    def command_get_current_turn(self, event):
        if self.verify_game_exists_and_running(event.msg.channel_id):
            event.msg.reply(
                "It is {}'s turn".format(
                    self.games[event.msg.channel_id]._get_current_turn))
        else:
            event.msg.reply("Game not created or started yet!")


