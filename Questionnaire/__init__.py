from otree.api import *

doc = """
Questionnaire
"""


class Constants(BaseConstants):
    name_in_url = 'Questionnaire'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
  pass


class Player(BasePlayer):
    #num_completed = models.IntegerField(initial=0)
    #num_correct = models.IntegerField(initial=0)
    #num_trials = models.IntegerField() 

    mathslider = models.FloatField(blank= True) 
    verbalslider = models.FloatField(blank= True)    
    age = models.IntegerField(label="Please enter your age:")
    gender = models.IntegerField(
        choices=[
        [1, 'Male'],
        [2, 'Female'],
        [3, 'Prefer not to say'],
        ],
        label="Please enter your gender:"
        )   
    occupation = models.StringField(label="Please enter your occupation (i.e. student/job):")
    nationality = models.StringField(label="Please enter your nationality:")



def get_current_trial(player: Player):
    return Trial.filter(player=player, choice=None)[0]


def is_finished(player: Player):
    return player.num_completed == player.num_trials


class Trial(ExtraModel):
    player = models.Link(Player)

def to_dict(trial: Trial):
    return dict(
        question=trial.question,
        optionA=trial.optionA,
        optionB=trial.optionB,
        id=trial.id,
    )

# PAGES
class Questionnairemath(Page):
    form_model = 'player'
    form_fields = ['verbalslider']

class Questionnaireverbal(Page):
    form_model = 'player'
    form_fields = ['mathslider']

class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'occupation', 'nationality']
    
    @staticmethod
    def live_method(player: Player, data):
        my_id = player.id_in_group

    

page_sequence = [Questionnairemath, Questionnaireverbal, Demographics]
