# Author: Magnus
# RollNo: 2628


class TransportMode:
    def __init__(self, mode_id: int, mode_name: str):
        self.__mode_id = mode_id
        self.__mode_name = mode_name

    def display_mode(self) -> None:
        print(f"Mode id : {self.__mode_id}")
        print(f"Mode name : {self.__mode_name}")
