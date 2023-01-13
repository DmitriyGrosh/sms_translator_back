from rest_framework import serializers

class TranslateSerializer(serializers.Serializer):
    text = serializers.CharField()
    fromLanguage = serializers.CharField(max_length=255)
    toLanguage = serializers.CharField(max_length=255)

    def create(self, validated_data):
        return validated_data