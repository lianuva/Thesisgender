from otree.api import *
import random

doc = """
Instructions
"""


class Constants(BaseConstants):
    name_in_url = 'instructions'
    players_per_group = None
    num_rounds = 1
    # next = ['1','2']

# random.shuffle(next)

class Subsession(BaseSubsession):
    pass


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

    # @staticmethod
    # def app_after_this_page(player, upcoming_apps):
    #     if player.next ==1:
    #         return upcoming_apps[0]
    #     else :
    #         return 


page_sequence = [Welcome]
