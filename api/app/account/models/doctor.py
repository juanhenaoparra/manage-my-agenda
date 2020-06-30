import mongoengine as me


class Doctor(me.DynamicDocument):
  document = me.IntField(required=True, unique=True)
  idCard = me.StringField()
  firstName = me.StringField(required=True)
  lastName = me.StringField(required=True)
  cel = me.StringField()