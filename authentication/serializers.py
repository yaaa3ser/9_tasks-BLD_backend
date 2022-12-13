from users.models import User
from rest_framework import serializers,validators

class RegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField()
    password2 = serializers.CharField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'bio']
        extra_kwargs = {
            'password1': {'write_only': True}
            }
        
    def create(self, validated_data):
        if validated_data['password1'] == validated_data['password2']:
            user = User.objects.create_user(
                username=validated_data['username'],
                email=validated_data['email'],
                password=validated_data['password1'],
                bio = validated_data['bio']
            )
            return user
        raise serializers.ValidationError("passwords doesn't match")

        