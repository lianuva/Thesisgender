from otree.api import *
import pandas as pd

doc = """
Verbal
"""


class Constants(BaseConstants):
    name_in_url = 'verbal'
    players_per_group = None
    num_rounds = 1
    xl = pd.ExcelFile("INFUSCATE-ENG.xlsx")
    df = xl.parse("Sheet1")



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
  pass


class Player(BasePlayer):
    word = models.StringField(label="Enter the words you find below", blank=True)
    score = models.IntegerField(blank=True)
    
def get_current_trial(player: Player):
    return Trial.filter(player=player, choice=None)[0]


def is_finished(player: Player):
    return player.num_completed == player.num_trials


class Trial(ExtraModel):
    player = models.Link(Player)

# PAGES
class Verbal(Page):
    form_model = 'player'
    form_fields = ['word', 'score']
    #timer_text = 'Time left to complete the task:'
    #timeout_seconds = 120
    
    #@staticmethod
    # def vars_for_template(player):
    #    word  = 'hello'
    #    return {
    #        'word' : word,
    #    }

    @staticmethod
    def vars_for_template(player):
        solution  = Constants.df["Word"][0]
        return {
            'solution' : solution,
        }

class Instructionsverbal(Page):
    pass

page_sequence = [Instructionsverbal, Verbal]
