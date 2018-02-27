from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField
)

from ..models import Question, Choice

# class ChoiceSerializer(ModelSerializer):
#     class Meta:
#         model = Choice
#         fields = ('question', 'choice_text', 'votes')

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
        check_choices = object.choice_set.all()
        return ChoiceSerializer(check_choices, many=True).data

class ChoiceSerializer(ModelSerializer):
    """
    This serializes the Choice model
    """
    #what do i want to do
    class Meta:
        model = Choice
        fields = ['question', 'choice_text', 'votes']


    
    