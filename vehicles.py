"""
Vehicle and Speed Ticket Classes

This module contains class definitions for managing vehicles and speed tickets. The classes include:
1. `Vehicle`: Base class for all vehicles with attributes such as make, year, mileage, price, and registration number.
2. `Car`: Subclass of `Vehicle` with an additional attribute for the number of doors.
3. `Truck`: Subclass of `Vehicle` with an attribute for wheel drive (2WD/4WD).
4. `SUV`: Subclass of `Vehicle` with an attribute for passenger capacity.
5. `SpeedTicket`: Represents a speed violation with details about registration number, time of offence, speed, and speed limit.

Key Features:
- Vehicle subclasses extend the functionality of the base `Vehicle` class.
- `SpeedTicket` is used to associate speed violations with specific vehicles.
- Each class includes a `__str__` method for clean and informative string representations.

Usage:
- Import and instantiate these classes in the main program.
- Use `SpeedTicket` to record and display speed violations.
"""

class Vehicle:
    def __init__ (self,make,year,kmstand,pris,regnummer,ticket=None):
        self.make = make
        self.year = year
        self.kmstand = kmstand
        self.pris = pris
        self.regnummer = regnummer
        self.ticket = ticket
    
    def get_make (self):
        return self.make
    def get_year (self):
        return self.year
    def get_kmstand(self):
        return self.kmstand
    def get_pris(self):
        return self.pris
    def get_regnummer(self):
        return self.regnummer
    
    
    def find_make(self, stored_make):
        return self.make.lower() == stored_make.lower()
    

    def __str__(self) -> str:
        return f'Vehicle: {self.make},{self.year},{self.kmstand},{self.pris},{self.regnummer},tickets: {self.ticket}'
    

    
class Car(Vehicle):
    def __init__ (self,make,year,kmstand,pris,regnummer,doors,ticket=None):
        super().__init__(make,year,kmstand,pris,regnummer,ticket)
        self.doors = doors

    def get_doors(self):
        return self.doors
    
    def __str__(self) -> str:
        return super().__str__() + f', {self.doors} doors'
    

class Truck(Vehicle):
    def __init__ (self,make,year,kmstand,pris,regnummer,WD=2,ticket=None):
        super().__init__(make,year,kmstand,pris,regnummer,ticket)
        self.WD = WD

    def get_WD(self):
        return self.WD
    
    def __str__(self) -> str:
        return super().__str__() + f', {self.WD} WD'
    

class SUV (Vehicle):
    def __init__ (self,make,year,kmstand,pris,regnummer,passengers,ticket=None):
        super().__init__(make,year,kmstand,pris,regnummer,ticket)
        self.passengers = passengers

    def get_passengers(self):
        return self.passengers
    
    def __str__(self) -> str:
        return super().__str__() + f', {self.passengers} passengers'
    

class SpeedTicket:
    def __init__ (self,regnummer, offence_time, speed, speed_limit):
        self.regnummer = regnummer
        self.offence_time = offence_time
        self.speed = speed
        self.speed_limit = speed_limit
    
    def list_tickets (self):
        return [self.offence_time, self.speed, self.speed_limit]

    def get_offence_time(self):
        return self.offence_time
    def get_speed(self):
        return self.speed 
    def get_speed_limit(self):
        return self.speed_limit
    
    def __str__(self):
        return f"{self.regnummer}, {self.offence_time}, {self.speed}, {self.speed_limit}"
    


