import mongoengine as me


class Patient(me.DynamicDocument):
  document = me.IntField(required=True, unique=True)
  firstName = me.StringField(required=True)
  lastName = me.StringField(required=True)
  cel = me.StringField(required=True)
