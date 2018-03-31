from disco.bot import Plugin

class WordGameObject:
    def __init__(self, channel_id, channel_name, max_players=4):
        self.max_players = max_players
        self.channel_id = channel_id
        self.channel_name = channel_name
        self.playing = []
        self.story = []
        self.current_sentence = ""
        self.current_turn = None

    def _get_max_players(self):
        return self.max_players

    def _get_channel_id(self):
        return self.channel_id

    def _get_players(self):
        return self.playing

    def _get_story(self):
        return self.story

    def _get_current_sentence(self):
        return self.current_sentence

    def _get_current_turn(self):
        return self.current_turn

    def __str__(self):
        print("Calling str")
        return "WordGameObject on channel {} aka {}".format(self.channel_id, self.channel_name)
