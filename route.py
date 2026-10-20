# Author: Magnus
# RollNo: 2628


class Route:
    def __init__(self, route_id: int, source: str, destination: str, distance: float):
        self.route_id = route_id
        self.source = source
        self.destination = destination
        self.distance = distance

    def display_route(self) -> None:
        print(" ROUTE DETAILS ")
        print(f"Route ID: {self.route_id}")
        print(f"Source: {self.source}")
        print(f"Destination: {self.destination}")
        print(f"Distance: {self.distance:g} km")
