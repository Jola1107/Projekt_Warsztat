from clcrypto import hash_password

#created class Users
class Users:
    def __init__(self, username='', password='', salt=''):
        self._id = -1
        self.username = username
        self._hashed_password = hash_password(password, salt)

#Readable attributes that I share externally
    @property
    def id(self):
        return self._id

    @property
    def hashed_password(self):
        return self._hashed_password

#passord change
    def set_password(self, password, salt =''):
        self._hashed_password = hash_password(password, salt)

    @hash_password.setter
    def hashed_password(self, password):
        self.set_password(password)
#add date to table users
    def save_to_db(self, cursor):
        if self._id == -1:
            sql = """INSERT INTO users(username, hashed_password)
                  VALUES (%s, %s) RETURNING id"""
            values = (self.username, self.hashed_password)
            cursor.execute(sql, values)
            self._id = cursor.fetchone()[0]
            return True
        else:
            sql = """UPDATE Users SET username = %s, hashed_password = %s WHERE id = %s"""
            values = (self.username, self. hashed_password, self.id)
            cursor.execute(sql, values)
            return True

#load data by username
    @staticmethod
    def load_user_by_username(cursor, username_):
        sql = """SELECT id, username, hashed_password FROM Users WHERE username = %s"""
        cursor.execute(sql, username_)
        data = cursor.fetchone()
        if data:
            id_, username_, hashed_password = data
            loaded_user = Users(username_)
            loaded_user._id = id
            loaded_user._hashed_password = hash_password
            return loaded_user

#load data by id
    @staticmethod
    def load_user_by_id(cursor, id_):
        sql = """SELECT id, username, hashed_password FROM Users WHERE id=%s"""
        cursor.execute(sql, (id_))
        data = cursor.fetchone()
        if data:
            id_, username, hashed_password = data
            loaded_user = Users(username)
            loaded_user._id = id_
            loaded_user._hashed_password = hashed_password
            return loaded_user

#load data all users
    @staticmethod
    def load_all_users(cursor):
        sql = """SELECT id, username, hashed_password FROM Users"""
        users = []
        cursor.execute(sql)
        for row in cursor.fetchall():
            id_, username, hashed_password = row
            loaded_user = Users(username)
            loaded_user._id = id_
            loaded_user._hashed_password = hashed_password
            users.append(loaded_user)
        return users

#delete users by id
    @staticmethod
    def delete(self, cursor):
        sql = """DELETE FROM Users WHERE id=%s"""
        cursor.execute(sql,(self.id))
        self._id = -1
        return True

#create class for messages

class Message:
    def __init__(self, from_id, to_id, text):
        self._id = -1
        self.from_id = from_id
        self.to_id = to_id
        self.text = text
        self._creation_date = None

# Readable attributes that I share externally
    @property
    def id(self):
        return self._id

    @property
    def creation_date(self):
        return self._creation_date

#add or update message in table Messages
    def save_to_db(self, cursor):
        if self._id == -1:
            sql = """INSERT INTO Messages(from_id, to_id, text) 
            VALUES (%s, %s, %s) RETURNING id, creation_date"""
            values = (self.from_id, self.to_id, self.text)
            cursor.execute(sql, values)
            self._id, self._creation_date= cursor.fetchone()
            return True
        else:
            sql = """UPDATE Messages SET from_id = %s, to_id = %s, text = %s
             WHERE id = %s"""
            values = (self.from_id, self.to_id, self.text, self.id)
            cursor.execute(sql, values)
            return True

#load message
    @staticmethod
    def load_all_masseges(cursor, user_id = None):
        if user_id:
            sql = """SELECT id, from_id, to_id, creation_date, text FROM Messages 
            WHERE to_id = %s"""
            cursor.execute(sql,(user_id))
        else:
            sql = """SELECT id, from_id, to_id, creation_date, text FROM Messages"""
            cursor.execute(sql)
        messages = []
        for row in cursor.fetchall():
            id, from_id, to_id, creation_date, text = row
            loaded_message = Message(from_id, to_id, text)
            loaded_message._id = id_
            loaded_message._creation_date= creation_date
            messages.append(loaded_message)
        return messages








