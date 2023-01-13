from rest_framework.response import Response
from rest_framework.views import APIView
from googletrans import Translator

from .serializers import TranslateSerializer

class TranslatorAPIView(APIView):
    def get(self, request):
        return Response({'translate': 'text'})
    def post(self, request):
        serializer = TranslateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        translator = Translator()

        toLanguage = serializer.validated_data.get('toLanguage')
        fromLanguage = serializer.validated_data.get('fromLanguage')

        translated = translator.translate(serializer.validated_data.get('text'), src=fromLanguage, dest=toLanguage)

        return Response({'translate': translated.text})

