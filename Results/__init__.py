from otree.api import *

doc = """
Results
"""


class Constants(BaseConstants):
    name_in_url = 'Results'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
  pass


class Player(BasePlayer):
    pass
    
def get_current_trial(player: Player):
    return Trial.filter(player=player, choice=None)[0]


def is_finished(player: Player):
    return player.num_completed == player.num_trials


class Trial(ExtraModel):
    player = models.Link(Player)

def to_dict(trial: Trial):
    return dict(
        question=trial.question,
        optionA=trial.optionA,
        optionB=trial.optionB,
        id=trial.id,
    )

# PAGES
class Results(Page):
    
    @staticmethod
    def vars_for_template(player: Player):
        return dict(trials=Trial.filter(player=player))
    pass


page_sequence = [Results]
