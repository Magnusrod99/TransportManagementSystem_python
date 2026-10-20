# Author: Magnus
# RollNo: 2628

from abc import ABC, abstractmethod


class Transport(ABC):
    def __init__(self, transport_type: str):
        self.transport_type = transport_type

    def display_transport_type(self) -> None:
        print(f"Transport Type: {self.transport_type}")

    @abstractmethod
    def start_journey(self) -> None:
        """Start the journey for a specific transport."""
        raise NotImplementedError
