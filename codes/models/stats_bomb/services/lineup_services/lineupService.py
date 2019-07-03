from codes.db_connection.db_connection import DbConnection


class LineupService:

    def __init__(self):
        self.dbConnection = DbConnection()


    def returnMatchesLineups(self, matches):
        matchesLineups = {}
        for match in matches:
            matchesLineups[match['_id']] = {self.getHomeTeamId(match): self.returnHomeDictLineup(match),
                                            self.getAwayTeamId(match): self.returnAwayDictLineup(match)}
        return matchesLineups

    def returnHomeLineup(self, match):
        homeTeamId = self.getHomeTeamId(match)
        return self.getTeamLineupFromDB(match['_id'], homeTeamId)

    def returnAwayLineup(self, match):
        awayTeamId = self.getAwayTeamId(match)
        return self.getTeamLineupFromDB(match['_id'], awayTeamId)

    def returnAwayDictLineup(self, match):
        awayTeamId = self.getAwayTeamId(match)
        awayLineup = self.getTeamLineupFromDB(match['_id'], awayTeamId)
        return self.makePlayersDictFromLineup(awayLineup)

    def returnHomeDictLineup(self, match):
        homeTeamId = self.getHomeTeamId(match)
        homeLineup = self.getTeamLineupFromDB(match['_id'], homeTeamId)
        return self.makePlayersDictFromLineup(homeLineup)

    def makePlayersDictFromLineup(self, lineup):
        lineupMade = {player['player_id']: {'player_name': player['player_name'],
                                       'jersey_number': player['jersey_number']}

                for player in lineup}
        return lineupMade

    def getTeamLineupFromDB(self, matchId, teamId):
        return self.dbConnection.returnLineupsCollection().find_one({'match_id': matchId, 'team_id': teamId})['lineup']

    def getHomeTeamId(self, match):
        return match['home_team']['home_team_id']

    def getAwayTeamId(self, match):
        return match['away_team']['away_team_id']