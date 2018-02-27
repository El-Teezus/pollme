from django.db import models

# Create your models here.
class Question(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        """
        Return first 50 characters of text using a slice
        """
        return self.text[:50]

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, default = 1)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        """
        Return question[:25] + choice_text[:25]
        """
        return "{} - {}".format(self.question.text[:25], self.choice_text[:25])
