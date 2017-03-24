# -*- coding: utf-8 -*-
__author__ = u'zloiia'

import requests
from requests.auth import HTTPBasicAuth
import hashlib
import dict2xml
import xmltodict


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
    def __fieldsignature__(root):
        """Склеивает поля запроса для расчета сигнатуры
        :param root: запрос
        :return:
        """
        result = ''
        if isinstance(root, dict):
            for k in sorted(root):
                #result += str(root[k])
                result += Planfix.__fieldsignature__(root[k])
        elif isinstance(root, list):
            result += ''.join([str(i) for i in sorted(root)])
        else:
            result += str(root)
        return result


    @staticmethod
    def __checkResponce__(r):
        if r['response']['@status']!= "ok":
            pass
        return r['response']

    def _signature_(self, function, query):
        """Расчет подписи для запроса
        :param function:
        :param query:
        :return:
        """
        assert (function is not None)
        assert (query is not None)
        assert (self.__SIGN_KEY__ is not None)
        md5_hash = hashlib.md5()
        md5_hash.update(function + Planfix.__fieldsignature__(query) + self.__SIGN_KEY__)
        return md5_hash.hexdigest()

    def auth(self, login, password):
        """Авторизация на сервисе
        :param login: пользователь
        :param password: пароль
        :return:
        """
        assert (self.__ACCOUNT__ is not None)
        assert (login is not None)
        assert (password is not None)
        method = "auth.login"
        request = {
            "account": self.__ACCOUNT__,
            "login": login,
            "password": password,
        }
        r = self.__send_request__(method, request)
        self.__SID__ = r["sid"]


    def __send_request__(self, method, request):
        header = {
            'Content-Type': 'application/xml'
        }
        request["signature"] = self._signature_(method, request)
        request = {
            "request": request
        }
        data = dict2xml.dict2xml(request, method).doc.toxml("utf-8")

        r = requests.post(
            PLANFIX_URL,
            auth=HTTPBasicAuth(self.__API_KEY__,""),
            headers = header,
            data=data
        )
        r.raise_for_status()
        return Planfix.__checkResponce__(xmltodict.parse(r.text))