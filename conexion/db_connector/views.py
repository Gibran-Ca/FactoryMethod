from django.shortcuts import render

from django.http import JsonResponse
from db_connector.mysql_factory import MySQLConnectionFactory

def test_connection(request):
    factory = MySQLConnectionFactory()
    connection = factory.create_connection()
    
    try:
        connection.connect()
      
    finally:
        connection.close()
    
    return JsonResponse({'status': 'success'})

