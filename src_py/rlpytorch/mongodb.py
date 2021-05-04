"""使用mongo存储或读取"""
from pymongo import MongoClient

DB_HOST = "192.168.3.6"


class Connect(object):
    @staticmethod
    def get_connection():
        # 使用默认值
        return MongoClient(DB_HOST, 27017)


def get_db(db_name='xiangqi'):
    client = Connect.get_connection()
    return client[db_name]
