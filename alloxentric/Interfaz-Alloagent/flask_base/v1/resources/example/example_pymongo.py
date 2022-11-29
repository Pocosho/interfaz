# Imports base de python
#import json
#import logging

# Imports de terceros
from flask import session, g, jsonify
from flask_restful import Resource, reqparse  # , reqparse #para crear recursos REST
from bson.json_util import dumps
import pysftp
# Import del sistema
# decorador de authorization y autentificacion
from config import SftpConfig
from v1.resources.auth.authorization import Auth
from v1.resources.auth.db_decorator import pymongo_access



class EndPoint1(Resource):
    '''
    Endpoint dummy
    '''

    def get(self):
        return "Hola Mundo", 200


class EndPoint2(Resource):
    '''
    Endpoint con acceso a Mongo
    '''
    # @Auth.test_user
    @Auth.authenticate
    @pymongo_access
    def get(self):
        mydb = g.db
        qry = {"client": session["user"]["bdName"]}
        data = mydb["info"].find_one(qry)
        return f'Cliente creado a las {data["creation_date"]}', 200


class EndPoint3(Resource):
    '''
    Endpoint con Keycloak y Mongo
    '''
    @Auth.authenticate
    @pymongo_access
    def get(self):
        mydb = g.db
        qry = {"client": session["user"]["bdName"]}
        data = mydb["info"].find(qry)
        return dumps(data), 200


class EndPoint4(Resource):

    def get(self):
        filenames = []

        remote_path = "/Portafolio SFTP"
        local_path = "/Users/crist/Desktop/Nueva carpeta/descargas"

        cnopts = pysftp.CnOpts()
        cnopts.hostkeys = None

        username = SftpConfig["user"]
        password = SftpConfig["pass"]
        port = SftpConfig["port"]
        host = SftpConfig["host"]

        with pysftp.Connection(host=host, username=username, password=password, cnopts=cnopts, port=port) as sftp:
            filenames = sftp.listdir(remote_path)

        return jsonify({'lista': filenames})
class EndPoint5(Resource):

    def get(self): #parametro de cliente desde el front
        
        content = []

        parser = reqparse.RequestParser()
        parser.add_argument("client", type=str, required=True, location='args',
                            help="Mensaje que devolvera en caso de parametro mal ingresado")
        data = parser.parse_args()  # obtenemos los datos de la request 
        remote_path = "/Portafolio SFTP/" + data["client"]

        cnopts = pysftp.CnOpts()
        cnopts.hostkeys = None

        username = SftpConfig["user"]
        password = SftpConfig["pass"]
        port = SftpConfig["port"]
        host = SftpConfig["host"]

        dicc_content = []

        with pysftp.Connection(host=host, username=username, password=password, cnopts=cnopts, port=port) as sftp_client:
            content = sftp_client.listdir(remote_path)

            for directory in content:
                remote_path_directory = remote_path + "/" + directory
                diccionario = {'name_directorio': directory,
                            'cantidad': 0, 'metadata': 'No Incluye'}

                try:
                    content_directory = sftp_client.listdir(
                        remote_path_directory)
                except:
                    continue

                for archivo in content_directory:
                    if archivo.endswith('wav') or archivo.endswith('mp3'):
                        diccionario["cantidad"] += 1
                    elif archivo.endswith('csv') or archivo.endswith('xlsx'):
                        diccionario["metadata"] = archivo
                        

                dicc_content.append(diccionario)
        
        if len(dicc_content) != 0:
                    return jsonify({'client1': dicc_content})

        return jsonify({'client1': 'False'})


class Endpoint6(Resource):
    def get(self): #parametro de cliente desde el front
        
        content = []

        remote_path = "/Portafolio SFTP/Cliente2"
        local_path = "/Users/crist/Desktop/Nueva carpeta/descargas"

        cnopts = pysftp.CnOpts()
        cnopts.hostkeys = None

        username = SftpConfig["user"]
        password = SftpConfig["pass"]
        port = SftpConfig["port"]
        host = SftpConfig["host"]

        dicc_content2 = []

        with pysftp.Connection(host=host, username=username, password=password, cnopts=cnopts, port=port) as sftp_client:
            content = sftp_client.listdir(remote_path)

            for directory in content:
                remote_path_directory = remote_path + "/" + directory
                diccionario2 = {'name_directorio': directory,
                            'cantidad': 0, 'metadata': 'No Incluye'}

                try:
                    content_directory = sftp_client.listdir(
                        remote_path_directory)
                except:
                    continue

                for archivo in content_directory:
                    if archivo.endswith('wav') or archivo.endswith('mp3'):
                        diccionario2["cantidad"] += 1
                    elif archivo.endswith('csv') or archivo.endswith('xlsx'):
                        diccionario2["metadata"] = archivo
                        

                dicc_content2.append(diccionario2)

            return jsonify({'client2': dicc_content2})