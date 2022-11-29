# pylint: disable=invalid-name
# pylint: disable=line-too-long
# imports python base
import json
import logging
import datetime 
# import terceros
from flask import session, jsonify
from flask_restful import Resource, reqparse
from mongoengine.context_managers import switch_db

# Import del sistema
from v1.resources.auth.authorization import Auth
from v1.resources.auth.dbDecorator import dbAccess
from v1.models.api_models import Model1, Model2,Model3

logger = logging.getLogger(__name__)


class Model1_CRUD(Resource):  # Clase para crear recursos REST
    @Auth.authenticate
    @dbAccess.mongoEngineAccess
    def get(self):
        parser = reqparse.RequestParser()  # creamos un objeto para obtener los datos de la request
        parser.add_argument("client", type=str, required=False, location='args',
                            help="Mensaje que devolvera en caso de parametro mal ingresado")
        data = parser.parse_args()  # obtenemos los datos de la request

        with switch_db(Model1, session["dbMongoEngine"]):
            if data["client"]:
                my_model = Model1.objects(name=data['client']).first()
                if my_model:
                    return json.loads(my_model.to_json())
                else:
                    return "Objeto no encontrado", 400
            all_data = Model1.objects()
            return json.loads(all_data.to_json())

    @Auth.authenticate
    @dbAccess.mongoEngineAccess
    def post(self):  # Se ejecutara este metodo con el metodo post del endpoint
        parser = reqparse.RequestParser()  # creamos un objeto para obtener los datos de la request
        parser.add_argument("client", type=str, required=True,
                            help="Mensaje que devolvera en caso de parametro mal ingresado")
        parser.add_argument("db_client", type=str, required=True,
                            help="Mensaje que devolvera en caso de parametro mal ingresado")
        parser.add_argument("sftp_client", type=str, required=True,
                            help="Mensaje que devolvera en caso de parametro mal ingresado")
        parser.add_argument("transcript", type=str, required=True,
                            help="Mensaje que devolvera en caso de parametro mal ingresado")
        parser.add_argument("workers", type=str, required=True,
                            help="Mensaje que devolvera en caso de parametro mal ingresado")
        data = parser.parse_args()  # obtenemos los datos de la request
        

        with switch_db(Model1, session["dbMongoEngine"]):
            my_model = Model1.objects(client=data['client']).first()
            my_model.db_client = data['db_client']
            my_model.sftp_client = data['sftp_client']
            my_model.transcript = data['transcript']
            my_model.workers = data['workers']
            my_model.idioma = "ES"
            my_model.ultimo_registro = "11/11/2020"
            my_model.ultimo_analisis = "11/11/2020"
            my_model.informe_proceso = []
            my_model.save()
        return json.loads(my_model.to_json())

    @Auth.authenticate
    @dbAccess.mongoEngineAccess
    def put(self):
        parser = reqparse.RequestParser()  # creamos un objeto para obtener los datos de la request
        parser.add_argument("client", type=str, required=True, location='args',
                            help="Mensaje que devolvera en caso de parametro mal ingresado")
        parser.add_argument("db_client", type=str, required=True, location='args',
                            help="Mensaje que devolvera en caso de parametro mal ingresado")
        parser.add_argument("sftp_client", type=str, required=True, location='args',
                            help="Mensaje que devolvera en caso de parametro mal ingresado")
        parser.add_argument("transcript", type=str, required=True, location='args',
                            help="Mensaje que devolvera en caso de parametro mal ingresado")
        parser.add_argument("workers", type=str, required=True, location='args',
                            help="Mensaje que devolvera en caso de parametro mal ingresado")
        data = parser.parse_args()  # obtenemos los datos de la request

        try:
            with switch_db(Model1, session["dbMongoEngine"]) as my_collection:
                my_model = my_collection(client=data['client'], db_client=data['db_client'], sftp_client=data['sftp_client'], 
                transcript=data['transcript'], workers=data['workers'])
                my_model.save()
        except Exception as err:
            logger.error(err)
        return json.loads(my_model.to_json())

    @Auth.authenticate
    @dbAccess.mongoEngineAccess
    def delete(self):
        parser = reqparse.RequestParser()  # creamos un objeto para obtener los datos de la request
        parser.add_argument("client", type=str, required=True, location='args',
                            help="Mensaje que devolvera en caso de parametro mal ingresado")
        data = parser.parse_args()  # obtenemos los datos de la request

        with switch_db(Model1, session["dbMongoEngine"]) as my_model:
            my_obj = my_model.objects(client=data['client']).first()
            if not my_obj:
                return {'error': 'data not found'}, 404
            my_obj.delete()
        return "Ok", 200


class Model3_rCargas(Resource):  # Clase para crear recursos REST
    @Auth.authenticate
    @dbAccess.mongoEngineAccess
    def get(self):
        parser = reqparse.RequestParser()  # creamos un objeto para obtener los datos de la request
        parser.add_argument("client", type=str, required=False, location='args',
                            help="Mensaje que devolvera en caso de parametro mal ingresado")
        data = parser.parse_args()  # obtenemos los datos de la request

        informe_proceso = []

        with switch_db(Model1, session["dbMongoEngine"]):
            if data["client"]:
                my_model = Model1.objects(client=data['client']).first()
                if my_model:
                    for item in my_model.informe_proceso:
                        carga = {'Directorio': item['Carpeta'], 'Fecha': datetime.datetime.strftime(item['Fecha'], '%d/%m/%Y')
                        , 'Audios': item['Audios'], 'Metadata': item['Metadata'], 'Tiempo': item['Tiempo']}
                        informe_proceso.append(carga)
                        
                    return jsonify({'data': informe_proceso})
                else:
                    return "Objeto no encontrado", 400
            all_data = Model1.objects()
            return json.loads(all_data.to_json())


    # documentacion sobre requestParser https://flask-restful.readthedocs.io/en/latest/reqparse.html
    # documentacion sobre decoradores https://github.com/alloxentric/KeycloakAuth
    # docuemntacion sobre flask https://flask.palletsprojects.com/en/2.0.x/
    # documentacion sobre flask restful https://flask-restful.readthedocs.io/en/latest/
