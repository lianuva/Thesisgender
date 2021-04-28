from otree.api import *
import pandas as pd
from openpyxl import load_workbook

doc = """
Math
"""


class Constants(BaseConstants):
    name_in_url = 'math'
    players_per_group = None
    num_rounds = 2
    xl = pd.ExcelFile("Matrices.xlsx")
    df = xl.parse("Sheet1")

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    correct = models.IntegerField(blank=True)
    

def get_current_trial(player: Player):
    return Trial.filter(player=player, choice=None)[0]


def is_finished(player: Player):
    return player.num_completed == player.num_trials


class Trial(ExtraModel):
    player = models.Link(Player)

# FUNCTIONS

# PAGES
class Math(Page):
    form_model = 'player'
    form_fields = ['correct']

    @staticmethod
    def vars_for_template(player):
        r = player.round_number - 1
        n1  = Constants.df["ValueInside11"][r]
        n2  = Constants.df["ValueInside12"][r]
        n3  = Constants.df["ValueInside13"][r]
        n4  = Constants.df["ValueInside21"][r]
        n5  = Constants.df["ValueInside22"][r]
        n6  = Constants.df["ValueInside23"][r]
        n7  = Constants.df["ValueInside31"][r]
        n8  = Constants.df["ValueInside32"][r]
        n9  = Constants.df["ValueInside33"][r]
        n10 = Constants.df["ValueInside41"][r]
        n11 = Constants.df["ValueInside42"][r]
        n12 = Constants.df["ValueInside43"][r]
        return {
            'n1' : n1,
            'n2' : n2,
            'n3' : n3,
            'n4' : n4,
            'n5' : n5,
            'n6' : n6,
            'n7' : n7,
            'n8' : n8,
            'n9' : n9,
            'n10' : n10,
            'n11' : n11,
            'n12' : n12,
        }

   #@staticmethod
    # def js_vars(player: Player):
     # return {
          
     # }

page_sequence = [Math]
