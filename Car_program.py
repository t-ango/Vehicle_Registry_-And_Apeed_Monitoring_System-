"""
Vehicle Registry and Speed Monitoring System

This program allows users to manage a registry of vehicles and track speed tickets based on data from checkpoint files. It supports creating new vehicles, listing all vehicles, finding vehicles by make, and associating speed tickets with registered vehicles.

Features:
1. Create and register different types of vehicles (Cars, Trucks, SUVs).
2. Load vehicle registry from a file and save changes persistently.
3. Analyze speed data from checkpoint files to identify speed violations.
4. Display associated speed tickets for registered vehicles.

Constants:
- NEW_CAR_CHOICE: Menu option to add a new car.
- NEW_TRUCK_CHOICE: Menu option to add a new truck.
- NEW_SUV_CHOICE: Menu option to add a new SUV.
- FIND_VEHICLE_CHOICE: Menu option to find vehicles by make.
- SHOW_VEHICLES_CHOICE: Menu option to show all registered vehicles.
- SHOW_SPEED_TICKET: Menu option to display speed tickets.
- QUIT_CHOICE: Menu option to exit the program.

Dependencies:
- `vehicles` module for class definitions.
- Data files (`box_a.txt`, `box_b.txt`) for speed data.
- `vehicle_registry.txt` for storing vehicle data persistently.

Usage:
1. Run the program.
2. Interact with the menu to manage the vehicle registry and speed tickets.
Note: for options 4,5 and 7 fill the registry with cars from speed cameras files first. 
Option 7 shows tickets only if speeders are registered. 
"""

import vehicles


import os
import pickle 
import time 
from datetime import datetime

def fileToDictionary (filename):
    new_dict = {}
    if os.path.isfile(filename):
        with open (filename, "r") as inputfile:
            try: 
                for line in inputfile:
                    line = line.rstrip()
                    if "," in line:
                        registration_number, date = line.split(",",1)
                        new_dict[registration_number.strip()] = date.strip()
            except Exception as e:
                print (f"Error loading file: {e}")
    else: 
        print("File not found")
    return new_dict

def listSpeeders (filename_a, filename_b, speed_limit=60, distance=5):
    dict_a = fileToDictionary(filename_a)
    dict_b = fileToDictionary(filename_b)
    get_fine = speed_limit * 1.05  
    list_of_speeders = {}

    for key in dict_a:
        if key in dict_b:
            start_time = datetime.fromisoformat(dict_a[key])
            end_time = datetime.fromisoformat(dict_b[key])
            driving_time = abs(start_time - end_time)
            driving_secongs = driving_time.total_seconds()
            avg_speed = round(( distance / (driving_secongs/3600)),3)
            if avg_speed > get_fine:
                list_of_speeders[key] = (avg_speed, dict_b[key])
    return list_of_speeders


# Constants for the menu choices
NEW_CAR_CHOICE = 1
NEW_TRUCK_CHOICE = 2
NEW_SUV_CHOICE = 3
FIND_VEHICLE_CHOICE = 4
SHOW_VEHICLES_CHOICE = 5
SHOW_SPEED_TICKET = 7
QUIT_CHOICE = 6

def main():
    import pickle
    import os.path

    speed_limit = 60
    dict_speeders = listSpeeders("box_a.txt","box_b.txt",speed_limit,5)

# Create empty list for vehicles
    vehicles_list = []  
    if not os.path.isfile("vehicle_registry.txt"):
        return []
    else:
        with open ("vehicle_registry.txt", "rb") as inputfile:
            try: vehicles_list = pickle.load(inputfile)
            except EOFError:
                print ("File contains NO data")
            pass

    
# Create a Car object for a used 2001 BMW
# with 70,000 miles, priced at $15,000, with
# 4 doors.
    car = vehicles.Car('BMW 320', 2001, 70000, 15000.0, 'NB72826', 4)
    if car not in vehicles_list:
        vehicles_list.append(car)
# Create a Truck object for a used 2002
# Toyota pickup with 40,000 miles, priced
# at $12,000, with 4-wheel drive.
    truck = vehicles.Truck('Toyota RAV4', 2002, 40000, 12000.0, 'ZH85499',4)
    if truck not in vehicles_list:
        vehicles_list.append(truck)
