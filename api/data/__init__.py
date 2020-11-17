from mongoengine import register_connection
from secrets import db_remote_ip

register_connection(alias='core', name='catpic',
                    host=db_remote_ip, port=27017)
register_connection(alias='default', name='catpic',
                    host=db_remote_ip, port=27017)
