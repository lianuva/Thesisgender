from otree.api import *
import pandas as pd
import json
import csv

doc = """
Math
"""

class Constants(BaseConstants):
    name_in_url = 'math'
    players_per_group = None
    num_rounds = 2
    num_trials = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]
    df = pd.read_csv("_static/Math/Matrices.csv")
   
x = {
    "n1"  : Constants.df["ValueInside11"].values.tolist(),
    "n2"  : Constants.df["ValueInside12"].values.tolist(),
    "n3"  : Constants.df["ValueInside13"].values.tolist(),
    "n4"  : Constants.df["ValueInside21"].values.tolist(),
    "n5"  : Constants.df["ValueInside22"].values.tolist(),
    "n6"  : Constants.df["ValueInside23"].values.tolist(),
    "n7"  : Constants.df["ValueInside31"].values.tolist(),
    "n8"  : Constants.df["ValueInside32"].values.tolist(),
    "n9"  : Constants.df["ValueInside33"].values.tolist(),
    "n10"  : Constants.df["ValueInside41"].values.tolist(),
    "n11"  : Constants.df["ValueInside42"].values.tolist(),
    "n12"  : Constants.df["ValueInside43"].values.tolist(),
}

sorted_string = json.dumps(x)

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    correcttablespractice   = models.IntegerField(blank=True)
    correcttables           = models.IntegerField(blank=True)

# class Trial(ExtraModel):
#     player                  = models.Link(Player)

# def is_finished(player: Player):
#     return player.num_completed == Constants.num_trials

# def get_current_trial(player: Player):
#     return Trial.filter(player=player, is_correct=None)[0]

# PAGES
class Mathpractice(Page):
    form_model = 'player'
    form_fields = ['correcttablespractice']

    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

class Math(Page):
    form_model = 'player'
    form_fields = ['correcttables']

    # live_method = live_method
    timer_text = 'Time left to complete the task:'
    timeout_seconds =120

    # def live_method(player: Player, matrixround):
    #     if matrixround:
    #         player.correcttables = matrixround 
    #         print(matrixround)
            # print(data)

        # if data:
        #     # if is_finished(player):
        #     #     return
        #     trial = get_current_trial(player)
        #     trial.matrixround = data['matrixround']

        #     if trial.matrixround:
        #         player.correcttables = trial.matrixround
            
    @staticmethod
    def js_vars(player: Player):
     return {
        'sorted_string' : sorted_string,
        'round_number'  : player.round_number,
    }

    # save vars for results page
    @staticmethod
    def before_next_page(player, timeout_happened):
        if player.round_number == 1:
            player.participant.correcttables = player.correcttables
        else :
            player.participant.correcttables2 = player.correcttables    

class Mathwaitpageround1(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

class Mathwaitpageround2(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == 2

page_sequence = [Mathpractice, Mathwaitpageround1, Mathwaitpageround2, Math]
