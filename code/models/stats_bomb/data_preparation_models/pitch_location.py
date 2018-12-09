class PitchLocation:
    X = 0
    Y = 1
    X_SIZE = 120
    Y_SIZE = 80
    MIDDLE_CORDINATES = [X_SIZE/2, Y_SIZE/2]

    def moveLocationFromLeftToRightPitchSide(self, location):
        return self.moveLocationFromLeftToRight(location)

    def moveLocationFromLeftToRight(self, location):
        if self.isOnTheLeftPitchSide(location):
            location = self.changeCordinates(location)
        return location

    def isOnTheLeftPitchSide(self, location):
        return location[PitchLocation.X] < PitchLocation.MIDDLE_CORDINATES[PitchLocation.X]

    def changeCordinates(self, location):
        location[PitchLocation.X] = PitchLocation.X_SIZE - location[PitchLocation.X]
        location[PitchLocation.Y] = PitchLocation.Y_SIZE - location[PitchLocation.Y]
        return location