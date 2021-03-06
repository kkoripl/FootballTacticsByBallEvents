class PitchEvents:
    BALL_RECOVERY = 2
    DISPOSSESSED = 3
    DUEL = 4
    CAMERA_ON = 5
    BLOCK = 6
    OFFSIDE = 8
    CLEARANCE = 9
    INTERCEPTION = 10
    DRIBBLE = 14
    SHOT = 16
    PRESSURE = 17
    HALF_START = 18
    SUBSTITUTION = 19
    OWN_GOAL_AGAINST = 20
    FAUL_WON = 21
    FAUL_COMMITTED = 22
    GOAL_KEEPER_ACTION = 23
    BAD_BEHAVIOUR = 24
    OWN_GOAL_FOR = 25
    SUBSTITUTION_ON = 26
    SUBSTITUTION_OFF = 27
    SHIELD = 28
    CAMERA_OFF = 29
    PASS = 30
    LOW_PASS = 31
    HIGH_PASS = 32
    FIFTY_FIFTY = 33
    HALF_END = 34
    STARTING_XI = 35
    TACTICAL_SHIFT = 36
    ERROR = 37
    MISCONTROL = 38
    DRIBBLE_PAST = 39
    INJURY_STOPPAGE = 40
    REFEREE_BALL_DROP = 41
    BALL_RECEIPT = 42
    CORNER = 61
    FREE_KICK = 62
    GOAL_KICK = 63
    KICK_OFF = 65
    RECOVERY = 66
    THROW_IN = 67
    PENALTY = 88

    OFFENSIVE_EVENTS = [SHOT, DRIBBLE, DRIBBLE_PAST, BALL_RECEIPT, RECOVERY, PASS, LOW_PASS, HIGH_PASS, SHIELD, BALL_RECOVERY, FIFTY_FIFTY]
    DEFENSIVE_EVENTS = [DUEL, BLOCK, CLEARANCE, INTERCEPTION, GOAL_KEEPER_ACTION]
