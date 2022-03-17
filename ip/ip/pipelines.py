import pymongo
from ip.settings import DB_PORT, DB_IP, DB_NAME, DB_USER, DB_PWD, DB_COLLECTION


class IpInsertMongoDBPipeline:
    def __init__(self):
        # https://pymongo.readthedocs.io/en/stable/migrate-to-pymongo4.html#database-authenticate-and-database-logout-are-removed
        # pymongo4 版本 接口不一样 3.6.1的比较好
        client = pymongo.MongoClient(DB_IP, DB_PORT, username=DB_USER, password=DB_PWD)
        db = client[DB_NAME]
        self.collection = db[DB_COLLECTION]
        self.collection.drop()

    def process_item(self, item, spider):  # 参数少了都会不执行 坑！！！！！！！！！！！！！
        self.collection.insert_one(dict(item))
        print('插入数据')
        return item


class IpPipeline:
    def process_item(self, item, spider):
        return item
