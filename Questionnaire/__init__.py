from otree.api import *

doc = """
Questionnaire
"""


class Constants(BaseConstants):
    name_in_url = 'questionnaire'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    mathslider = models.FloatField(blank=True) 
    verbalslider = models.FloatField(blank=True)  
    confirm = models.IntegerField(
        choices=[
        [1, 'I confirm my answer'],
        ],
        widget=widgets.RadioSelect,
        label="Check this button and click next to confirm your answer.",
    )  
    confirm1 = models.IntegerField(
        choices=[
        [1, 'I confirm my answer'],
        ],
        widget=widgets.RadioSelect,
        label="Check this button and click next to confirm your answer.",
    )  

def get_current_trial(player: Player):
    return Trial.filter(player=player, choice=None)[0]


def is_finished(player: Player):
    return player.num_completed == player.num_trials


class Trial(ExtraModel):
    player = models.Link(Player)

# PAGES
class Instructions(Page):
    pass
    
class Questionnairemath(Page):
    form_model = 'player'
    form_fields = ['mathslider', 'confirm']

class Questionnaireverbal(Page):
    form_model = 'player'
    form_fields = ['verbalslider', 'confirm1']    

page_sequence = [Instructions, Questionnairemath, Questionnaireverbal]
