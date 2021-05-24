from otree.api import *
import random
import json

doc = """
Instructions
"""


class Constants(BaseConstants):
    name_in_url = 'instructions'
    players_per_group = None
    tasks = ['1', '2']
    num_rounds = len(tasks)

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
        label="By clicking the button below, you acknowledge that your participation in the study is voluntary, you are over 18 years of age, and that you are aware that you may choose to terminate your participation in the study at any time and for any reason.",
    )  
    # random = models.StringField(blank=True)

    

def get_current_trial(player: Player):
    return Trial.filter(player=player, choice=None)[0]


def is_finished(player: Player):
    return player.num_completed == player.num_trials


class Trial(ExtraModel):
    player = models.Link(Player)

# FUNCTIONS
# randomize next app
def creating_session(subsession: Subsession):
    if subsession.round_number == 1:
        for p in subsession.get_players():
            round_numbers = list(range(1, Constants.num_rounds + 1))
            random.shuffle(round_numbers)
            p.participant.vars['task_rounds'] = dict(zip(Constants.tasks, round_numbers))

# PAGES
class Welcome(Page):
    form_model = 'player'
    form_fields = ['consent']

    @staticmethod
    def app_after_this_page(player, upcoming_apps):
        print('upcoming_apps is', upcoming_apps)
        if player.round_number == player.participant.vars['task_rounds']['1']:
            return "Math"
        else :
            return "Verbal"

    @staticmethod
    def before_next_page(player, timeout_happened):
        if player.round_number == player.participant.vars['task_rounds']['1']:
            player.participant.apprandom = 1
            player.participant.apptext = ""
        else :
            player.participant.apprandom = 2
            player.participant.apptext = "This experiment exists of two tasks, which you will have to perform twice, followed by a questionnaire. "

page_sequence = [Welcome]
