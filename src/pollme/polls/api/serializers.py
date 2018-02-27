"""
serializers.py
Lawrence Thompson
02/27/2018
Takes the Model data, serializes it, which then gets used by views.
"""

# imports the ModelSerializer and SerializerMethodField
from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField
)

#import models from higher package.
from ..models import Question, Choice


class QuestionListSerializer(ModelSerializer):
    """
    This serializer serializes the Question model
    It should also include a field "choices" that will serialize all the
        choices for a question
    You well need a SerializerMethodField for choices,
        http://www.django-rest-framework.org/api-guide/fields/#serializermethodfield
    Reference this stack overflow for the choices:
        https://stackoverflow.com/questions/33945148/return-nested-serializer-in-serializer-method-field
    """
    choices = SerializerMethodField()

    class Meta:
        model = Question
        fields = ['text', 'id', 'pub_date', 'choices']

    def get_choices(self, object):
        """
        Get choices for the choices field by builtins and get_<field>.
        object - a question being passed in.
        Returns .data as a Python native datatype with all related objects in.
        """
        check_choices = object.choice_set.all()
        return ChoiceSerializer(check_choices, many=True).data

class ChoiceSerializer(ModelSerializer):
    """
    This serializes the Choice model. Many-to-one with Question.
    """
    class Meta:
        model = Choice
        fields = ['question', 'choice_text', 'votes']


    
    