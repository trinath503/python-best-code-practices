from abc import ABC, abstractmethod

"""
 ------------------
| SOLID principles |
 ------------------
Single Responsibility Principle (SRP): Each class has a single responsibility, such as calculating parking fees for vehicle types, managing the parking lot, or representing vehicle objects.
Open/Closed Principle (OCP): The code is open for extension (new vehicle types) but closed for modification. Adding a new vehicle type involves creating a new class that inherits from the Vehicle abstract base class.
Liskov Substitution Principle (LSP): The TwoWheeler and FourWheeler classes are subclasses of the Vehicle base class and can be used interchangeably where Vehicle is expected.
Interface Segregation Principle (ISP): The Vehicle class defines the calculate_parking_fee method, which is implemented by each concrete vehicle type. This avoids imposing unnecessary methods on subclasses.
Dependency Inversion Principle (DIP): The ParkingLot class depends on the abstraction (Vehicle) rather than specific implementations (TwoWheeler or FourWheeler). This promotes flexibility and allows for easy substitution of different vehicle types.

"""
from abc import ABC, abstractmethod
from datetime import datetime, timedelta


class Vehicle(ABC):
    def __init__(self, license_plate):
        self.license_plate = license_plate
        self.entry_time = datetime.now()

    def calculate_parking_fee(self):
        exit_time = datetime.now()
        duration = exit_time - self.entry_time
        total_hours = int(duration.total_seconds() / 3600)
        return self._calculate_fee(total_hours)

    @abstractmethod
    def _calculate_fee(self, total_hours):
        pass


class TwoWheeler(Vehicle):
    BASE_TWO_WHEELER_PRICE = 20

    def _calculate_fee(self, total_hours):
        # Custom fee calculation logic for two-wheelers
        return self.BASE_TWO_WHEELER_PRICE + (10 * max(total_hours - 1, 0))


class FourWheeler(Vehicle):
    def _calculate_fee(self, total_hours):
        return 20 * total_hours  # Custom fee calculation logic for four-wheelers


class ParkingLot:
    def __init__(self, capacity):
        self.capacity = capacity
        self.slots = {}
        self.floors = {}
        self.users = {}

    def park(self, floor, slot, vehicle, user):
        if floor not in self.floors:
            self.floors[floor] = {}

        if slot in self.floors[floor]:
            return f"Slot {slot} on floor {floor} is already occupied"

        if not isinstance(vehicle, Vehicle):
            return f"Invalid vehicle"

        self.floors[floor][slot] = vehicle
        if user not in self.users:
            self.users[user] = set()
        self.users[user].add(vehicle.license_plate)
        return f"Vehicle {vehicle.license_plate} parked on floor {floor}, slot {slot}"

    def remove(self, floor, slot, user):
        if floor in self.floors and slot in self.floors[floor]:
            vehicle = self.floors[floor].pop(slot)
            self.users[user].remove(vehicle.license_plate)
            return f"Vehicle {vehicle.license_plate} removed from floor {floor}, slot {slot}"
        else:
            return f"No vehicle found in floor {floor}, slot {slot}"

    def status(self):
        print("Floor\tSlot No.\tVehicle")
        for floor, slots in self.floors.items():
            for slot, vehicle in slots.items():
                print(f"{floor}\t{slot}\t\t{vehicle.license_plate}")

    def get_user_vehicles(self, user):
        if user in self.users:
            return self.users[user]
        else:
            return set()


# Example usage:
parking_lot = ParkingLot(10)

two_wheeler = TwoWheeler("ABC123")
four_wheeler = FourWheeler("XYZ789")

print(parking_lot.park(1, 1, two_wheeler, "User1"))  # Park a two-wheeler on floor 1, slot 1
print(parking_lot.park(1, 2, four_wheeler, "User1"))  # Park a four-wheeler on floor 1, slot 2
print(parking_lot.status())  # Check the status of the parking lot

print(parking_lot.remove(1, 2, "User1"))  # Remove a vehicle from floor 1, slot 2
print(parking_lot.status())  # Check the status again

user1_vehicles = parking_lot.get_user_vehicles("User1")
print(f"User1 vehicles: {user1_vehicles}")

# Calculate parking fee
fee1 = two_wheeler.calculate_parking_fee()
fee2 = four_wheeler.calculate_parking_fee()
print(f"Parking fee for two-wheeler: {fee1}")
print(f"Parking fee for four-wheeler: {fee2}")
