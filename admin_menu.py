# Author: Magnus
# RollNo: 2628

from route import Route
from schedule import Schedule
from transport_mode import TransportMode
from transport import Transport
from vehicle import Vehicle


class AdminMenu:
    @staticmethod
    def _read_int(prompt: str) -> int | None:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            return None

    @staticmethod
    def _read_float(prompt: str) -> float | None:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")
            return None

    def show_menu(self) -> None:
        choice = 0

        while choice != 6:
            print("===TRANSPORT SYSTEM=== :Admin")
            print("Menu")
            print("1. Manage Transport Modes")
            print("2. Manage Vehicles")
            print("3. Manage Routes")
            print("4. Manage Schedules")
            print("5. View Bookings")
            print("6. Exit")

            selected = self._read_int("enter your choice\n")
            if selected is None:
                continue
            choice = selected

            if choice == 1:
                print("\n--- ADD TRANSPORT MODE ---")
                mode_id = self._read_int("Enter Mode ID: ")
                if mode_id is None:
                    continue
                mode_name = input("Enter Mode Name: ")
                mode = TransportMode(mode_id, mode_name)
                print("\nTransport mode added successfully!")
                mode.display_mode()

            elif choice == 2:
                print("\n--- ADD VEHICLE ---")
                vehicle_id = self._read_int("Enter Vehicle ID: ")
                if vehicle_id is None:
                    continue
                vehicle_name = input("Enter Vehicle Name: ")
                vehicle_type = input("Enter Vehicle Type: ")
                vehicle_number = input("Enter Vehicle Number: ")
                capacity = self._read_int("Enter Vehicle Capacity: ")
                if capacity is None:
                    continue

                vehicle = Vehicle(
                    vehicle_id, vehicle_name, vehicle_type, vehicle_number, capacity
                )
                print("\nVehicle added successfully!")
                vehicle.display_vehicle()

                # Polymorphism: use the abstract base type for a derived object.
                transport: Transport = vehicle
                transport.start_journey()

            elif choice == 3:
                print("\n--- ADD ROUTE ---")
                route_id = self._read_int("Enter Route ID: ")
                if route_id is None:
                    continue
                source = input("Enter Source: ")
                destination = input("Enter Destination: ")
                distance = self._read_float("Enter Distance in km: ")
                if distance is None:
                    continue

                route = Route(route_id, source, destination, distance)
                print("\nRoute added successfully!")
                route.display_route()

            elif choice == 4:
                print(" ADD SCHEDULE ")
                schedule_id = self._read_int("Enter Schedule ID: ")
                if schedule_id is None:
                    continue
                vehicle_id = self._read_int("Enter Vehicle ID: ")
                if vehicle_id is None:
                    continue
                route_id = self._read_int("Enter Route ID: ")
                if route_id is None:
                    continue

                departure_time = input("Enter Departure Time: ")
                arrival_time = input("Enter Arrival Time: ")
                schedule = Schedule(
                    schedule_id, vehicle_id, route_id, departure_time, arrival_time
                )
                print("Schedule added successfully!")
                schedule.display_schedule()

            elif choice == 5:
                print(" opening view bookings ....")

            elif choice == 6:
                print("exiting thank you ....")

            else:
                print("error please enter the number from the given choice")

            print()
