# -*- coding: utf-8 -*-
__author__ = u'Дмитрий'


def enum(**enums):
    return type('Enum', (), enums)


SEX = enum(
    MALE="MALE",
    FEMALE="FEMALE"
)

TASK_STATES = enum(
    DRAFT="DRAFT", #Черновик
    ACTIVE="ACTIVE", #Активный но еще не принятый
    ACCEPTED="ACCEPTED", #Принятый / В работу
    COMPLETED="COMPLETED", #Завершенный
    DELAYED="DELAYED", #Отложенный
    REJECTED="REJECTED", #Отклоненный
    DONE="DONE", #Выполненный
    CANCELED="CANCELED" #Отмененный
)