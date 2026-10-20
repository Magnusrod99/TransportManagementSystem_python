# Author: Magnus
# RollNo: 2628

from transport import Transport


class Vehicle(Transport):
    def __init__(
        self,
        vehicle_id: int,
        vehicle_name: str,
        transport_type: str,
        vehicle_number: str,
        capacity: int,
    ):
        super().__init__(transport_type)
        self.__vehicle_id = vehicle_id
        self.__vehicle_name = vehicle_name
        self.__vehicle_number = vehicle_number
        self.__capacity = capacity

    def get_vehicle_id(self) -> int:
        return self.__vehicle_id

    def get_vehicle_name(self) -> str:
        return self.__vehicle_name

    def get_vehicle_number(self) -> str:
        return self.__vehicle_number

    def get_capacity(self) -> int:
        return self.__capacity

    def set_vehicle_name(self, vehicle_name: str) -> None:
        self.__vehicle_name = vehicle_name

    def set_vehicle_number(self, vehicle_number: str) -> None:
        self.__vehicle_number = vehicle_number

    def set_capacity(self, capacity: int) -> None:
        self.__capacity = capacity

    def start_journey(self) -> None:
        print(f"{self.__vehicle_name} will be starting its journey soon.")

    def display_vehicle(self) -> None:
        print("\n--- VEHICLE DETAILS ---")
        print(f"Vehicle ID: {self.get_vehicle_id()}")
        print(f"Vehicle Name: {self.get_vehicle_name()}")
        self.display_transport_type()
        print(f"Vehicle Number: {self.get_vehicle_number()}")
        print(f"Capacity: {self.get_capacity()}")
