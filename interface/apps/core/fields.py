from django.db.models import *


class ArrowField(FloatField):
    """
    This is basically a FloatField, with its own form widget
    """
    def formfield(self, **kwargs):
        # This is a fairly standard way to set up some defaults
        # while letting the caller override them.
        defaults = {'form_class': ArrowField}
        defaults.update(kwargs)
        return super(ArrowField, self).formfield(**defaults)


class LineField(TextField):
    """
    Stores either one or two string keys and a float point value
    """
    __metaclass__ = SubfieldBase

    def __init__(self, *args, **kwargs):
        self.token = kwargs.pop('token', ',')
        super(LineField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if not value:
            return
        if isinstance(value, list):
            return value
        return value.split(self.token)

    def get_db_prep_value(self, value):
        if not value:
            return
        assert(isinstance(value, list) or isinstance(value, tuple))
        return self.token.join([unicode(s) for s in value])

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)
