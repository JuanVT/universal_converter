from django.db import models


class Converter(models.Model):
    unit_choices = [("metre", "Metre"),
                    ("kilometre", "Kilometre"),
                    ("centimetre", "Centimetre"),
                    ("millimetre", "Millimetre"),
                    ("micrometre", "Micrometre"),
                    ("nanometre", "Nanometre"),
                    ("mile", "Mile"),
                    ("yard", "Yard"),
                    ("foot", "Foot"),
                    ("inch", "Inch")]

    unit = models.CharField(null=True, blank=True, max_length=15, choices=unit_choices)

    unit_to = models.CharField(null=True, blank=True, max_length=15, choices=unit_choices)

    unit_value = models.FloatField(null=True, blank=True)

    def unit_converter(self):
        metre_values = {
            'kilometre': 1000.0,
            'metre': 1.0,
            'centimetre': 0.01,
            'millimetre': 0.001,
            'micrometre': 10 ** -6.0,
            'nanometre': 10 ** -9.0,
            'mile': 1609.34,
            'yard': 0.9144,
            'foot': 0.3048,
            'inch': 0.0254,
        }

        result = self.unit_value * metre_values[self.unit] / metre_values[self.unit_to]
        return result
