from otree.api import *

doc = """
Results
"""


class Constants(BaseConstants):
    name_in_url = 'Results'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass


class Player(BasePlayer):
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
    email       = models.StringField(label="Please enter your e-mail adress if you want to be in the random selection to be paid according to your outcomes:", blank=True)
    nickname    = models.StringField(label="If you want to receive this ranking to see how good you performed relative to other participants, please enter your nickname:", blank=True)
    mobile      = models.IntegerField(
        label="What device did you use to participate in this study?",
        choices=[
        [1, 'Laptop'],
        [2, 'Computer'],
        [3, 'Mobile'],
        [4, 'Tablet'],
        [4, 'Other'],
        ],
        blank=True,
        )

# PAGES
class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'occupation', 'nationality', 'education', 'firstlanguage', 'english', 'mobile']

class Results(Page):
    form_model = 'player'
    form_fields = ['email', 'nickname']

class Goodbye(Page):
    pass
    

page_sequence = [Demographics, Results, Goodbye]
