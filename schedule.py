# Author: Magnus
# RollNo: 2628


class Schedule:
    def __init__(
        self,
        schedule_id: int,
        vehicle_id: int,
        route_id: int,
        departure_time: str,
        arrival_time: str,
    ):
        self.schedule_id = schedule_id
        self.vehicle_id = vehicle_id
        self.route_id = route_id
        self.departure_time = departure_time
        self.arrival_time = arrival_time

    def display_schedule(self) -> None:
        print(" SCHEDULE DETAILS ")
        print(f"Schedule ID: {self.schedule_id}")
        print(f"Vehicle ID: {self.vehicle_id}")
        print(f"Route ID: {self.route_id}")
        print(f"Departure Time: {self.departure_time}")
        print(f"Arrival Time: {self.arrival_time}")
