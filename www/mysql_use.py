
from transwarp import db

db.create_engine(
    user='user1',
    password='a45b3643364f7f',
    database='web-app',
    host='',
    port='3306'
)

users = db.select('select * from user')

n = db.update('insert into user(id, name) values(?, ?)', 4, 'Jack')

with db.connection():
    db.select('...')
    db.update('...')

with db.transaction():
    db.select('...')
    db.update('...')


class _Engince(object):
    def __init__(self, connect):
        self._connect = connect
    def connect(self):
        return self.connect()

engince = None

