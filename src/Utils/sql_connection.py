import pymysql

config = {
    'database': 'MERCOR_TRIAL_SCHEMA',
    'host': '35.224.61.48',
    'user': 'trial_user',
    'password': 'trial_user_12345#',
    'port': 3306
}

def get_connection():
    connection = pymysql.connect(**config)
    return connection