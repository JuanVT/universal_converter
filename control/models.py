from django.db import models

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


class Converter(models.Model):

    unit = models.CharField(null=True, blank=True, max_length=15, choices=unit_choices)

    unit_to = models.CharField(null=True, blank=True, max_length=15, choices=unit_choices)

    unit_value = models.FloatField(null=True, blank=True)
