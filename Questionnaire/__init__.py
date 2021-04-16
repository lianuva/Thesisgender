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


def creating_session(subsession: Subsession):
    for p in subsession.get_players():
        stimuli = read_csv()
        p.num_trials = len(stimuli)
        #for stim in stimuli:
        #   Trial.create(player=p, **stim)


class Group(BaseGroup):
  pass


class Player(BasePlayer):
    #num_completed = models.IntegerField(initial=0)
    #num_correct = models.IntegerField(initial=0)
    #num_trials = models.IntegerField()
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
    word = models.StringField(label="Enter the words you find in the word below")
    
    

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


def read_csv():
    import csv
    import random

    f = open('Questionnaire/stimuli.csv', encoding='utf8')
    rows = list(csv.DictReader(f))

    random.shuffle(rows)
    return rows


# PAGES
class Welcome(Page):
    pass

class Verbal(Page):
    form_model = 'player'
    form_fields = ['word']

class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'occupation','nationality']
    
    @staticmethod
    def live_method(player: Player, data):
        my_id = player.id_in_group

       #if 'choice' in data:
       #     if is_finished(player):
       #         return
       #     trial = get_current_trial(player)
       #     if data['trialId'] != trial.id:
       #         return
       #     trial.choice = data['choice']
       #     trial.is_correct = trial.choice == trial.solution
       #     player.num_correct += int(trial.is_correct)
       #    player.num_completed += 1

       #if is_finished(player):
       #     return {my_id: dict(status='finished')}
       #    return {my_id: dict(status='next_stimulus', stimulus=to_dict(get_current_trial(player)))}

class Questionnaire(Page):
    pass

class Results(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return dict(trials=Trial.filter(player=player))
    pass


page_sequence = [Welcome, Verbal, Demographics, Questionnaire, Results]
