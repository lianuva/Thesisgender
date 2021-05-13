from otree.api import *
import pandas as pd
from openpyxl import load_workbook
import json
import csv

doc = """
Math
"""

class Constants(BaseConstants):
    name_in_url = 'mathpractice'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    correcttablespractice = models.IntegerField(blank=True)

# FUNCTIONS

# PAGES
class Mathpractice(Page):
    form_model = 'player'
    form_fields = ['correcttablespractice']


page_sequence = [Mathpractice]
