import mongoengine as me


class Manager(me.Document):
  document = me.IntField(required=True, unique=True)
  firstName = me.StringField(required=True)
  lastName = me.StringField(required=True)
  cel = me.StringField()