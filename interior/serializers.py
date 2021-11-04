from rest_framework import serializers
from .models import User,Company


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =['id', 'name', 'email', 'password']
        extra_kwargs = {

            'password': {'write_only': True}
        }


    def create(self,validated_data):
        password = validated_data['password']
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()

        return instance


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['title','description','timestamp']

        


        