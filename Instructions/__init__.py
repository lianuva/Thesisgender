from otree.api import *
import random
import json

doc = """
Instructions
"""

class Constants(BaseConstants):
    name_in_url = 'instructions'
    players_per_group = None
    num_rounds = 1

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
    os1 = models.StringField(blank=True)

# PAGES
class Welcome(Page):
    form_model = 'player'
    form_fields = ['consent', 'os1']
    # form_fields = ['consent']

page_sequence = [Welcome]
