from curses import intrflush
from mongoengine import Document, DynamicDocument
from mongoengine import StringField, IntField, ListField


class Model1(Document):
    client = StringField(max_length=30, required=True)
    db_client = StringField(max_length=30, required=True)
    sftp_client = StringField(max_length=30, required=True)
    transcript = StringField(max_length=30, required=True)
    workers = IntField(max_length=2, required=True)
    idioma = StringField(max_length=30)
    ultimo_registro = StringField(max_length=30)
    ultimo_analisis = StringField(max_length=30)
    informe_proceso = ListField()
            
    def hello(self):
        return f"Hola {self.name}"

class Model2(DynamicDocument):
    meta = {'collection': 'model2'}


class Model3(Document):
    client = StringField(max_length=77)
    
    
class Model4(Document):
    
    metadata = StringField(max_length=30, required=True)
    tiempo = StringField(max_length=30, required=True)
    tunning = IntField(max_length=2, required=True)
