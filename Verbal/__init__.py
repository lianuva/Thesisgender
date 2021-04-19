from otree.api import *

doc = """
Verbal
"""


class Constants(BaseConstants):
    name_in_url = 'Verbal'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
  pass


class Player(BasePlayer):
    word = models.StringField(label="Enter the words you find in the word below")
    
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
class Verbal(Page):
    form_model = 'player'
    form_fields = ['word']

page_sequence = [Verbal]
