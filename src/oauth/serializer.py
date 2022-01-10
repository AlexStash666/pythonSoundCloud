from rest_framework import serializers


class GoogleAuth(serializers.Serializer):
    """Сериализация данных гугл"""
    email = serializers.EmailField()
    token = serializers.CharField()