# Create an SUV object for a used 2000
# Volvo with 30,000 miles, priced
# at $18,500, with 5 passenger capacity.
    suv = vehicles.SUV('Volvo XC60', 2010, 30000, 18500.0, 'DA49644', 5)
    if suv not in vehicles_list:
        vehicles_list.append(suv)
    choice = 0

    while choice != QUIT_CHOICE:
# display the menu.
        display_menu()
        choice = int(input('Enter your choice: '))
        # Perform the selected action.
        if choice == NEW_CAR_CHOICE:
            print('Add a new car')
            print ('Input car data:')
            make = input("Make: ")
            year = input("Year: ")
            milage = input("Milage: ")
            price = input("Price: ")
            regnumber = input("License plate number: ")
            doors = input("Doors: ")

            new_car = vehicles.Car(make, year, milage, price, regnumber, doors)
            vehicles_list.append(new_car)

            with open ("vehicle_registry.txt", 'ab') as outputfile:
                pickle.dump(vehicles_list, outputfile)


        elif choice == NEW_TRUCK_CHOICE:
            print('Add a new truck')
            print ('Input vehicle data:')
            make = input("Make: ")
            year = input("Year: ")
            milage = input("Milage: ")
            price = input("Price: ")
            regnumber = input("License plate number: ")
            wd = input("WD(2 or 4): ")
            new_truck = vehicles.Truck(make, year, milage, price, regnumber, wd)        

            vehicles_list.append(new_truck)

            with open ("vehicle_registry.txt", 'ab') as outputfile:
                pickle.dump(vehicles_list, outputfile)

        elif choice == NEW_SUV_CHOICE:
            print('Add a new SUV')
            print ('Input car data:')
            make = input("Make: ")
            year = input("Year: ")
            milage = input("Milage: ")
            price = input("Price: ")
            regnumber = input("License plate number: ")
            passengers = input("Passengers: ")

            new_suv = vehicles.SUV(make, year, milage, price, regnumber, passengers)
            vehicles_list.append(new_suv)

            with open ("vehicle_registry.txt", 'ab') as outputfile:
                pickle.dump(vehicles_list, outputfile)

        elif choice == FIND_VEHICLE_CHOICE:
            print('Find vehicle by name')
            find_name = input('Enter name: ')
            
            unique_makes = set()
            found_vehicle = False

            for vehicle in vehicles_list:
                if vehicle.find_make(find_name):
                    if vehicle.make not in unique_makes:
                        print(vehicle)
                        unique_makes.add(vehicle.make)
                        found_vehicle = True
            if not found_vehicle:
                print('No vehicle found')


        elif choice == SHOW_VEHICLES_CHOICE:
        #show all vehicles
            print('The following cars are in inventory:')
            for item in vehicles_list:
                print(item)

        elif choice == SHOW_SPEED_TICKET:
            print ("Find speed tickets by license plate number: ")
            find_ticket = input("Enter license plate number: ")
            
            # Check if the ticket is in dict_speeders and add it to speed_tickets
            if find_ticket.upper() in dict_speeders:
                regnr = find_ticket.upper()
                speed, time_of_passage = dict_speeders[regnr]
                ticket = vehicles.SpeedTicket(regnr, speed, time_of_passage.strip(),speed_limit)

                for vehicle in vehicles_list:
                    if vehicle.regnummer == regnr:
                        # Associate the existing SpeedTicket with the vehicle
                        vehicle.ticket = vehicles.SpeedTicket(regnummer=regnr, offence_time=time_of_passage.strip(),speed=speed, speed_limit=speed_limit)                           
                        print(f"Speed ticket associated with {vehicle}")
                        break
            else: 
                print ("No speed ticket found")       


        elif choice == QUIT_CHOICE:
            print('Exiting the program...')
        else:
            print('Error: invalid selection.')

    with open ("vehicle_registry.txt", 'ab') as outputfile:
        pickle.dump(vehicles_list, outputfile)
    


# The display_menu function displays a menu.
def display_menu():
    print(' MENU')
    print('1) New car')
    print('2) New truck')
    print('3) New SUV')
    print('4) Find vehicles by make')
    print('5) Show all vehicles')
    print('7) Show speed tickets')
    print('6) Quit')

# Call the main function.
if __name__ == '__main__':
    main()

