import datetime
import json
#from api import register_booking

def register_booking(booking):
    pass

class Booking(dict):
    def __init__(self, room_name, start, end):
        if (end < start):
            raise ValueError
        else:
            self.room_name = room_name
            self.start = start
            self.end = end
    @property
    def duration(self):
        return int((self.end - self.start).minutes())
    def start_date(self):
        return self.start.date()
    def end_date(self):
        return self.start.date()
    def start_time(self):
        return self.start.time()
    def end_time(self):
        return self.end.time()
    def create_booking(room_name, start, end) -> str:
        booking = Booking(room_name, start, end)
        try:
            result = register_booking(booking)
        except KeyError:
            msg = "Комната не найдена"
        else:
            if result == True:
                msg = "Бронирование создано"
            if result == False:
                msg = "Комната занята"
        finally:
            print("Начинаем создание бронирования")
            print("Заканчиваем создание бронирования")
        data = []
        data.append("created: {}".format(register_booking(booking)))
        data.append("msg: {}".format(msg))
        data.append("booking: {}".format(booking))
        return json.dumps(data)










# def create_booking(room_name, start,end) -> str:
#     booking = Booking(........)
#     try:
#         result = register_booking(booking)
#     except ....:
#     ....
#     return json.dumps(......)