class PitchLocation:
    X = 0
    Y = 1
    Z = 3
    A = 4
    LEFT_SIDE = 0
    RIGHT_SIDE = 1
    X_SIZE = 120
    Y_SIZE = 80
    MIDDLE_CORDINATES = [X_SIZE/2, Y_SIZE/2]
    CORNERS = [[0, 0], [X_SIZE, 0], [0, Y_SIZE], [X_SIZE, Y_SIZE]]
    BINS_X = 10 #10
    BINS_Y = 8 #16

    def createPitchBins(self, bins_x, bins_y):
        vertical_bins_ranges = []
        horizontal_bins_ranges = []

        width = PitchLocation.X_SIZE / bins_x
        height = PitchLocation.Y_SIZE / bins_y
        for low in range(0, PitchLocation.X_SIZE, int(width)):
            if low + width == PitchLocation.X_SIZE: horizontal_bins_ranges.append((low, low + width + 1))
            else: horizontal_bins_ranges.append((low, low + width))

        for low in range(0, PitchLocation.Y_SIZE, int(height)):
            if low + height == PitchLocation.Y_SIZE: vertical_bins_ranges.append((low, low + height + 1))
            else: vertical_bins_ranges.append((low, low + height))

        return vertical_bins_ranges, horizontal_bins_ranges

    # bins like: [ 0 1 2 3 ]
    #            [ 4 5 6 7 ]
    def findPitchBin(self, location, vertical_bins_ranges, horizontal_bins_ranges):
        self.standarizeToFarCordinates(location)
        vertical_bin = None
        horizontal_bin = None

        for i in range(0, len(horizontal_bins_ranges)):
            if horizontal_bins_ranges[i][0] <= location[PitchLocation.X] < horizontal_bins_ranges[i][1]:
                horizontal_bin = i

        for i in range(0, len(vertical_bins_ranges)):
            if vertical_bins_ranges[i][0] <= location[PitchLocation.Y] < vertical_bins_ranges[i][1]:
                vertical_bin = i

        return (horizontal_bin + (len(horizontal_bins_ranges)-1)*vertical_bin) + vertical_bin

    def standarizeToFarCordinates(self, location):
        if location[0] > PitchLocation.X_SIZE:
            location[0] = PitchLocation.X_SIZE

        if location[1] > PitchLocation.Y_SIZE:
            location[1] = PitchLocation.Y_SIZE