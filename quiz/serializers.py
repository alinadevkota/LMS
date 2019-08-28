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
            'title', 'description', 'mcquestion', 'tfquestion', 'saquestion', 'url', 'cent_code', 'course_code', 'chapter_code', 'duration', 'random_order', 'answers_at_end', 'exam_paper', 'single_attempt', 'pre_test', 'post_test', 'pass_mark', 'success_text', 'fail_text'
        )

class MCQuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.MCQuestion
        fields = (
            'figure', 'content', 'course_code', 'explanation', 'cent_code', 'answer_order'
        )

class TF_QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.TF_Question
        fields = (
            'figure', 'content', 'course_code', 'explanation', 'cent_code', 'correct'
        )

class SA_QuestionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.SA_Question
        fields = (
            'figure', 'content', 'course_code', 'explanation', 'cent_code'
        )

class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Answer
        fields = (
            'question', 'content', 'correct'
        )
