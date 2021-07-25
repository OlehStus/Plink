import string

from rest_framework import serializers
from . import models
from .models import MyUser
import re


class MyUserDetailSerializer(serializers.ModelSerializer):

    symbols_password = '(,),*,-,+,=,&,^,%,$,#,@,!,{,},",:,;,?,/,<,>,., ,'
    sp = symbols_password.split(',')
    symbols_fn = '(,),*,+,=,&,^,%,$,#,@,!,{,},",:,;,?,/,<,>,., ,'
    sf = symbols_fn.split(',')
    symbols_ln = '(,),*,+,=,&,^,%,$,#,@,!,{,},",:,;,?,/,<,>,.,'
    sl = symbols_ln.split(',')
    email = serializers.EmailField(max_length=100)
    password = serializers.CharField(max_length=16, min_length=7)
    first_name = serializers.CharField(max_length=255, min_length=2)
    last_name = serializers.CharField(max_length=255, min_length=2)

    class Meta:
        model = MyUser
        fields = '__all__'

    def validate(self, attrs):

        email = attrs.get('email', '')
        password = attrs.get('password', '')
        first_name = attrs.get('first_name', '')
        last_name = attrs.get('last_name', '')
        exception_email = email.split('@')
        if re.compile('gmail.com').findall(exception_email[1]) or re.compile('icloud.com').findall(exception_email[1]) \
                or set(string.punctuation).intersection(exception_email[0]):
            raise serializers.ValidationError('Email has non-typical view')
        if not set(string.ascii_uppercase).intersection(password) or set(string.punctuation).intersection(password):
            raise serializers.ValidationError('Password has non-typical view')
        if any(map(str.isdigit, first_name)) or set(string.punctuation).intersection(first_name):
            raise serializers.ValidationError('First name has non-typical view')
        if any(map(str.isdigit, last_name)) or set(string.punctuation).intersection(last_name):
            raise serializers.ValidationError('Last name has non-typical view')
        return attrs

    def create(self, validated_data):
        return super().create(validated_data)



class MyUserListSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = MyUser
        fields = ('id', 'first_name', 'user')

