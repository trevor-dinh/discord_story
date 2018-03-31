from disco.bot import Plugin

class WordGameObject:
    def __init__(self, channel_id, channel_name, max_players=4, can_join_during_game=True):
        self.max_players = max_players
        self.channel_id = channel_id
        self.channel_name = channel_name
        self.playing = []
        self.story = []
        self.current_sentence = ""
        self.current_turn = None
        self.can_join_during_game = can_join_during_game

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

    def _add_player(self, user):
        self.playing.append(user)

    def _count_players(self):
        return len(self.playing)


    def __str__(self):
        print("Calling str")
        return "WordGameObject on channel {} aka {}".format(self.channel_id, self.channel_name)
