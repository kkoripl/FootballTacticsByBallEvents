from code.models.stats_bomb.data_preparation_models.pitch_events import PitchEvents as pe

class Event:
    @classmethod
    def from_dict(cls, dict):
        obj = cls()
        obj.__dict__.update(dict)
        return obj

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self)

    def gotPlayer(self):
        return self.player is not None

    def isAttackingEvent(self):
        return self.possession_team.id == self.team.id  \
               and self.type.id in pe.OFFENSIVE_EVENTS \
               and self.play_pattern.id not in [2, 3]

    def isDefendingEvent(self, event):
        return self.possession_team.id != self.team.id \
               and self.type.id in pe.DEFENSIVE_EVENTS \
               and event.play_pattern.id not in [2, 3]


    # The unique identifier for each event UUID
    id = None
    # Sequence notation for the ordering of  events. INTEGER
    index = None
    # The part of the match the timestamp relates to (1 = first half, 2 = second half)
    period = None
    # The point in the match the event takes  place.
    timestamp = None
    # The minute part of the timestamp
    minute = None
    # The second part of the timestamp
    second = None
    # Type of the event
    type = None
    # Each possession is given a unique integer  within the scope of the match. Events in  the same possession have this same  identifier.
    possession = None
    # Team with the ball at the time
    possession_team = None
    # Type of play taken apart
    play_pattern = None
    # The team this event relates to
    team = None
    # Player this event relates to
    player = None
    # Position the player was in at  the time of this event
    position = None
    # Array containing two integer values. These  are the x and y coordinates of the event.  This only displays if the event has pitch  coordinates.
    location = None
    # If relevant, the length in seconds the event  lasted. 
    duration = None
    # If an event was done whilst pressure was  being applied, this flag will arise. 
    under_pressure = None
    # A comma separated list of the Ids of related events. For example, a shot might  be related to the Goalkeeper event, and a  Block Event. The corresponding events will  have the Id of the shot in their  related_events column.
    related_events = None
    # For some event types, additional details are added with additional details specific  to that event type. e.g. for shot events a  shot object is added, containing details  about the shot (shot_type, body_part used  etc.
    event_type_name = None
    # Event made by the player in details
    action = None
    # For events with a set of match_posititions  relevant (starting XI, tactical shift), the  “tactics” object is added. The formation  item describes the formation being used
    tactics = None
    # Each shot includes an object called freeze_frame which is an array containing information  about relevant players at the time of the shot
    freeze_frame = None
