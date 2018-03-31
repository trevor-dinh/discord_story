from disco.bot import Plugin

from .game_object import WordGameObject

class TutorialPlugin(Plugin):

    def load(self, ctx):
        self.games = {}

    @Plugin.command('testgame')
    def command_test_game(self, event):
        channel_id = event.msg.channel_id
        self.games.update({channel_id: WordGameObject(
            channel_id, event.msg.channel.name)})
        print(self.games)
        self.games[channel_id].playing.append(event.msg.author)
        print(self.games[channel_id].playing)
        event.msg.reply("Game created with {}".format(self.games[channel_id]))

    @Plugin.command('inc')
    def command_increment(self, event):
        channel_called = event.msg.channel_id
        self.players_playing[channel_called].add(str(event.msg.author))
        event.msg.reply("Current players: {}".format(
            self.players_playing[channel_called]))

    @Plugin.command('ping')
    def command_ping(self, event):
        event.msg.reply('Pong!')

    @Plugin.command('pong')
    def command_pong(self, event):
        event.msg.reply("IM SUPPOSED TO SAY PONG, ASSHOLE")

    @Plugin.command('echo', '<content:str...>')
    def on_echo_command(self, event, content):
        #print(content)
        #print(event)
        if content[0] == '!':
            event.msg.reply(content[1:])
            event.msg.reply("Nice try, but please don't make the bot do commands with echo. They have feelings too.")
            return
        event.msg.reply(content)

    @Plugin.command('add', '<a:int> <b:int>', group='math')
    def on_add_command(self, event, a, b):
        event.msg.reply('{}'.format(a + b))

    @Plugin.command('noticeme')
    def command_hello(self, event):
        event.msg.reply("Hi " + event.msg.author.mention)

    @Plugin.command('hi')
    def command_hi(self,event):
        event.msg.reply("Hi {}".format(event.msg.author))

    @Plugin.command('whatchannel')
    def command_get_channel(self, event):
        event.msg.reply("You are in " + 
            str(event.msg.channel.id) + 
            " aka " + event.msg.channel.name)
