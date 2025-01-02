# Vehicle Registry and Speed Monitoring System

This program manages a registry of vehicles and monitors speed tickets based on checkpoint data. It combines object-oriented programming with file handling to provide a robust solution for vehicle management and speed enforcement.

## Features
1. **Vehicle Management**:
   - Add new vehicles (Cars, Trucks, SUVs) with details like make, year, mileage, price, and registration number.
   - Load and save the vehicle registry persistently using a file.

2. **Speed Monitoring**:
   - Analyze speed data from checkpoint files (`box_a.txt` and `box_b.txt`) to identify speed violations.
   - Associate speed tickets with registered vehicles for tracking.

3. **User-Friendly Interface**:
   - Interactive menu for managing vehicles and viewing speed tickets.

## Installation
1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd vehicle-registry
Ensure box_a.txt, box_b.txt, and vehicle_registry.txt are in the same directory as the program.

**Usage**

Run the program:
python Car_program.py
Use the menu to:
Add new vehicles.
Find vehicles by make.
List all registered vehicles.
Check and display speed tickets.
Example

Sample menu:

 MENU
1) New car
2) New truck
3) New SUV
4) Find vehicles by make
5) Show all vehicles
7) Show speed tickets
6) Quit
   
**Dependencies**

Python 3.x
pickle module for saving/loading registry data.

**File Descriptions**

Car_program.py: Implements the program logic and menu interface.
vehicles.py: Contains class definitions for vehicles and speed tickets.
vehicle_registry.txt: Contains registered cars.

**License**

This program is released under the MIT License.
