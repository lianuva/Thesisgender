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
    num_rounds = 2
    df = pd.read_csv("_static/Verbal/verbalwords.csv")

# Dump solution word1 to json   
x = {
    "solution"  : Constants.df["Word"].tolist(),
}
solution_string = json.dumps(x)

# Dump points word 1to json   
y = {
    "points"  : Constants.df["Points"].tolist(),
}
points_string = json.dumps(y)

# Dump solution word2 to json
w = {
    "solution2"  : Constants.df["Word2"].tolist(),
}
solution_string2 = json.dumps(w)

# Dump points to json   
z = {
    "points2"  : Constants.df["Points2"].tolist(),
}
points_string2 = json.dumps(z)

# Number of correct words in excel sheet:
numberofsolutions = len(Constants.df["Word"]) 
numberofsolutions2 = len(Constants.df["Word2"]) 

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
    timeout_seconds = 30

    @staticmethod
    def vars_for_template(player):
        if player.round_number ==1:
            longword  = Constants.df["Longword"][0]
            return {
                'longword'  : longword,
            }
        else:
            longword = Constants.df["Longword2"][0]
            return {
                'longword'  : longword,
            }

    @staticmethod
    def js_vars(player: Player):
        return {
            'solution_string'       : solution_string,
            'points_string'         : points_string,
            'numberofsolutions'     : numberofsolutions,
            'solution_string2'      : solution_string2,
            'points_string2'        : points_string2,
            'numberofsolutions2'    : numberofsolutions2,
            'round_number'          : player.round_number,
        }

    @staticmethod
    def before_next_page(player, timeout_happened):
        if player.round_number == 1:
            player.participant.score = player.score
            player.participant.verbalpayoff = round(player.score/10,2)
        else :
            player.participant.score2 = player.score
            player.participant.verbalpayoff2 = round(player.score/10,2)

class Instructionsverbalround1(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

class Instructionsverbalround2(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == 2

page_sequence = [Instructionsverbalround1, Instructionsverbalround2, Verbal]
