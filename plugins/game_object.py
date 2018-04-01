from disco.bot import Plugin


class WordGameObject:
    def __init__(self, channel_id, channel_name,
                 max_players=4, maximum_sentences=5,
                 can_join_during_game=True):
        #change max_sentences later
        self.max_players = max_players
        self.channel_id = channel_id
        self.channel_name = channel_name
        self.playing = []
        self.story = []
        self.current_sentence = []
        self.current_turn = None
        self.can_join_during_game = can_join_during_game
        self.game_started = False
        self.maximum_sentences = maximum_sentences
        self.turn_queue = []

    def _get_max_players(self):
        return self.max_players

    def _get_channel_id(self):
        return self.channel_id

    def _get_players(self):
        return self.playing

    def _get_story(self):
        return ' '.join(word for word in (self.story))

    def _get_current_sentence(self):
        return ' '.join(word for word in self.current_sentence)

    def _get_current_turn(self):
        return self.current_turn

    def _add_player(self, user):
        self.playing.append(user)
        if self.game_started and self.can_join_during_game:
            self.turn_queue.append(user) 
        #test this: game in session and someone joins partway through

    def _count_players(self):
        return len(self.playing)

    def _set_turn_order(self):
        if self.game_started:
            self.turn_queue = self.playing

    def _change_turn(self):
        if self.game_started:
            self.current_turn = self.turn_queue.pop(0)
            self.turn_queue.append(self.current_turn)

    def _clear_current_sentence(self):
        self.current_sentence = []


    def __str__(self):
        print("Calling str")
        return "WordGameObject on channel {} aka {}".format(self.channel_id, self.channel_name)
