from otree.api import *
import random
import json

doc = """
Instructions
"""


class Constants(BaseConstants):
    name_in_url = 'instructions'
    players_per_group = None
    # tasks = ['1', '2']
    # num_rounds = len(tasks)
    num_rounds =1

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

# FUNCTIONS
# randomize next app
# def creating_session(subsession: Subsession):
#     if subsession.round_number == 1:
#         for p in subsession.get_players():
#             round_numbers = list(range(1, Constants.num_rounds + 1))
#             random.shuffle(round_numbers)
#             p.participant.vars['task_rounds'] = dict(zip(Constants.tasks, round_numbers))

# PAGES
class Welcome(Page):
    form_model = 'player'
    form_fields = ['consent']

    # @staticmethod
    # def app_after_this_page(player, upcoming_apps):
    #     print('upcoming_apps is', upcoming_apps)
    #     if player.round_number == player.participant.vars['task_rounds']['1']:
    #         # return upcoming_apps[0]
    #         return "Mathpractice"
    #     else :
    # #         return "Verbal"

    # @staticmethod
    # def before_next_page(player, timeout_happened):
    #     if player.round_number == player.participant.vars['task_rounds']['1']:
    #         player.participant.text = "In the first task"
    #     else :
    #         player.participant.text = "In the second task"


page_sequence = [Welcome]
