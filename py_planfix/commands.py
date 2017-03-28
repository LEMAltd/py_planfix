# -*- coding: utf-8 -*-
__author__ = u'zloiia'


def check_authorization(f):
    def wrapper(*args, **kwargs):
        assert args[0].__base__.__SID__ is not None, (u'Need auth')
        return f(*args, **kwargs)
    return wrapper


class BaseCommand(object):
    def __init__(self, base):
        assert (base is not None)
        self.__base__ = base

    def _sendrequest(self, *args, **kwargs):
        return self.__base__.__send_request__(*args, **kwargs)


class ContactCommand(BaseCommand):
    def __init__(self, *args, **kwargs):
        super(ContactCommand, self).__init__(*args, **kwargs)

    @check_authorization
    def add(self, contact):
        """Добавление контакта
        :param contact:
        :return:
        """
        assert (isinstance(contact, dict))
        method = "contact.add"
        contact = {
            "contact": contact
        }
        return super(ContactCommand, self)._sendrequest(method, contact)


    @check_authorization
    def update(self, contact):
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
        return super(ContactCommand, self)._sendrequest(method, contact)

    @check_authorization
    def get(self, contact):
        """Получение данных о контакте
        :param contact: словарь с данными контакта
        :return: 
        """
        assert (self.__base__.__SID__ is not None)
        assert (contact is not None)
        assert (isinstance(contact, dict))
        assert "id" in contact.keys() or "general" in contact.keys(), (u'"Id" or "general" must be set')
        method = "contact.get"
        contact = {
            "contact": contact
        }
        return super(ContactCommand, self)._sendrequest(method, contact)

    @check_authorization
    def getlist(self, request):
        """Получение спистка контактов
        :param request: 
        :return: 
        """
        assert (request is not None)
        assert (isinstance(request, dict))
        assert "target" in request.keys() or "search" in request.keys(), (u'"target" or "search" must be set')
        method = "contact.getList"
        return super(ContactCommand, self)._sendrequest(method, request)

    @check_authorization
    def manageplanfixaccess(self, request):
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
        return super(ContactCommand, self)._sendrequest(method, request)

    @check_authorization
    def updateContractors(self, request):
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
        return super(ContactCommand, self)._sendrequest(method, request)

    @check_authorization
    def delete(self, request):
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
        return super(ContactCommand, self)._sendrequest(method, request)


class ProjectCommand(BaseCommand):
    def __init__(self, *args, **kwargs):
        super(ProjectCommand, self).__init__(*args, **kwargs)

    @check_authorization
    def add(self, request):
        """Запрос на создание проекта
        :param request: 
        :return: 
        """
        assert (request is not None)
        assert (isinstance(request, dict))
        method = "project.add"
        request = {
            "project": request
        }
        return super(ProjectCommand, self)._sendrequest(method, request)

    @check_authorization
    def update(self, request):
        """Обновление данных о проектк
        :param request: 
        :return: 
        """
        assert (request is not None)
        assert (isinstance(request, dict))
        method = "project.update"
        request = {
            "project": request
        }
        return super(ProjectCommand, self)._sendrequest(method, request)

    @check_authorization
    def get(self, request):
        """Функция позволяет получить информацию о проекте
        :param request: 
        :return: 
        """
        assert (request is not None)
        assert (isinstance(request, dict))
        assert "id" in request.keys(), (u'"id" must be setted')
        method = "project.update"
        request = {
            "project": request
        }
        return super(ProjectCommand, self)._sendrequest(method, request)

    @check_authorization
    def getlist(self, request):
        """Функция для получения списка проектов
        :param request: 
        :return: 
        """
        assert (request is not None)
        assert (isinstance(request, dict))
        assert "client" in request.keys(), (u'"Client" must be setted')
        method = "project.getList"
        return super(ProjectCommand, self)._sendrequest(method, request)


