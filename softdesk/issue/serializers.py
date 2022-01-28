from rest_framework import serializers

from .models import Issue
from comment.serializers import CommentSerializer


class IssueDetailSerializer(serializers.ModelSerializer):

    comment_id_for_issue = CommentSerializer(many=True)

    class Meta:
        model = Issue
        fields = ['title',
                  'description',
                  'tag',
                  'priority',
                  'project_id',
                  'status',
                  'creator',
                  'assignee_user_id',
                  'created_time',
                  'comment_id_for_issue'
                  ]

class IssueSerializer(serializers.ModelSerializer):

    class Meta:
        model = Issue
        fields = ['id',
                  'description',
                  'title',
                  'tag',
                  'priority',
                  'status',
                  'creator',
                  'assignee_user_id',
                  'project_id',
                  'created_time',
                  ]
