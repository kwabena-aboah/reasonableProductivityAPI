from rest_framework import serializers
from . models import User, UserProfile


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'is_admin']


class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'image',
                  'fb_profile', 'twitter_profile', 'linkedin_profile', 'website']
