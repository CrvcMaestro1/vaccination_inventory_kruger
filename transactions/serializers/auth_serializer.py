from rest_framework import serializers


class AuthTokenResponseSerializer(serializers.Serializer):
    token = serializers.CharField(label="Token")
    email = serializers.EmailField(label="Email")

    def update(self, instance, validated_data):
        raise NotImplementedError()

    def create(self, validated_data):
        raise NotImplementedError()
