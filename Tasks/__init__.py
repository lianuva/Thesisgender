from otree.api import *
import pandas as pd
import json
import csv
import random

doc = """
Tasks
"""

class Constants(BaseConstants):
    name_in_url = 'tasks'
    players_per_group = None
    tasks = ['1', '2']
    num_rounds = len(tasks)
    df = pd.read_csv("_static/Math/Matrices.csv")
    dv = pd.read_csv("_static/Verbal/verbalwords.csv")
   
u = {
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

sorted_string = json.dumps(u)

# Dump solution word1 to json   
x = {
    "solution"  : Constants.dv["Word"].tolist(),
}
solution_string = json.dumps(x)

# Dump points word1 to json   
y = {
    "points"  : Constants.dv["Points"].tolist(),
}
points_string = json.dumps(y)

# Dump solution word2 to json
w = {
    "solution2"  : Constants.dv["Word2"].tolist(),
}
solution_string2 = json.dumps(w)

# Dump points to json   
z = {
    "points2"  : Constants.dv["Points2"].tolist(),
}
points_string2 = json.dumps(z)

# Number of correct words in excel sheet:
numberofsolutions = len(Constants.dv["Word"]) 
numberofsolutions2 = len(Constants.dv["Word2"]) 

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    correcttablespractice   = models.IntegerField(blank=True)
    correcttables           = models.IntegerField(blank=True)
    correcttables2           = models.IntegerField(blank=True)
    score                   = models.IntegerField(blank=True)
    score2                   = models.IntegerField(blank=True)

# FUNCTIONS
# randomize next app
def creating_session(subsession: Subsession):
    if subsession.round_number == 1:
        for p in subsession.get_players():
            round_numbers = list(range(1, Constants.num_rounds + 1))
            random.shuffle(round_numbers)
            p.participant.vars['task_rounds'] = dict(zip(Constants.tasks, round_numbers))
            print(p.participant.vars['task_rounds'])

# PAGES
class Verbal(Page):
    form_model = 'player'
    form_fields = ['score']
    timer_text = 'Time left to complete the task:'
    timeout_seconds = 120
    
    @staticmethod
    def vars_for_template(player):
        if player.participant.vars['task_rounds']['1']:
            longword  = Constants.dv["Longword"][0]
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
            'round_number'          : 1,
        }
    
    @staticmethod
    def before_next_page(player, timeout_happened):
        player.participant.score = player.score
        player.participant.verbalpayoff = player.score/10
 

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.vars['task_rounds']['1']


class Verbal2(Page):
    form_model = 'player'
    form_fields = ['score2']
    timer_text = 'Time left to complete the task:'
    timeout_seconds = 120
    
    @staticmethod
    def vars_for_template(player):
        if player.participant.vars['task_rounds']['1']:
            longword = Constants.dv["Longword2"][0]
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
            'round_number'          : 2,
        }

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.participant.score2 = player.score2
        player.participant.verbalpayoff2 = player.score2/10

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.vars['task_rounds']['1']

class Verbalinstructionsround1(Page):    
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.vars['task_rounds']['1']

class Verbalinstructionsround2(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.vars['task_rounds']['1']

class Mathpractice(Page):
    form_model = 'player'
    form_fields = ['correcttablespractice']

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.vars['task_rounds']['2']

class Math(Page):
    form_model      = 'player'
    form_fields     = ['correcttables']
    timer_text      = 'Time left to complete the task:'
    timeout_seconds = 120
            
    @staticmethod
    def js_vars(player: Player):
     return {
        'sorted_string' : sorted_string,
        'round_number'  : 1,
    }

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.participant.correcttables = player.correcttables  
    
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.vars['task_rounds']['2']

class Math2(Page):
    form_model      = 'player'
    form_fields     = ['correcttables2']
    timer_text      = 'Time left to complete the task:'
    timeout_seconds = 120
            
    @staticmethod
    def js_vars(player: Player):
     return {
        'sorted_string' : sorted_string,
        'round_number'  : 2,
    }

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.participant.correcttables2 = player.correcttables2 
    
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.vars['task_rounds']['2']

class Mathwaitpageround1(Page):    
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.vars['task_rounds']['2']

class Mathwaitpageround2(Page):    
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.vars['task_rounds']['2']

page_sequence = [Mathpractice, Mathwaitpageround1, Math, Mathwaitpageround2, Math2, Verbalinstructionsround1, Verbal, Verbalinstructionsround2, Verbal2]
