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
            'title', 'description', 'mcquestion', 'tfquestion', 'essayquestion', 'url', 'random_order', 'answers_at_end', 'exam_paper', 'single_attempt', 'pre_test', 'post_test', 'pass_mark', 'success_text', 'fail_text'
        )

class MCQuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Quiz
        fields = (
            'figure', 'content', 'explanation', 'answer_order'
        )

class TF_QuestionSerializer(serializers.ModelSerializer):

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
