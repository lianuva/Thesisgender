from otree.api import *
import random

doc = """
Questionnaire
"""


class Constants(BaseConstants):
    name_in_url = 'questionnaire'
    players_per_group = None
    tasks = ['1','2']
    num_rounds = len(tasks)

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

# FUNCTIONS
def creating_session(subsession: Subsession):
    if subsession.round_number == 1:
        for p in subsession.get_players():
            round_numbers = list(range(1, Constants.num_rounds + 1))
            random.shuffle(round_numbers)
            p.participant.vars['task_rounds'] = dict(zip(Constants.tasks, round_numbers))


# PAGES
class Instructions(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1
    
class Questionnairemath(Page):
    form_model = 'player'
    form_fields = ['mathslider', 'confirm']

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.vars['task_rounds']['1']

class Questionnaireverbal(Page):
    form_model = 'player'
    form_fields = ['verbalslider', 'confirm1']    

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.vars['task_rounds']['2']

page_sequence = [Instructions, Questionnairemath, Questionnaireverbal]
