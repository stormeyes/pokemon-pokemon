import Config
import peewee
from playhouse.mysql_ext import JSONField


dbConfig = Config.getDBConfig("pokemon")
db = peewee.MySQLDatabase(host=dbConfig["host"], port=dbConfig["port"])


class Pokemon(peewee.Model):
    no = peewee.IntegerField()
    name = peewee.CharField()
    form = peewee.CharField()
    category = peewee.CharField()
    gen = peewee.IntegerField()
    type = JSONField()
    ability = JSONField()
    stat = JSONField()
    height = peewee.IntegerField()
    weight = peewee.IntegerField()
    genderRatio = JSONField()
    eggGroup = JSONField()
    hatchSteps = peewee.IntegerField()

    class Meta:
        database = db
        db_table = 'pokemon'
