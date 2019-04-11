# Each shot includes an object called freeze_frame which is an array containing information  about relevant players at the time of the shot
class FreezeFrame:
    def __init__(self, location, player, position, teammate):
        # Array containing two integer values. These  are the x and y coordinates on the pitch of  the player at the time of the shot.
        self.location = location
        # Referenced player
        self.player = player
        # Position played by the player referenced
        self.position = position
        # Is this player on the same team as the shooter
        self.teammate = teammate