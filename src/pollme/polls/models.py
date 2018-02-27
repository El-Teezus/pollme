"""
models.py
Lawrence Thompson
02/27/18
The Question and Choice models, created as they were through
lab3 and lab4
"""

from django.db import models

# Create your models here.
class Question(models.Model):
    """
    Question class for the Pollme API
    Arguments:
       text: the text of the question.
       pub_date: the date the question was created.
    Creates a Question object that can be seen in the API.
    To create this object, use http://127.0.0.1:8000/admin
    """
    text = models.TextField()
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        """
        Return first 50 characters of text using a slice
        """
        return self.text[:50]

class Choice(models.Model):
    """
    Choice class for the Pollme API.
    In a many-to-one relationship with Questions.
    Arguments:
        question: Question the choice is linked to.
        choice_text: the choice that can be voted on.
        votes: the number of votes the choice has gotten.
    Creates a Choice object that can be seen in the API.
    To create this object, use http://127.0.0.1:8000/admin
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE, default = 1)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        """
        Return question[:25] + choice_text[:25]
        """
        return "{} - {}".format(self.question.text[:25], self.choice_text[:25])
