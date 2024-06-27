import pymysql

config = {
    'host': '35.224.61.48',
    'user': 'trail_user',
    'password': 'trail_user_12345#',
    'port': 3306
}

def get_connection():
    connection = pymysql.connect(**config)
    return connection