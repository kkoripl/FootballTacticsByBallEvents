class PitchEvents:
    def __init__(self):
        self.pitchEvents= {
            'withPitchPosition': {
                2: 'Ball recovery',
                3: 'Dispossessed',
                4: 'Duel',
                6: 'Block',
                8: 'Offside',
                9: 'Clearance',
                10: 'Interception',
                14: 'Dribble',
                16: 'Shot',
                17: 'Pressure',
                20: 'Own goal against',
                21: 'Faul won',
                22: 'Faul committed',
                23: 'Goal keeper action',
                25: 'Own goal for',
                28: 'Shield - defender shields ball going out of bounds',
                30: 'Pass on the ground',
                31: 'Low pass - under shoulder level',
                32: 'High pass - over shoulder level',
                33: '50/50 - recover a loose ball',
                37: 'Error - on-the-ball mistake leading for shot on goal',
                38: 'Miscontrol',
                39: 'Dribble past',
                41: 'Referee ball-drop',
                42: 'Ball receipt'
            },
            'withoutPitchPosition': {
                5: 'Camera on',
                18: 'Half start',
                19: 'Substitution',
                24: 'Bad behaviour',
                26: 'Substitution - player on',
                27: 'Substitution - player off',
                29: 'Camera off - video broadcast leaves gameplay',
                34: 'Half end',
                35: 'Starting XI',
                36: 'Tactical shift',
                40: 'Injury stoppage'
            }
        }