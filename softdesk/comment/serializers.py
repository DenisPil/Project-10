from rest_framework import serializers

from .models import Com


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Com
        fields = ['id', 'description', 'creator', 'issue_id', 'created_time']