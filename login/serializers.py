from django.db.models import Q # for queries
from rest_framework import serializers
from re import S
    

class UserLoginSerializer(serializers.Serializer):

    mobile_no = serializers.RegexField(r"^[0-9]{9,10}$", error_messages={"invalid": "Invalid mobile number"})
    password = serializers.CharField(max_length=30)


