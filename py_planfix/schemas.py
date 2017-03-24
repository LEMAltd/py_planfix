# -*- coding: utf-8 -*-
__author__ = u'Дмитрий'

from schema import Schema, And, Use, Optional
import enums

contact_schema = Schema(
    {
        "template": And(int),
        "name": And(str),
        Optional("lastName"): And(str),
        Optional("lastName"): And(str),
        Optional("lastName"): And(str, Use(str.lower)),
    }
)

schema = Schema(
    [
        {
            'name': And(str, len),
            'age':  And(Use(int), lambda n: 18 <= n <= 99),
            Optional('sex'): And(str, Use(str.lower), lambda s: s in ('male', 'female'))
        }
    ]
)