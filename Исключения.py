import datetime
import json
#from api import register_booking
class Booking:
    def __init__(self, room_name, startDate, endDate):
        if (endDate < startDate):
            raise ValueError
        else:
            self.room_name = room_name
            self.start_date = datetime.datetime.date(startDate).strftime("%Y-%m-%d")
            self.start_time = datetime.datetime.time(startDate).strftime("%H:%M")
            self.end_date = datetime.datetime.date(startDate).strftime("%Y-%m-%d")
            self.end_time = datetime.datetime.time(endDate).strftime("%H:%M")
            self.duration = int((datetime.datetime.strptime(self.end_time, "%H:%M") - datetime.datetime.strptime(self.start_time, "%H:%M")).total_seconds() / 60)
    @property
    def start(self):
        return self.start_date
    @start.setter
    def start(self, value):
        value = datetime.datetime.time(value).strftime("%H:%M")
        if value < self.end_time:
            self.start_time = value
            self.duration = int((datetime.datetime.strptime(self.end_time, "%H:%M") - datetime.datetime.strptime(self.start_time, "%H:%M")).total_seconds() / 60)
        else:
            raise ValueError
    @property
    def end(self):
        return self.end_date
    @end.setter
    def end(self, value):
        value = datetime.datetime.time(value).strftime("%H:%M")
        if value > self.start_time:
            self.end_time = value
            self.duration = int((datetime.datetime.strptime(self.end_time, "%H:%M") - datetime.datetime.strptime(self.start_time, "%H:%M")).total_seconds() / 60)
        else:
            raise ValueError
def create_booking(room_name, start, end):
    booking = Booking(room_name, start, end)
    try:
        print("Начинаем создание бронирования")
        #result = register_booking(booking)
        result = False
        #assert booking.duration == 2 * 60 + 5
    except KeyError:
        msg = 'Комната не найдена'
    else:
        if result == True:
            msg = 'Бронирование создано'
        if result == False:
            msg = 'Комната занята'
    finally:
        print("Заканчиваем создание бронирования")
        return json.dumps({"created": result, "msg": msg, "booking": booking.__dict__}, ensure_ascii=False)

result = create_booking(
    "Вагнер",
    datetime.datetime(2022, 9, 1, 13),
    datetime.datetime(2022, 9, 1, 15, 5)
)

print(result)
