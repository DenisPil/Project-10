from rest_framework import serializers

from .models import  Contributor, Project, User,  Com #Issue,


class CommentSerializer(serializers.ModelSerializer):
    
    
    
    class Meta:
        model = Com
        fields = ['description', 'author_user_id', 'issue_id', 'created_time']


"""class IssueSerializer(serializers.ModelSerializer):

    comment_id_for_issue = CommentSerializer(many=True)

    class Meta:
        model = Issue
        fields = ['title',
                  'description',
                  'tag', 'priority',
                  'project_id',
                  'status',
                  'author_user_id',
                  'assignee_user_id',
                  'created_time',
                  'comment_id_for_issue'
                  ]"""

class ContributorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Contributor
        fields = ['id', 'project_id','contributor_id', "role"]
        

class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ['id',
                  'title',
                  'description',
                  'type',
                  'creator',
                  'contributor'
                  
                  ]

class ProjectDetailSerializer(serializers.ModelSerializer):
    contributor = serializers.SerializerMethodField()
    class Meta:
        model = Project
        fields = ['id',
                  'title',
                  'description',
                  'type',
                  'creator',
                  'contributor'
                  ]
    def get_contributor(self, instance):
        queryset = instance.contributor.all()
        print(queryset, '------------------------------------')
        serializer = ContributorSerializer(queryset, many=True)
        return serializer.data

class SignupSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'username', "password"]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        account = User(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            
        )
        password = self.validated_data['password']
        account.set_password(password)
        account.save()
        return account


