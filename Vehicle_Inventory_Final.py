#Portfolio Project Option 1, Vehicle Inventory Program


#Create class Automobile
class Automobile:

	def __init__(self, make, model, color, year, mileage):
		self._make = make
		self._model = model
		self._color = color
		self._year = year
		self._mileage = mileage
	
	#Return the values of the object instead of the memory location.	
	def __repr__(self):
		return f"MAKE:{self._make} MODEL:{self._model} COLOR:{self._color} YEAR:{self._year} MILEAGE:{self._mileage}\n\n"

	#Method to update existing vehicle
	def update_vehicle():
		show_inventory()
		car_index = int(input("Enter the number of the vehicle you want to update:\n"))
		make = input("Enter vehicle make:\n")
		model = input("Enter vehicle model:\n")
		color = input("Enter vehicle color:\n")
		year = int(input("Enter vehicle year:\n"))
		mileage = int(input("Enter vehicle mileage\n"))
		inventory[car_index] = Automobile(make, model, color, year, mileage)
		print(f"\nVehicle number {car_index} has been updated successfully.\n")

#Start with empty list to add invetory to
inventory = []

#Function to print inventory list with index number
def show_inventory():
	print("Vehicle Inventory\n")
	for index in range(len(inventory)):
		print(index, inventory[index], end = "\n")

#Function to add new vehicle to list
def add_vehicle():
	try:
		make = input("Enter new vehicle make:\n")
		model = input("Enter new vehicle model:\n")
		color = input("Enter new vehicle color:\n")
		year = int(input("Enter new vehicle year:\n"))
		mileage = int(input("Enter new vehicle mileage\n"))
		inventory.append(Automobile(make, model, color, year, mileage))
		print("\nNew vehicle added successfully.\n")
	except ValueError:
		print("Please enter numeric values for year and mileage.\n")

#Function to remove vehicle from Inventory
def remove_vehicle():
	show_inventory()
	vehicle_to_remove = int(input("Select vehicle number to remove: "))
	del inventory[vehicle_to_remove]
	print(f"\nYou've removed vehicle {vehicle_to_remove} from inventory.\n")

#Function to export inventory into text file
def export_inventory():
	output_file = open('inventory.txt', 'w')
	for item in inventory:
		output_file.write(str(item))
	output_file.close()
	print("\nVehicle Inventory has been exported to txt file.\n")


program_running = True 

while program_running:
	try:
		print("____MENU____") 
		print("(1) Add vehicle to inventory.")
		print("(2) Remove vehicle from inventory.")
		print("(3) Update vehicle in inventory.")
		print("(4) View inventory.")
		print("(5) Export vehicle inventory.")
		print("(6) Exit program.")

		option = int(input("\nWhat would you like to do?  Please enter a number: \n"))
		print("\n")

		if option == 1:
			add_vehicle()
		elif option == 2:
			remove_vehicle()
		elif option == 3:
			Automobile.update_vehicle()
		elif option == 4:
			show_inventory()
		elif option == 5:
			export_inventory()
		elif option == 6:
			program_running = False
			quit()
	except (ValueError, NameError):
		print("Please enter a number.  Thank you!")