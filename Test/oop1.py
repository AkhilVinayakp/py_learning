from msilib import type_binary


class Vehicle:
    def __init__(self, id_, per_value, type_, cost) -> None:
        self.__vehicle_id = id_
        self.__premium_percentage = per_value
        self.__vehicle_type = type_
        self.__vehicle_cost = cost
        self.__premium_amount = None
    @property
    def vehicle_id(self):
        return self.__vehicle_id
    @vehicle_id.setter
    def vehicle_id(self, id):
        self.__vehicle_id = id
    @property
    def premium_percentage(self):
        return self.__premium_percentage
    @premium_percentage.setter
    def premium_percentage(self, amount):
        self.premium_percentage = amount
    @property
    def vehicle_cost(self):
        return self.__vehicle_cost
    @vehicle_cost.setter
    def vehicle_cost(self, cost):
        self.__vehicle_cost = cost
    def display_vehicle_details():
        pass
