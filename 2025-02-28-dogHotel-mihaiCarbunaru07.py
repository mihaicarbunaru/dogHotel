import os
import csv

class Customer:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class Booking:
    def __init__(self, customer, dog_name, check_in_date, check_out_date):
        self.customer = customer
        self.dog_name = dog_name
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date

customers = -1  
bookings = -1   

def menu_action_register_customer():
    global customers  
    name = input("Enter customer name: ")
    phone = input("Enter customer phone: ")
    email = input("Enter customer email: ")
    customer = Customer(name, phone, email)

    if customers == -1:  
        customers = []
    customers.append(customer)
    print("Customer registered successfully!")

def menu_action_create_booking():
    global bookings  
    if customers == -1:  
        print("No customers registered. Please register a customer first.")
        return
    print("Select a customer:")
    for i in range(len(customers)):  
        print(f"{i + 1}, {customers[i].name}")
    customer_index = int(input("Enter customer number: ")) - 1  
    if customer_index < 0 or customer_index >= len(customers):
        print("Invalid selection.")
        return

    dog_name = input("Enter dog's name: ")
    check_in_date = input("Enter check-in date (YYYY-MM-DD): ")
    check_out_date = input("Enter check-out date (YYYY-MM-DD): ")
    booking = Booking(customers[customer_index], dog_name, check_in_date, check_out_date)

    if bookings == -1:  
        bookings = []
    bookings.append(booking)
    print("Booking created successfully!")

def menu_action_check_in():
    if bookings == -1:  
        print("No bookings available.")
        return

    print("Select a booking to check-in:")
    for i in range(len(bookings)):  
        print(f"{i + 1}, {bookings[i].dog_name} (Customer: {bookings[i].customer.name})")
    booking_index = int(input("Enter booking number: ")) - 1
    if booking_index < 0 or booking_index >= len(bookings):
        print("Invalid selection.")
        return

    print(f"{bookings[booking_index].dog_name} checked in successfully!")

def menu_action_check_out():

    if bookings == -1:  
        print("No bookings available.")
        return
    print("Select a booking to check-out:")

    for i in range(len(bookings)):  
        print(f"{i + 1}, {bookings[i].dog_name} (Customer: {bookings[i].customer.name})")
    booking_index = int(input("Enter booking number: ")) - 1

    if booking_index < 0 or booking_index >= len(bookings):
        print("Invalid selection.")
        return
    print(f"{bookings[booking_index].dog_name} checked out successfully!")
    bookings.pop(booking_index)

def view_bookings():
    if bookings == -1:  
        print("No bookings available.")
        return
    print("Current Bookings:")
    for i in range(len(bookings)):  
        print(f"{i + 1}, Name: {bookings[i].dog_name}, Customer: {bookings[i].customer.name}, Check-in: {bookings[i].check_in_date}, Check-out: {bookings[i].check_out_date}")

def view_registered_customers():
    if customers == -1:  
        print("No registered customers.")
        return
    print("Registered customers:")
    for i in range(len(customers)):  
        print(f"{i + 1}. Customer: {customers[i].name}, Phone: {customers[i].phone}, Email: {customers[i].email}")

def load_customers_from_csv():
    global customers
    file_path = (PROGRAM_PATH + "\\customers.csv" )

    if os.path.exists(file_path): 
        customers = []  
        file = open(file_path, "r") 
        reader = csv.reader(file)

        row_counter = 0
        for row in reader:
            if row_counter > 0:  
                name, phone, email = row  
                customer = Customer(name, phone, email)
                customers.append(customer)
            row_counter += 1  

        file.close()  
        print("Customers loaded successfully!")
    else:
        customers = -1  

def menu_action_save_customers_to_csv():
    if customers == -1:  
        print("No customers to save.")
        return

    file_path = os.path.join(PROGRAM_PATH, "customers.csv")
    file = open(file_path, mode="w", newline="")
    writer = csv.writer(file)
    writer.writerow(['Name', 'Phone', 'Email'])
    for customer in customers:
        phone_to_string = f"'{customer.phone}"
        writer.writerow([customer.name, phone_to_string, customer.email])

    file.close()
    print(f"Customers saved to {file_path}")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    global customers
    load_customers_from_csv()
    while True:
        clear_screen()  
        print("\n** Dog Hotel Management **", "\n")
        print(MAIN_OP_REGISTER  ,           MAIN_OP_SEPARATOR, "Register")
        print(MAIN_OP_BOOKING   ,           MAIN_OP_SEPARATOR, "Submit a Booking")
        print(MAIN_OP_CHECKIN   ,           MAIN_OP_SEPARATOR, "Complete your Check in")
        print(MAIN_OP_CHECKOUT  ,           MAIN_OP_SEPARATOR, "Complete your Check out")
        print(MAIN_OP_PRINT_BOOKINGS  ,     MAIN_OP_SEPARATOR, "Display the booking list")
        print(MAIN_OP_SAVE_CUSTOMERS  ,     MAIN_OP_SEPARATOR, "Save customer registration")
        print(MAIN_OP_PRINT_CUSTOMERS ,     MAIN_OP_SEPARATOR, "Display the registered customers")
        print(MAIN_OP_EXIT      ,           MAIN_OP_SEPARATOR, "Press E to Exit")
        option = 0

        option = input("Enter your choice: ")

        if option == MAIN_OP_REGISTER:
            menu_action_register_customer()

        if option == MAIN_OP_BOOKING:
            menu_action_create_booking()

        if option == MAIN_OP_CHECKIN:
            menu_action_check_in()

        if option == MAIN_OP_CHECKOUT:
            menu_action_check_out()

        if option == MAIN_OP_PRINT_BOOKINGS:
            view_bookings()

        if option == MAIN_OP_SAVE_CUSTOMERS:
            menu_action_save_customers_to_csv()

        if option == MAIN_OP_PRINT_CUSTOMERS:
            view_registered_customers()

        if option == MAIN_OP_EXIT:
            print("Exiting the program. Goodbye!")
            break
        else:
            input("Press Enter to reload the menu...") 
               

PROGRAM_PATH = "C:\\pythonLearning\\examenProiect\\"

MAIN_OP_REGISTER = "1"
MAIN_OP_BOOKING = "2"
MAIN_OP_CHECKIN = "3"
MAIN_OP_CHECKOUT = "4"
MAIN_OP_PRINT_BOOKINGS = "5"
MAIN_OP_SAVE_CUSTOMERS = "6"
MAIN_OP_PRINT_CUSTOMERS = "7"
MAIN_OP_EXIT = "E"
MAIN_OP_SEPARATOR = "--"


main()
