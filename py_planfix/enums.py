# -*- coding: utf-8 -*-
__author__ = u'Дмитрий'


def enum(**enums):
    return type('Enum', (), enums)


SEX = enum(
    MALE="MALE",
    FEMALE="FEMALE"
)