class ProjectGroups(BaseCommand):
    def __init__(self, *args, **kwargs):
        super(ProjectGroups, self).__init__(*args, **kwargs)

    @check_authorization
    def add(self, request):
        """Запрос на создание группы проектов
        :param request: 
        :return: 
        """
        assert (request is not None)
        assert (isinstance(request, dict))
        assert "name" in request.keys(), (u'"name" must be setted')
        method="projectGroup.add"
        request = {
            "projectGroup": request
        }
        return super(ProjectGroups, self)._sendrequest(method, request)

    @check_authorization
    def update(self, request):
        """Функция обновления данных о группе проектов
        :param request: 
        :return: 
        """
        assert (request is not None)
        assert (isinstance(request, dict))
        assert "name" in request.keys() and "id" in request.keys(), (u'"name" and "id" must be setted')
        method = "projectGroup.update"
        request = {
            "projectGroup": request
        }
        return super(ProjectGroups, self)._sendrequest(method, request)

    @check_authorization
    def move(self, request):
        """Функция перемещения группы проектов в списке
        https://planfix.ru/docs/%D0%9F%D0%BB%D0%B0%D0%BD%D0%A4%D0%B8%D0%BA%D1%81_API_projectGroup.move
        :param request: 
        :return: 
        """
        assert (request is not None)
        assert (isinstance(request, dict))
        method="projectGroup.move"
        return super(ProjectGroups, self)._sendrequest(method, request)

    @check_authorization
    def get(self, request):
        """Функция позволяет получить информацию о группе проектов
        https://planfix.ru/docs/%D0%9F%D0%BB%D0%B0%D0%BD%D0%A4%D0%B8%D0%BA%D1%81_API_projectGroup.get
        :param request: 
        :return: 
        """
        assert (request is not None)
        assert (isinstance(request, dict))
        assert "id" in request.keys(), (u'"id" must be setted')
        method = "projectGroup.get"
        return super(ProjectGroups, self)._sendrequest(method, request)

    @check_authorization
    def getlist(self):
        """Функция для получения списка групп проектов
        https://planfix.ru/docs/%D0%9F%D0%BB%D0%B0%D0%BD%D0%A4%D0%B8%D0%BA%D1%81_API_projectGroup.getList
        :param request: 
        :return: 
        """
        method = "projectGroup.get"
        return super(ProjectGroups, self)._sendrequest(method, {})


