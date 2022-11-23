import datetime
import json
#from api import register_booking
class Booking:
    def __init__(self, room_name, startDate, endDate):
        if (endDate <= startDate):
            raise ValueError
        else:
            self.room_name = room_name
            self.start_date = datetime.datetime.strftime(startDate, "%Y-%m-%d")
            self.start_time = datetime.datetime.strftime(startDate, "%H:%M")
            self.end_date = datetime.datetime.strftime(endDate, "%Y-%m-%d")
            self.end_time = datetime.datetime.strftime(endDate, "%H:%M")
            self.duration = int((endDate - endDate).seconds // 60)
    start = property()
    @start.setter
    def start(self, value):
        value = datetime.datetime.strftime(value, "%H:%M")
        if value < self.end_time:
            self.start_time = value
            self.duration = int((datetime.datetime.strptime(self.end_time, "%H:%M") - datetime.datetime.strptime(self.start_time, "%H:%M")).seconds // 60)
        else:
            raise ValueError
    end = property()
    @end.setter
    def end(self, value):
        value = datetime.datetime.strftime(value, "%H:%M")
        if value > self.start_time:
            self.end_time = value
            self.duration = int((datetime.datetime.strptime(self.end_time, "%H:%M") - datetime.datetime.strptime(self.start_time, "%H:%M")).total_seconds / 60)
        else:
            raise ValueError
def create_booking(room_name, start, end):
    booking = Booking(room_name, start, end)
    try:
        print("Начинаем создание бронирования")
        #result = register_booking(booking)
        result = True
    except KeyError:
        msg = 'Комната не найдена'
    else:
        if result == True:
            msg = 'Бронирование создано'
        if result == False:
            msg = 'Комната занята'
    finally:
        print("Заканчиваем создание бронирования")
        my_json = json.dumps({'created': result, 'msg': msg, 'booking': booking.__dict__}, ensure_ascii=False)
        return my_json
print(create_booking(
    "Вагнер",
    datetime.datetime(2022, 9, 1, 14),
    datetime.datetime(2022, 9, 1, 15, 15)
))







# def create_booking(room_name, start,end) -> str:
#     booking = Booking(........)
#     try:
#         result = register_booking(booking)
#     except ....:
#     ....
#     return json.dumps(......)