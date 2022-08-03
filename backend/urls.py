from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('user_card/', include('backend.user_card.urls'))
]
