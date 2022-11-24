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

result = create_booking(
    "Вагнер",
    datetime.datetime(2022, 9, 1, 13),
    datetime.datetime(2022, 9, 1, 15, 5)
)

print(result)
