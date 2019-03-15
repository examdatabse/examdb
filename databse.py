from peewee import *
from PIL import Image

db = SqliteDatabase('database.db')


class BaseModel(Model):
    class Meta:
        database = db


class Users(BaseModel):
    id = PrimaryKeyField()
    username = CharField(null=False)
    password = CharField(null=False)
    permission = IntegerField(null=False)


class Problems(BaseModel):
    id = PrimaryKeyField(null=True)
    serial_code = CharField(null=False)
    tags = CharField(null=True)
    question = CharField(null=False)
    question_image = BlobField(null=True)
    answer = CharField(null=True)
    answer_image_a = BlobField(null=True)
    answer_image_b = BlobField(null=True)
    answer_image_c = BlobField(null=True)
    answer_image_d = BlobField(null=True)
    answer_image_e = BlobField(null=True)
    choice_1 = CharField(null=False)
    choice_2 = CharField(null=False)
    choice_3 = CharField(null=False)
    choice_4 = CharField(null=False)
    choice_5 = CharField(null=False)
    time_stamp = BigIntegerField(null=True)


if __name__ == '__main__':
    Users.create_table()
    Problems.create_table()
    # img = open('ai.jpg', 'rb').read()
    # Problems.create(serial_code='12345', testlet='asdnjan', question_image=img)
    # query = Problems.select().where(Problems.serial_code == '12345')
    # image_out = ''
    # for i in query:
    #     image_out = i.question_image
    # imgo = open('out.jpg', 'wb')
    # imgo.write(image_out)
