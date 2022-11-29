# obtenemos la clase del recurso que tenemos en el archivo example.py para utilizarlo en un endpoint
#from v1.resources.example.example import Role
from v1.resources.example.example_pymongo import EndPoint1, EndPoint2, EndPoint3, EndPoint4, EndPoint5, Endpoint6
from v1.resources.example.example_crud import Model1_CRUD,Model3_rCargas

def initialize_routes(api):
    '''
    En el endpoint le indicamos el recurso keycloak a utilizar
    con el formato "auth:nombrerecurso:explicacion_corta"
    '''
    #api.add_resource(Role, '/role', endpoint='auth:flask_base:dev', methods=['GET','POST',])
    api.add_resource(EndPoint1, '/endpoint1', endpoint='auth:recurso1', methods=['GET',])
    api.add_resource(EndPoint2, '/endpoint2', endpoint='auth:recurso2', methods=['GET',])
    api.add_resource(EndPoint3, '/endpoint3', endpoint='auth:recurso3', methods=['GET',])
    api.add_resource(Model1_CRUD, '/model1', endpoint='auth:recurso4', methods=['GET', 'POST', 'PUT', 'DELETE'])
    api.add_resource(EndPoint4, '/endpoint4', endpoint='auth:recurso5', methods=['GET',])
    api.add_resource(EndPoint5, '/endpoint5', endpoint='auth:recurso6', methods=['GET',])
    api.add_resource(Model3_rCargas, '/model3', endpoint='auth:recurso7', methods=['GET',])