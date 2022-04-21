from .models import User
from .models import Inquiry
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        #fields = ('firstName', 'lastName', 'username', 'password', 'userType')
        fields = '__all__'


class InquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inquiry
        #fields = ('firstName', 'lastName', 'email', 'contact', 'intrestedSubject')
        fields = '__all__'