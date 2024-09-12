
from django.urls import path
from .views import test_connection

urlpatterns = [
    path('test-connection/', test_connection, name='test_connection'),
]
