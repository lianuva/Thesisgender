from otree.api import *
import pandas as pd
from openpyxl import load_workbook
import json
import csv

doc = """
Verbal
"""


class Constants(BaseConstants):
    name_in_url = 'verbal'
    players_per_group = None
    num_rounds = 1
    df = pd.read_csv("_static/Verbal/INFUSCATE-ENG.csv")

# Dump solution to json   
x = {
    "solution"  : Constants.df["Word"].tolist(),
}
solution_string = json.dumps(x)

# Dump points to json   
y = {
    "points"  : Constants.df["Points"].tolist(),
}
points_string = json.dumps(y)

# Number of correct words in excel sheet:
numberofsolutions = len(Constants.df["Word"]) 

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
  pass


class Player(BasePlayer):
    score = models.IntegerField(blank=True)

# PAGES
class Verbal(Page):
    form_model = 'player'
    form_fields = ['score']
    timer_text = 'Time left to complete the task:'
    timeout_seconds = 20

    @staticmethod
    def vars_for_template(player):
        longword  = Constants.df["Longword"][0]
        return {
            'longword' : longword,
        }

    @staticmethod
    def js_vars(player: Player):
        return {
            'solution_string'   : solution_string,
            'points_string'     : points_string,
            'numberofsolutions' : numberofsolutions,
        }

class Instructionsverbal(Page):
    pass

page_sequence = [Instructionsverbal, Verbal]
