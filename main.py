from code.data_parsers.stats_bomb.json_utils import SBJsonUtils
from code.models.stats_bomb.data_preparation_models import pitch_events_field_names as pefn
from code.models.stats_bomb.services.sequence_services.sequence_in_attack_service import SequenceInAttack

if __name__ == "__main__":
    sbJsonUtils = SBJsonUtils()
    sequenceInAttack = SequenceInAttack()
    events = sbJsonUtils.readSBDataInTypeFromJsons('event')

    for event in events:
        if sequenceInAttack.isAttackSequenceStartAt(event):
            print('[POCZ]{} - {} -> {}'.format(event[pefn.TIMESTAMP], event[pefn.TEAM][pefn.NAME],
                                               event[pefn.TYPE][pefn.NAME]))

        elif sequenceInAttack.isAttackSequenceEndAt(event):
            print('[KON]{} - {} -> {}'.format(event[pefn.TIMESTAMP], event[pefn.TEAM][pefn.NAME],
                                              event[pefn.TYPE][pefn.NAME]))
        else:
            print('{} - {} -> {}'.format(event[pefn.TIMESTAMP], event[pefn.TEAM][pefn.NAME],
                                         event[pefn.TYPE][pefn.NAME]))

