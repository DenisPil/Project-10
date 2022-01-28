from rest_framework import serializers

from .models import Project
from issue.serializers import IssueSerializer
from user.serializers import UserSerializer
from contributor.serializers import ContributorForProjectSerializer

class ProjectSerializer(serializers.ModelSerializer):
    
    

    class Meta:
        model = Project
        fields = ['id',
                  'title',
                  'description',
                  'type',
                  'creator',
                  ]


class ProjectDetailSerializer(serializers.ModelSerializer):

    contributor = ContributorForProjectSerializer(many=True)
    id_issue = IssueSerializer(many=True)

    class Meta:
        model = Project
        fields = ['id',
                  'title',
                  'description',
                  'type',
                  'creator',
                  'id_issue',
                  'contributor',
                  ]
