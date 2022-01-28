from rest_framework import serializers

from .models import Contributor


class ContributorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contributor
        fields = ['id', 'project_id', 'contributor_id', "role"]


class ContributorForProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contributor
        fields = ['id', 'contributor_id', "role"]
