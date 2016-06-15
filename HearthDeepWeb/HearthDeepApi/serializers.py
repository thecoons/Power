from rest_framework import serializers
from .models import HearthLog
from django.contrib.auth.models import User

class HearthLogSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    # brutLog = serializers.CharField()
    #
    # def create(self, validated_data):
    #     return HearthLog.objects.create(**validated_data)
    #
    # def update(selg, instance, validated_data):
    #     instance.brutLog = validated_data.get('brutLog', instance.brutLog)
    #     instance.save()
    #     return instance
    class Meta:
        model = HearthLog
        fields = '__all__'

# class LogUploadSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=LogUpload
#         read_only_fields = ('created', 'owner', 'datafile')

class UserSerializer(serializers.ModelSerializer):
    # hearthlogs = serializers.PrimaryKeyRelatedField(many=True, queryset=LogUpload.objects.all())
    class Meta:
        model = User
        fields = ('id', 'username')
