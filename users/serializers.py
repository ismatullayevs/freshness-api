from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    avatar_thumbnail = serializers.ImageField(read_only=True)
    email = serializers.EmailField(read_only=True)
    date_joined = serializers.DateTimeField(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'phone_number', 'avatar', 'avatar_thumbnail',
                  'first_name', 'last_name', 'date_joined')
