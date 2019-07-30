from . import models

from rest_framework import serializers


# class ProfileSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = models.Profile
#         fields = (
#             'pk',
#         )


class QuizSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Quiz
        fields = (
            'title', 'description', 'url', 'random_order', 'max_questions', 'answers_at_end', 'exam_paper', 'single_attempt', 'pass_mark', 'success_text', 'fail_text'
        )

class MCQuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Quiz
        fields = (
            'figure', 'content', 'explanation', 'answer_order'
        )

class TFQuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Quiz
        fields = (
            'figure', 'content', 'explanation', 'correct'
        )

class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Quiz
        fields = (
            'content', 'correct'
        )
