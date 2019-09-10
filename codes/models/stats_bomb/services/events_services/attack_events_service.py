from codes.models.stats_bomb.services.events_services.particular_events.event_service import Event


class AttackEventsService:
    def get_attack_events(self, events):
        attackEvents = []
        for event in events:
            if Event.is_attacking_event(event):
                attackEvents.append(event)
        return attackEvents

    # def isAttackingEvent(self, event):
    #     return Event.getEventTypeId(event) in [pe.SHOT, pe.PASS, pe.DRIBBLE, pe.BALL_RECOVERY, pe.BALL_RECEIPT, pe.FIFTY_FIFTY, pe.FAUL_WON, pe.FAUL_COMMITTED, pe.MISCONTROL]