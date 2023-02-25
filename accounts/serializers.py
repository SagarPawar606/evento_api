from rest_framework import serializers
from django.contrib.auth.models import User


class getUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields  = ('id','first_name', 'last_name', 'username', 'email', 'is_active', 'is_staff')
        extra_kwargs = {'id' : {'read_only' : True}}


class registerUserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'})      

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password', 'password2')
        extra_kwargs = {
            'password' : {'write_only' : True},
            'password2' : {'write_only' : True},
        }
    
    #this method will be executed on serilizer.save() in view
    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password':'Both passwords must match'})
        else:
            new_user = User(
                username = self.validated_data['username'],
                first_name = self.validated_data['first_name'],
                last_name = self.validated_data['last_name'],
                email = self.validated_data['email'],
                )
            new_user.set_password(password)
            new_user.save()

            return new_user
            

            