class Task(BaseCommand):
    def __init__(self, *args, **kwargs):
        super(Task, self).__init__(*args, **kwargs)

    @check_authorization
    def add(self, request):
        """Функция позволяет создать новую задачу
        https://planfix.ru/docs/%D0%9F%D0%BB%D0%B0%D0%BD%D0%A4%D0%B8%D0%BA%D1%81_API_task.add
        :param request: 
        :return: 
        """
        assert (request is not None)
        assert (isinstance(request, dict))
        method = "task.add"
        request = {
            "task":request
        }
        return super(Task, self)._sendrequest(method, request)

    @check_authorization
    def update(self, request):
        """Функция обновления информации задачи
        https://planfix.ru/docs/%D0%9F%D0%BB%D0%B0%D0%BD%D0%A4%D0%B8%D0%BA%D1%81_API_task.update
        :param request: 
        :return: 
        """
        assert (request is not None)
        assert (isinstance(request, dict))
        method="task.update"
        request = {
            "task": request
        }
        return super(Task, self)._sendrequest(method, request)

    @check_authorization
    def get(self, request):
        """Функция получения карточки задачи
        https://planfix.ru/docs/%D0%9F%D0%BB%D0%B0%D0%BD%D0%A4%D0%B8%D0%BA%D1%81_API_task.get
        :param request: 
        :return: 
        """
        assert (request is not None)
        assert (isinstance(request, dict))
        assert "id" in request.keys() or "general" in request.keys(), (u'"id" or "general" must be setted')
        method = "task.get"
        request = {
            "task": request
        }
        return super(Task, self)._sendrequest(method, request)

    @check_authorization
    def getmulti(self, request):
        """Функция получения множества карточек задачи
        https://planfix.ru/docs/%D0%9F%D0%BB%D0%B0%D0%BD%D0%A4%D0%B8%D0%BA%D1%81_API_task.getMulti
        :param request: 
        :return: 
        """
        assert (request is not None)
        assert (isinstance(request, dict))
        method="task.getMulti"
        request = {
            "tasks": request
        }
        return super(Task, self)._sendrequest(method, request)

    @check_authorization
    def getlist(self, request):
        """Функция получения списка задач. В зависимости от значений параметров, можно получить список задач упорядоченных по разным признакам
        https://planfix.ru/docs/%D0%9F%D0%BB%D0%B0%D0%BD%D0%A4%D0%B8%D0%BA%D1%81_API_task.getList
        :param request: 
        :return: 
        """
        assert (request is not None)
        assert (isinstance(request, dict))
        method = "task.getList"
        return super(Task, self)._sendrequest(method, request)

    @check_authorization
    def accept(self, request):
        """Для дальнейшей работы с задачей, пользователь должен принять задачу
        https://planfix.ru/docs/%D0%9F%D0%BB%D0%B0%D0%BD%D0%A4%D0%B8%D0%BA%D1%81_API_task.accept
        :param request: 
        :return: 
        """
        assert (request is not None)
        assert (isinstance(request, dict))
        assert "id" in request.keys() or "general" in request.keys(), (u'"id" or "general" must be setted')
        method = "task.accept"
        request = {
            "task": request
        }
        return super(Task, self)._sendrequest(method, request)

    @check_authorization
    def reject(self, request):
        """Для отклонения задачи, необходимо вызвать следующую функцию
        https://planfix.ru/docs/%D0%9F%D0%BB%D0%B0%D0%BD%D0%A4%D0%B8%D0%BA%D1%81_API_task.reject
        :param request: 
        :return: 
        """
        assert (request is not None)
        assert (isinstance(request, dict))
        assert "id" in request.keys() and "reason" in request.keys(), (u'"id" and "reason" must be setted')
        method = "task.reject"
        request = {
            "task": {
                "id": request["id"]
            },
            "reason": request["reason"]
        }
        return super(Task, self)._sendrequest(method, request)

    @check_authorization
    def changeexpectdate(self, request):
        """Если пользователь по какой-то причине не может выполнить в установленный срок задачу, он может перенести время выполнения её
        https://planfix.ru/docs/%D0%9F%D0%BB%D0%B0%D0%BD%D0%A4%D0%B8%D0%BA%D1%81_API_task.changeExpectDate
        :param request: 
        :return: 
        """
        assert (request is not None)
        assert (isinstance(request, dict))
        assert "id" in request.keys() and "expectDate" in request.keys(), (u'"id" and "expectDate" must be setted')
        method = "task.changeExpectDate"
        request = {
            "task": {
                "id": request["id"]
            },
            "expectDate": request["expectDate"]
        }
        return super(Task, self)._sendrequest(method, request)

    @check_authorization
    def changestatus(self, request):
        """Изменение статуса задачи
        https://planfix.ru/docs/%D0%9F%D0%BB%D0%B0%D0%BD%D0%A4%D0%B8%D0%BA%D1%81_API_task.changeStatus
        :param request: 
        :return: 
        """
        assert (request is not None)
        assert (isinstance(request, dict))
        assert "id" in request.keys() and "status" in request.keys() and "dateTime" in request.keys(), (u'"id" and "status" and "dateTime" must be setted')
        method = "task.changeStatus"
        request = {
            "task": {
                "id": request["id"]
            },
            "status": request["status"],
            "dateTime": request["dateTime"]
        }
        return super(Task, self)._sendrequest(method, request)

    @check_authorization
    def getpossiblestatustochange(self, id):
        assert (id is not None)
        method = "task.getPossibleStatusToChange"
        request = {
            "task": {
                "id": id
            }
        }
        return super(Task, self)._sendrequest(method, request)

    @check_authorization
    def changeworkers(self, request):
        """Функция используется для изменения списка исполнителей задачи
        https://planfix.ru/docs/%D0%9F%D0%BB%D0%B0%D0%BD%D0%A4%D0%B8%D0%BA%D1%81_API_task.changeWorkers
        :param request: 
        :return: 
        """
        assert (request is not None)
        assert (isinstance(request, dict))
        method = "task.changeWorkers"
        request = {
            "task": request
        }
        return super(Task, self)._sendrequest(method, request)

    @check_authorization
    def getfilterlist(self):
        """Функция позволяет получить список доступных текущему сотруднику фильтров задач для функции task.getList
        https://planfix.ru/docs/%D0%9F%D0%BB%D0%B0%D0%BD%D0%A4%D0%B8%D0%BA%D1%81_API_task.getFilterList
        :param request: 
        :return: 
        """
        method = "task.getFilterList"
        return super(Task, self)._sendrequest(method, {})