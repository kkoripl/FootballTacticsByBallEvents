class PlayPattern:

    def __init__(self):
        self.play_pattern = {
            1: 'Regular Play',
            2: 'From Corner',
            3: 'From free Kick',
            4: 'From Throw In',
            5: 'Other',
            6: 'From Counter',
            7: 'From Goal Kick',
            8: 'From Keeper',
            9: 'From Kick Off'
        }

    def get_play_pattern_name(self, play_pattern_id):
        return self.play_pattern[play_pattern_id]