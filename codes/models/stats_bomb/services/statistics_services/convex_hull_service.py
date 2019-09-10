from scipy.spatial import ConvexHull


class ConvexHullService:
    def create_convex_hulls(self, match):
        self.create_players_convex_hulls(match.home)
        self.create_players_convex_hulls(match.away)

    def create_players_convex_hulls(self, team):
        for player in team.lineup:
            player.convex_hulls['attack'] = self.create_convex_hull(self.get_attack_locations(player.events))
            player.convex_hulls['defence'] = self.create_convex_hull(self.get_defence_locations(player.events))

    def get_attack_locations(self, events):
        return [event.location for event in events['attack']]

    def get_defence_locations(self, events):
        return [event.location for event in events['defence']]

    def create_convex_hull(self, events_locations):
        if len(events_locations) < 3:
            return None
        else:
            return ConvexHull([location for location in events_locations])
