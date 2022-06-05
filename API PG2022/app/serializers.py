from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from vm_formacao.models import Employeer, Formation, PaymentsControlUssd, PaymentsControlUssdMercados,Plano, RequestControlUssd, Taximota, Transporte, Quiz, RequestsUssd, Notario
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],
                                        validated_data['email'],
                                        validated_data['password'])

        return user


class EmployeerSerializer(serializers.ModelSerializer):
    validate = serializers.DateField(format="%d-%b-%y")

    class Meta:
        model = Employeer
        fields = '__all__'


class FormationSerializer(serializers.ModelSerializer):
    validity = serializers.DateField(format="%d-%b-%y")
    trabalhador = EmployeerSerializer()

    class Meta:
        model = Formation
        fields = '__all__'


class TransporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transporte
        fields = '__all__'


class ChoiceField(serializers.ChoiceField):

    def to_representation(self, obj):
        if obj == '' and self.allow_blank:
            return obj
        return self._choices[obj]

    def to_internal_value(self, data):
        if data == '' and self.allow_blank:
            return ''

        for key, val in self._choices.items():
            if val == data:
                return key
        self.fail('invalid_choice', input=data)


class AddFormationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formation
        fields = '__all__'


class RequestControlUssdSerializer(serializers.ModelSerializer):
    date = serializers.DateField(format="%d-%b-%y")

    class Meta:
        model = RequestControlUssd
        fields = '__all__'


class RequestsUssdSerializer(serializers.ModelSerializer):
    date = serializers.DateField(format="%d-%b-%y")

    class Meta:
        model = RequestsUssd
        fields = '__all__'


class PaymentsControlSerialazer(serializers.ModelSerializer):
    class Meta:
        model = PaymentsControlUssd
        fields = '__all__'

class PaymentsControlMercadosSerialazer(serializers.ModelSerializer):
    class Meta:
        model = PaymentsControlUssdMercados
        fields = '__all__'


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'


class PlanoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plano
        fields = '__all__'


class TaximotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taximota


class NotarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notario
        fields = '__all__'
