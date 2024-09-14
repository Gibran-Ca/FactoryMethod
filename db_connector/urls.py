from django.urls import path
from .views import test_connection

urlpatterns = [
    path('test-connection/<str:db_type>/', test_connection, name='test_connection'),
]
