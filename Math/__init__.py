from otree.api import *
import pandas as pd
from openpyxl import load_workbook
import json
import csv

doc = """
Math
"""

class Constants(BaseConstants):
    name_in_url = 'math'
    players_per_group = None
    num_rounds = 2
    
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
    correcttables = models.IntegerField(blank=True)
    # correcttables2 = models.IntegerField(blank=True)

# FUNCTIONS

# PAGES
class Math(Page):
    form_model = 'player'
    form_fields = ['correcttables']
    timer_text = 'Time left to complete the task:'
    timeout_seconds = 20

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

    # when refresh, dont start over
    # @staticmethod
    # def live_method(player, data):
    #     print('received a bid from', player.id_in_group, ':', data)

class Mathwaitpageround1(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

class Mathwaitpageround2(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == 2


page_sequence = [Mathwaitpageround1, Mathwaitpageround2, Math]
