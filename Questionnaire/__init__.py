from otree.api import *

doc = """
Questionnaire
"""


class Constants(BaseConstants):
    name_in_url = 'questionnaire'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
  pass


class Player(BasePlayer):
    mathslider = models.FloatField(blank= True) 
    verbalslider = models.FloatField(blank= True)    
    age = models.IntegerField(label="Please enter your age:", blank=True)
    gender = models.IntegerField(
        choices=[
        [1, 'Male'],
        [2, 'Female'],
        [3, 'Prefer not to say'],
        ],
        label="Please enter your gender:",
        blank=True
        )   
    occupation = models.StringField(label="Please enter your occupation (i.e. student/job):", blank=True)
    nationality = models.StringField(label="Please enter your nationality:", blank=True)
    email = models.StringField(label="Please enter your nationality:", blank=True)


def get_current_trial(player: Player):
    return Trial.filter(player=player, choice=None)[0]


def is_finished(player: Player):
    return player.num_completed == player.num_trials


class Trial(ExtraModel):
    player = models.Link(Player)

# PAGES
class Instructions(Page):
    pass
    
class Questionnairemath(Page):
    form_model = 'player'
    form_fields = ['mathslider']

class Questionnaireverbal(Page):
    form_model = 'player'
    form_fields = ['verbalslider']

class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'occupation', 'nationality']

class Emailpayoff(Page):
    form_model = 'player'
    form_fields = ['email']
    
    @staticmethod
    def live_method(player: Player, data):
        my_id = player.id_in_group

    

page_sequence = [Instructions, Questionnairemath, Questionnaireverbal, Demographics, Emailpayoff]
