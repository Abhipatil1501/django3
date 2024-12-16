from django.urls import path
from kannadatext import views

urlpatterns = [
    path('store/',views.store_kannada),
    path('display/',views.display_kannada),
]