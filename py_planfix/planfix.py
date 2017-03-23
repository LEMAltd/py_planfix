# -*- coding: utf-8 -*-
__author__ = u'zloiia'

import requests
from requests.auth import HTTPBasicAuth
import xml.etree.cElementTree as ET

PLANFIX_URL = "https://api.planfix.ru/xml/"


class Planfix(object):
    __API_KEY__ = None
    __ACCOUNT__ = None
    __SID__ = None
    __SIGN_KEY__ = None

    def __init__(self, api_key = None, account=None, sign_key=None):
        """
        :param api_key: ключ API
        :param account: используемый аккаунт
        :param sign_key: ключ подписи
        """
        self.__API_KEY__ = api_key
        self.__ACCOUNT__ = account
        self.__SIGN_KEY__ = sign_key

    @staticmethod
    def __create_root__(method):
        """Создает корневой элемент
        :param method:
        :return:
        """
        assert (method is not None)
        root = ET.Element("request", method=method)
        return root

    @staticmethod
    def __fieldsignature__(root):
        """Склеивает поля документа для расчета сигнатуры
        :param root: корневой элемент
        :return:
        """
        result = ''

        for node in sorted(list(root), key=lambda x: x.tag):
            result+= node.text
            for child in sorted(list(node), key=lambda x: x.tag):
                result += Planfix.__signature__(child)
        return result

    def _signature_(self, root):
        """Рассчитываем сигнатуру элемента запроса
        :param root:
        :return:
        """
        assert ()

    def auth(self, login, password):
        """Авторизация на сервисе
        :param login: пользователь
        :param password: пароль
        :return:
        """
        assert (self.__ACCOUNT__ is not None)
        assert (login is not None)
        assert (password is not None)
        root = self.__create_root__("auth.login")
        ET.SubElement(root, "account").text = self.__ACCOUNT__
        ET.SubElement(root, "login").text = login
        ET.SubElement(root, "password").text = password


    def __get_request__(self, function, data = None):
        header = {
            'Content-Type': 'application/xml'
        }
        content = ET.Element("request")
        return requests.post(
            PLANFIX_URL,
            auth=HTTPBasicAuth(self.__API_KEY__,""),
            headers = header,
            data=data
        )