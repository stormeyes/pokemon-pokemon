import os
import nacos

NACOS_SERVER_ADDRESSES = os.environ["nacos_addr"] or "127.0.0.1:8848"
NACOS_NAMESPACE = os.environ["env"] or "dev"

SERVER_ADDR = "[::]:50051"
SERVER_MAX_WORKERS = 10
SERVER_MAX_SEND_MESSAGE_LENGTH = 100 * 1024 * 1024
SERVER_MAX_RECEIVE_MESSAGE_LENGTH = 100 * 1024 * 1024

client = nacos.NacosClient(NACOS_SERVER_ADDRESSES, namespace = NACOS_NAMESPACE)


def getDBConfig(databaseName):
    client.get_config("pokemon", "database")


def getRedisConfig(redisName):
    pass

