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
    mathslider = models.FloatField(blank=True) 
    verbalslider = models.FloatField(blank=True)  
    confirm = models.IntegerField(
        choices=[
        [1, 'I confirm my answer'],
        ],
        widget=widgets.RadioSelect,
        label="Check this button and click next to confirm your answer.",
    )  
    confirm1 = models.IntegerField(
        choices=[
        [1, 'I confirm my answer'],
        ],
        widget=widgets.RadioSelect,
        label="Check this button and click next to confirm your answer.",
    )  
    age = models.IntegerField(label="Please enter your age:", min=18, max=100)
    gender = models.IntegerField(
        choices=[
        [1, 'Male'],
        [2, 'Female'],
        [3, 'Non-binary/ third gender'],
        [4, 'Prefer not to answer'],
        ],
        label="Please select your gender:",
        )   
    occupation = models.IntegerField(
        choices=[
        [1, 'Employed, working 36-40 hours per week'],
        [2, 'Employed, working less than 36 hours per week'],
        [3, 'Parttime job'],
        [4, 'Not employed, looking for a job'],
        [5, 'Not employed, not looking for a job'],
        [6, 'Retired'],
        [7, 'Student'],
        [8, 'Student with parttime job'],
        [9, 'Not able to work'],
        [10, 'Other'],
        ],
        label="Which of these choices is best applicable for your occupational situation?",
        ) 
    nationality = models.StringField(label="Please enter your nationality:")
    education = models.IntegerField(
        choices=[
        [1, 'Primary education'],
        [2, 'High school or equivalent'],
        [3, 'Vocational school (Dutch: MBO)'],
        [4, 'Higher education (Dutch: HBO)'],
        [5, 'Bachelors degree (Dutch: WO bachelor)'],
        [6, 'WO Masters degree (Dutch: WO master)'],
        [7, 'Doctorate (e.g., PhD, EdD)'],
        [7, 'Other'],
        ],
        label="What is the highest level of education that you have completed?",
        ) 
    firstlanguage = models.IntegerField(
        choices= [
        [1, 'Dutch'],
        [2, 'English'],
        [3, 'French'],
        [4, 'German'],
        [5, 'Irish'],
        [6, 'Italian'],
        [7, 'Portuguese'],
        [8, 'Scottish'],
        [9, 'Spanish'],
        [10, 'Other'],
        ],
        label="What is your first language?",
        ) 
    english = models.IntegerField(
        choices=[
        [1, 'Native speaker'],
        [2, 'Near native/fluent'],
        [3, 'Excellent command / highly proficient in spoken and written English'],
        [4, 'Very good command'],
        [5, 'Good command / good working knowledge'],
        [6, 'Basic communication skills / working knowledge'],
        ],
        label="How would you rank your own English language skills?",
        )  
    email = models.StringField(label="Please enter your e-mail adress if you want to be in the random selection to be paid according to your outcomes:", blank=True)


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
    form_fields = ['mathslider', 'confirm']

class Questionnaireverbal(Page):
    form_model = 'player'
    form_fields = ['verbalslider', 'confirm1']

class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'occupation', 'nationality', 'education', 'firstlanguage', 'english']

class Emailpayoff(Page):
    form_model = 'player'
    form_fields = ['email']
    
    @staticmethod
    def live_method(player: Player, data):
        my_id = player.id_in_group

    

page_sequence = [Instructions, Questionnairemath, Questionnaireverbal, Demographics, Emailpayoff]
