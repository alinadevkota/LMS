from . import models

from rest_framework import serializers


class CategoryInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.CategoryInfo
        fields = (
            'pk', 
            'Category_Name', 
        )


class SurveyInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.SurveyInfo
        fields = (
            'pk', 
            'Survey_Title', 
            'Start_Date', 
            'End_Date', 
            'Survey_Cover', 
            'Use_Flag', 
        )


class QuestionInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.QuestionInfo
        fields = (
            'pk', 
            'Question_Name', 
        )


class OptionInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.OptionInfo
        fields = (
            'pk', 
            'Option_Name', 
        )


