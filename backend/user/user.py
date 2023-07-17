import json
import hashlib

class User:
    
    ALIVE_COOKIES = []
    
    def __init__(self, info_tuple):
        '''
        ID bigint AI
        nick_name varchar(50)
        account varchar(50) PK
        password varchar(50) PK
        image mediumblob
        telephone varchar(20)
        gender varchar(2)
        email varchar(50)
        QQ varchar(20)
        weChat
        '''

        if len(info_tuple) != 0:
            info_tuple = info_tuple[0]
            keys = ['ID','nickname','account','password','image','telephone','gender','email','QQ','weChat']
            self.info = { keys[i]:info_tuple[i] if info_tuple[i] != None else '' for i in range(len(keys))}
        else:
            self.info = {}

    @staticmethod
    def encode(password):
        sha1_obj = hashlib.sha1()
        sha1_obj.update(password.encode('utf-8'))
        return sha1_obj.hexdigest()
    
    def getCookie(self):
        return {
            'key': 'nickname',
            'value': self.info['nickname']
        }
    
    def __str__(self):
        return json.dumps(self.info, ensure_ascii=False)
