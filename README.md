# analyticalls

Aplicación que consulta una url y recoge los datos de esa url mediante json , y los guarda en una base de datos PostgreSql.
Se implementa una API mediante la django rest framework, las funciones de la api implementadas son las siguientes:

    /api/importJson: GET, POST, DELETE       # GET list of retreived data, POST new data, DELETE all data
    /api/importJson/:id: GET, PUT, DELETE    # GET data by pk (id), PUT new data, DELETE data
    /api/importJson/all: GET                 # GET all retreived data
    
Para comenzar a obtener datos de la url mediante json cada minuto y guardarlos en la BBDD, basta con lanzar el comando "import_from_url":

    python manage.py import_from_url
