from email.policy import default
from django.db import models

class dict_data_field (models.BinaryField):
    def to_python(self, value) :
        from json import loads
        data = loads(super().to_python(value))
        return data
    def get_prep_value(self, value):
        from json import dumps
        return super().get_prep_value(dumps(value).encode('UTF-8'))


class cache(models.Model):
    data = dict_data_field(default={})
