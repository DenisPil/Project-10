from rest_framework import serializers

from .models import  Contributor, Project, User,  Com, Issue


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Com
        fields = ['description', 'creator', 'issue_id', 'created_time']


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
#'comment_id_for_issue'

class IssueSerializer(serializers.ModelSerializer):

    class Meta:
        model = Issue
        fields = ['id',
                  "project_id",
                'title',
                'description',
                'tag', 
                'priority',
                'status',
                'creator',
                'assignee_user_id',
                'created_time',
                ]


class ContributorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contributor
        fields = ['id', 'project_id','contributor_id', "role"]


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'id']


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

    contributor = serializers.SerializerMethodField()
    issue_id_for_project = IssueSerializer(many=True)

    class Meta:
        model = Project
        fields = ['id',
                  'title',
                  'description',
                  'type',
                  'creator',
                  'contributor',
                  'issue_id_for_project'
                  ]
        
    def get_contributor(self, instance):
        queryset = instance.contributor.all()
        serializer = UserSerializer(queryset, many=True)
        return serializer.data

    """def get_issue_id_for_project(self, instance):
        queryset = instance.issue_id_for_project.all()
        serializer = IssueSerializer(queryset, many=True)
        return serializer.data"""

class SignupSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'username', "password"]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        account = User(email=self.validated_data['email'],
                       username=self.validated_data['username'],)
        password = self.validated_data['password']
        account.set_password(password)
        account.save()
        return account

