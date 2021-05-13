from otree.api import *

doc = """
Instructions
"""


class Constants(BaseConstants):
    name_in_url = 'instructions'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


#def creating_session(subsession: Subsession):
    #for p in subsession.get_players():
        #stimuli = read_csv()
        #p.num_trials = len(stimuli)
        #for stim in stimuli:
        #   Trial.create(player=p, **stim)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    consent = models.IntegerField(
        choices=[
        [1, 'I would like to participate'],
        ],
        widget=widgets.RadioSelect,
        label="",
    )  
    

def get_current_trial(player: Player):
    return Trial.filter(player=player, choice=None)[0]


def is_finished(player: Player):
    return player.num_completed == player.num_trials


class Trial(ExtraModel):
    player = models.Link(Player)


# PAGES
class Welcome(Page):
    form_model = 'player'
    form_fields = ['consent']

page_sequence = [Welcome]
