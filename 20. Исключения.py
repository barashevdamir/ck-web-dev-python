# 20. Исключения
# Напишем часть сервиса, который будет помогать бронировать переговорки в офисе.
# Для этого опишем класс Booking - его объекты будут содержать информацию о конкретном бронировании,
# а также вспомогательную функцию create_booking,
# которая будет создавать новый объект бронирования и записывать информацию о бронировании в базу данных бронирований через предоставляемое API.
# Возвращать она должна будет статус создания бронирования (получилось или переговорка уже занята) и информацию о брони в формате JSON.
# Ниже - подробности.
#
# Класс Booking должен обладать следующим функционалом.
#
# конструктор должен принимать три аргумента в следующем порядке: название переговорки, datetime начала брони и datetime конца брони
# внутри конструктора, если datetime конца брони оказался раньше, чем datetime начала, нужно вызвать исключение ValueError
# Также у объектов этого класса должны быть следующие поля (рекомендую сделать часть из них в виде проперти):
#
# room_name
# название переговорки, полученное из конструктора
# start
# datetime начала брони. Должна быть возможность назначить новое время начала уже созданной брони
# end
# datetime конца брони. Должна быть возможность назначить новое время конца уже созданной брони
# duration
# длительность бронирования в минутах (гарантируется, что длительность любой встречи кратна одной минуте, поэтому это должно быть целое число)
# start_date
# дата начала брони в формате YYYY-MM-DD (строка)
# end_date
# дата конца брони в формате YYYY-MM-DD (строка)
# start_time
# время начала брони в формате HH-MM (строка)
# end_time
# время конца брони в формате HH-MM (строка)
# Функция create_booking должна обладать следующей сигнатурой:
#
# create_booking(room_name, start, end) -> str,
#
# где аргументы - это те же аргументы, которые принимает конструктор Booking, а выходная строка - это json определенного формата,
# который описан чуть ниже по тексту.
#
# Будем считать, что взаимодействие с базой данных у нас уже описано нашим коллегой в соседнем файле api.py.
# В нем есть уже готовая функция register_booking, которая:
#
# принимает на вход объект класса Booking
# возвращает True, если бронирование получилось создать
# возвращает False, если мы пытаемся забронировать уже занятую в это время переговорку
# если такой переговорки не существует, вызывается KeyError
# Таким образом, в том же файле, что и класс Booking, вам нужно описать фукнцию create_booking, которая:
#
# обладает сигнатурой create_booking(room_name, start, end) -> str, где аргументы - те же, что и в конструкторе Booking
# в самом начале своей работы выводит на экран текст: Начинаем создание бронирования
# внутри функции создается объект класса Booking, а также вызывается функция register_booking, которая принимает на вход созданный объект.
# Должны быть обработаны все случаи работы register_booking: True, False и KeyError. Сделать это поможет конструкция try-except
# перед выходом из функции должно выводиться на экран сообщение Заканчиваем создание бронирования.
# Это должно происходить в любом случае, даже если мы попытались создать бронирование с неверными датами и получили ValueError
# (см. описание класса Booking). Для этого рекомендую использовать блок finally, в котором описать этот print
# Функция должна возвращать json-строку с ответом, в котором будут содержаться следующие поля:
#
# created: true/false, получилось ли забронировать комнату. Если возникло KeyError, то нужно здесь записать false
# msg: сообщение с пояснениями. Сообщение должно быть одним из следующих: Бронирование создано, Комната занята, Комната не найдена.
# Сообщение выбирается на основе того, что вернет функция register_booking
# booking
# это бронирование в виде json-строки. Должны содержаться поля: room_name, duration, start_date, end_date, start_time, end_time.

import datetime
import json
from api import register_booking
class Booking:
    def __init__(self, __room_name, __start, __end):
        if __start > __end:
            raise ValueError
        self.__room_name = __room_name
        self.__start = __start
        self.__end = __end

    @property
    def room_name(self):
        return self.__room_name

    @property
    def start(self):
        return self.__start

    @start.setter
    def start(self, __value):
        self.__start = __value

    @property
    def end(self):
        return self.__end

    @end.setter
    def end(self, __value):
        self.__end = __value

    @property
    def duration(self):
        return int((self.__end - self.__start).total_seconds() // 60)

    @property
    def start_date(self):
        return self.__start.strftime("%Y-%m-%d")

    @property
    def end_date(self):
        return self.__end.strftime("%Y-%m-%d")

    @property
    def start_time(self):
        return self.__start.strftime("%H:%M")

    @property
    def end_time(self):
        return self.__end.strftime("%H:%M")
def create_booking(room_name, start, end) -> str:
    print("Начинаем создание бронирования")
    res: dict = {}
    try:
        booking = Booking(room_name, start, end)
        if register_booking(booking) == True:
            res["created"] = True
            res["msg"] = "Бронирование создано"
        else:
            res["created"] = False
            res["msg"] = "Комната занята"
    except KeyError:
        res["created"] = False
        res["msg"] = "Комната не найдена"
    finally:
        print("Заканчиваем создание бронирования")

    res["booking"] = {"room_name": booking.room_name,
                          "start_date": booking.start_date,
                          "start_time": booking.start_time,
                          "end_date": booking.end_date,
                          "end_time": booking.end_time,
                          "duration": booking.duration}
    return json.dumps(res)