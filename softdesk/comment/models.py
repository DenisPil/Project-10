from django.db import models

from user.models import User
from issue.models import Issue

class Com(models.Model):

    """ Classe qui représente le model des commentaires """

    description = models.fields.CharField(max_length=2048)
    creator = models.ForeignKey(User,
                                on_delete=models.CASCADE,
                                related_name='author_user_id_comment')
    issue_id = models.ForeignKey(Issue,
                                 on_delete=models.CASCADE,
                                 related_name='comment_id_for_issue')
    created_time = models.DateTimeField(auto_now_add=True)
