# -*- coding: utf-8 -*-
__author__ = u'zloiia'

import requests
from requests.auth import HTTPBasicAuth
import hashlib
import dict2xml
import xmltodict
import schemas

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
        if self.__SID__ is not None:
            request['sid'] = self.__SID__
            request['account'] = self.__ACCOUNT__
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

    def contacts_add(self, contact):
        """Добавление контакта
        :param contact:
        :return:
        """
        assert (isinstance(contact, dict))
        assert (self.__SID__ is not None)
        method = "contact.add"
        contact = {
            "contact": contact
        }
        return self.__send_request__(method, contact)

    def contact_update(self, contact):
        """Обновление контакта
        :param contact: словарь с данными контакта
        :return: 
        """
        assert (contact is not None)
        assert (isinstance(contact, dict))
        assert "id" in contact.keys() or "general" in contact.keys(), (u'"Id" or "general" must be set')
        method = "contact.update"
        contact = {
            "contact": contact
        }
        return self.__send_request__(method, contact)

    def contact_get(self, contact):
        """Получение данных о контакте
        :param contact: словарь с данными контакта
        :return: 
        """
        assert (contact is not None)
        assert (isinstance(contact, dict))
        assert "id" in contact.keys() or "general" in contact.keys(), (u'"Id" or "general" must be set')
        method = "contact.get"
        contact = {
            "contact": contact
        }
        return self.__send_request__(method, contact)

    def contact_getlist(self, request):
        """Получение спистка контактов
        :param request: 
        :return: 
        """
        assert (request is not None)
        assert (isinstance(request, dict))
        assert "target" in request.keys() or "search" in request.keys(), (u'"target" or "search" must be set')
        method = "contact.getList"
        return self.__send_request__(method, request)

    def contact_manageplanfixaccess(self, request):
        """Функция позволяет разрешить или запретить доступ для контакта. Выполнение этой функции требует наличие админ прав.
        :param request: 
        :return: 
        """
        assert (request is not None)
        assert (isinstance(request, dict))
        assert "id" in request.keys() and "havePlanfixAccess" in request.keys(), (u'"id" and "havePlanfixAccess" must be setted')
        method = "contact.managePlanfixAccess"
        request = {
            "contact": request
        }
        return self.__send_request__(method, request)

    def contact_updateContractors(self, request):
        """Функция изменение информации о принадлежности контакта к фирме/контрагенту
        :param request: 
        :return: 
        """
        method="contact.updateContractors"
        assert (request is not None)
        assert (isinstance(request, dict))
        method="contact.updateContractors"
        request = {
            "contact": request
        }
        return self.__send_request__(method, request)

    def contact_delete(self, request):
        """Функция позволяет удалить контакт. Выполнение этой функции требует наличие соответствующих прав
        :param request: 
        :return: 
        """
        assert (request is not None)
        assert (isinstance(request, dict))
        assert "id" in request.keys(), (u'"id" must be setted')
        method = "contact.delete"
        request = {
            "contact": request
        }
        return self.__send_request__(method, request)

