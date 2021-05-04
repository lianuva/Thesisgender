from otree.api import *
import pandas as pd
from openpyxl import load_workbook
import json

doc = """
Math
"""

class Constants(BaseConstants):
    name_in_url = 'math'
    players_per_group = None
    num_rounds = 1
    xl = pd.ExcelFile("Matrices.xlsx")
    df = xl.parse("Sheet1")
    # r = 0
  
    # n2  = df["ValueInside12"][r]
    # n3  = df["ValueInside13"][r]
    # n4  = df["ValueInside21"][r]
    # n5  = df["ValueInside22"][r]
    # n6  = df["ValueInside23"][r]
    # n7  = df["ValueInside31"][r]
    # n8  = df["ValueInside32"][r]
    # n9  = df["ValueInside33"][r]
    # n10 = df["ValueInside41"][r]
    # n11 = df["ValueInside42"][r]
    # n12 = df["ValueInside43"][r]

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

# FUNCTIONS

# PAGES
class Math(Page):
    form_model = 'player'
    form_fields = ['correcttables']
    timer_text = 'Time left to complete the task:'
    timeout_seconds = 120

    # @staticmethod
    # def vars_for_template(player):
    #     r = 0
    #     n1  = Constants.df["ValueInside11"][r]
    #     n2  = Constants.df["ValueInside12"][r]
    #     n3  = Constants.df["ValueInside13"][r]
    #     n4  = Constants.df["ValueInside21"][r]
    #     n5  = Constants.df["ValueInside22"][r]
    #     n6  = Constants.df["ValueInside23"][r]
    #     n7  = Constants.df["ValueInside31"][r]
    #     n8  = Constants.df["ValueInside32"][r]
    #     n9  = Constants.df["ValueInside33"][r]
    #     n10 = Constants.df["ValueInside41"][r]
    #     n11 = Constants.df["ValueInside42"][r]
    #     n12 = Constants.df["ValueInside43"][r]
    #     return {
    #         'n1' : n1,
    #         'n2' : n2,
    #         'n3' : n3,
    #         'n4' : n4,
    #         'n5' : n5,
    #         'n6' : n6,
    #         'n7' : n7,
    #         'n8' : n8,
    #         'n9' : n9,
    #         'n10' : n10,
    #         'n11' : n11,
    #         'n12' : n12,
    #     }

    @staticmethod
    def js_vars(player: Player):
     return {
    #     'n1'  : Constants.n1,
    #     'n2'  : Constants.n2,
    #     'n3'  : Constants.n3,
    #     'n4'  : Constants.n4,
    #     'n5'  : Constants.n5,
    #     'n6'  : Constants.n6,
    #     'n7'  : Constants.n7,
    #     'n8'  : Constants.n8,
    #     'n9'  : Constants.n9,
    #     'n10'  : Constants.n10,
    #     'n11'  : Constants.n11,
    #     'n12'  : Constants.n12,
    #     # 'df' : Constants.df,
        'sorted_string' : sorted_string,
     }

page_sequence = [Math]
