# List of registered users and passwords
registered_users = ['jovan1', 'jovan2', 'jovan3', 'jovan4', 'jovan5']
registered_passwords = ['bachtiar1', 'bachtiar2', 'bachtiar3', 'bachtiar4', 'bachtiar5']

# Login function to verify the users
def login():
    print("Welcome to Didi Rental")
    while True:
        username = input("Please enter your username: ")
        if username in registered_users:  
            user_index = registered_users.index(username)  
            while True:
                password = input("Please enter your password: ")
                if password == registered_passwords[user_index]:  
                    print(f"Hi {username}, Welcome to Didi Rental, Hope you have a good day!")
                    return True
                else:
                    print("Wrong password, please try again.")
        else:
            print(f"{username} is not registered in Didi Rental. Please try again")

car_data = []

# Add a new car function to display the car that can be rented
def add_car():
    car = {}
    car['id'] = input("Please enter car ID: ")
    car['name'] = input("Please enter name of the car: ")
    car['seats'] = input("Please enter how many seats that the car can have: ")
    car['price_per_day'] = input("Please enter the price per day of the car: ")
    car['availability'] = True
    car_data.append(car)
    print("Car already added into the database")
    
# Get the status of the aavailability for the car
def get_car_status(availability):
    return "Available" if availability else "Not Available"

# View all cars that can be rented
def view_car():
    print("List of cars that can be rented: \n")
    if len(car_data)==0:
        print ("There are no cars in the database")
    else:
        for car in car_data:
            status = get_car_status(car['availability'])
            print(f"ID: {car['id']}, Name: {car['name']}, Type: {car['seats']}, Price: {car['price_per_day']}, status: {status}")          
            
# Update data for the car in the database
def update_car():
    car_id = input("Please input car's ID to update: ")
    for car in car_data: 
        if car_id == car['id']:
            status = get_car_status(car['availability'])
            print(f"Here the information of the car:\nID: {car['id']}, Name: {car['name']}, Type: {car['seats']}, Price: {car['price_per_day']}, status: {status}")
            print("1. Name of the car: ")
            print("2. Type of the car (seats): ")
            print("3. Price of the car per day: ")
            print("4. Avalability status of the car: ")
            choice= input("Please choose the aspect of the car that you want to update: ")
            
            if choice == "1": 
                new_name = input("Please input the new name of the car: ")
                if not new_name:
                    print("Name of the car is not changed.")
                elif new_name == car['name']:
                    print("Name of the car is same as before.")
                else:
                    car['name'] = new_name
                    print("New name of the car is already updated.")
                    
            elif choice == "2":
                new_type = input("Please input the new type of the car: ")
                if not new_type:
                    print("Type of the car is not changed.")
                elif new_type == car['seats']:
                    print("Type of the car is same as before.")
                else:
                    car['seats'] = new_type
                    print("New type of the car is already updated.")
                    
            elif choice == "3":
                new_price = input("Please input the new price of the car per day: ")
                if not new_price:
                    print("Price of the car per day is not changed.")
                elif new_price == car['price_per_day']:
                    print("Price of the car per day is same as before.")
                else: 
                    car['price_per_day'] = new_price
                    print("New price of the car per day is already updated.")
                    
            elif choice == "4":
                new_status = input("Do you want to mark the car as available? (y/n): ").lower()
                if new_status == 'y':
                    if car['availability']:
                        print("The car is already available.")
                    else:
                        car['availability'] = True
                        print("The car is now marked as available.")
                elif new_status == 'n':
                    if not car['availability']:
                        print("The car is already unavailable.")
                    else:
                        car['availability'] = False
                        print("The car is now marked as unavailable.")
                else:
                    print("Invalid input. Status is not changed.")
                
            else:
                print("Invalid input.")
                return update_car()
        else: 
            print("ID of the car is invalid.")

# Delete car from the database
def delete_car():
    car_id = input("Please input car's ID to delete: ")
    for car in car_data:
        if car['id'] == car_id:
            car_data.remove(car)
            print("The car is already removed from the database.")
            return
        else:
            print("Invalid input. ID of the car is invalid.")
    
# Rent car service
def rent_car():
    # check if there are cars in the database
    if not car_data:
        print("There are no cars that available to rent.")
        return
    
    print("Available cars: ")
    for car in car_data:
        if car['availability']:
            print(f"ID: {car['id']}, Name: {car['name']}, Type: {car['seats']}, Price: {car['price_per_day']}")
            
    car_id = input("Please input the ID of the car you want to rent: ")
    for car in car_data:
        if car_id == car['id']:
            if not car['availability']:
                print("Sorry, this car is not available at the moment")
                return
            else:
                # Ask input user's name
                user_name = input("Please input your name: ")
                # Validate the numbers of day that renter wants to rent
                days_of_rent = input("Please input how many days you want to rent the car: ")
                if not days_of_rent.isdigit():
                    print("Invalid input.")
                    return
                else:
                    # Calculate the numbers of day that renter wants to rent and update car availability
                    days = int(days_of_rent)
                    total_price = int(car['price_per_day']) * days
                    car['availability'] = False
                    print(f"Car successfully rented by {user_name} for {days} days.")
                    print(f"Total price: {total_price}")
                    return
        else:
            print("Car ID is not found. Please try again.")

# Return car service            
def return_car():
    if not car_data:  # Check if the car database is empty
        print("There are no cars in the database.")
        return
    
    car_id = input("Enter the ID of the car you want to return: ")
    
    for car in car_data:
        if car['id'] == car_id:
            if not car['availability']:  # Check if the car is currently rented
                car['availability'] = True  # Mark the car as available
                print(f"The car with ID '{car_id}' has been successfully returned!")
                return
            else:
                print(f"The car with ID '{car_id}' is already available and was not rented.")
                return        
            
        else: 
            print(f"No car with ID '{car_id}' was found in the database.")

# Menu
def main_menu():
    while True:
        print("\nMenu Rental Mobil")
        print("1. Add new car")
        print("2. View all cars in the database")
        print("3. Update car in the database")
        print("4. Delete car from the database")
        print("5. Rent car")
        print("6. Return car")
        print("7. Exit")
        choice = input("Please choose your option: ")
        if choice == "1":
            add_car()
        elif choice == "2":
            view_car()
        elif choice == "3":
            update_car()
        elif choice == "4":
            delete_car()
        elif choice == "5":
            rent_car()
        elif choice == "6":
            return_car()
        elif choice == "7":
            print("Thank you for using Didi Rental Car service!")
            break
        else:
            print("Invalid input.")    
        
# Run the application
if __name__ == "__main__":
    login()
    main_menu()