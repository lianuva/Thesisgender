from otree.api import *

doc = """
Verbal
"""


class Constants(BaseConstants):
    name_in_url = 'verbal'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
  pass


class Player(BasePlayer):
    word = models.StringField(label="Enter the words you find below", blank=True)
    
def get_current_trial(player: Player):
    return Trial.filter(player=player, choice=None)[0]


def is_finished(player: Player):
    return player.num_completed == player.num_trials


class Trial(ExtraModel):
    player = models.Link(Player)

# PAGES
class Verbal(Page):
    form_model = 'player'
    form_fields = ['word']
    timer_text = 'Time left to complete the task:'
    timeout_seconds = 120

page_sequence = [Verbal]
