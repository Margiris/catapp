from mongoengine import register_connection

register_connection(alias='core', name='catpic',
                    host='192.168.0.102', port=27017)
register_connection(alias='default', name='catpic',
                    host='192.168.0.102', port=27017)
