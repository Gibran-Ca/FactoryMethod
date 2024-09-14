from django.http import JsonResponse
from db_connector.db_factory import ConcreteDBFactory

def test_connection(request, db_type):
    factory = ConcreteDBFactory()

    if db_type == 'mysql':
        connection_factory = factory.create_mysql_factory()
    elif db_type == 'mariadb':
        connection_factory = factory.create_mariadb_factory()
    elif db_type == 'postgresql':
        connection_factory = factory.create_postgresql_factory()
    elif db_type == 'sqlite':
        connection_factory = factory.create_sqlite_factory()
    else:
        return JsonResponse({'error': 'Invalid database type'}, status=400)

    connection = connection_factory.create_connection()
    
    try:
        connection.connect()
    finally:
        connection.close()

    return JsonResponse({'status': 'success'})
