from django.contrib import admin
from django.urls import path
from translator.views import TranslatorAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/translate', TranslatorAPIView.as_view())
]
