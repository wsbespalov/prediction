
from data import data

k = 0.5
b = 0.9
q = 0.5

point_in_period = 12
number_of_periods_before_prediction = 4
number_of_periods_in_prediction  = 1


class Point:
    data = 0.0              # Точка данных
    Lt = 0.0                # Экспоненциально сглаженный ряд
    Tt = 0.0                # Значение тренда
    St_s = 0.0              # Сезонность
    p = 0                   # Номер периода
    prognoz_holt = 0.0      # Прогноз на основе Хольта-Винтреса
    prognoz_modeli = 0.0    # Прогнозные значения
    error = 0.0             # Ошибка модели
    otklonenie = 0.0        # Отклонение
    tochnost = 0.0          # Точность прогноза


def calculate(points):
    pass


data_points = []
for dp in data:
    one_point = Point()
    one_point.data = dp
    one_point.Lt = 0.0
    one_point.Tt = 0.0
    one_point.St_s = 0.0
    one_point.p = 0
    one_point.prognoz_holt = 0.0
    one_point.prognoz_modeli = 0.0
    one_point.error = 0.0
    one_point.otklonenie = 0.0
    one_point.tochnost = 0.0
    data_points.append(one_point)

calculate(data_points)