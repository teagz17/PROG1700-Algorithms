'''
w0302952
teagan stewart
PROG1700
november 22nd, 2023
Order and Customer Management assignment
'''
# import modules
import sys
# main dictionary
customers = {
    '1': {
        'lastName': 'kiryu',
        'firstName': 'kazuma', 
        'contact': '667-651-8512', 
        'orders': [],
        'total_spent': 0
        },
    '2': {
        'lastName': 'majima',
        'firstName': 'goro', 
        'contact': '667-318-7163', 
        'orders': [],
        "total_spent": 0
        }
    }
# global variables
attempts = 5
# functions
# security
def attempt(): # subtracts from attempt counter when an invalid input is entered
    global attempts
    attempts -= 1
    print(f'\nerror: invalid input. you have {attempts} attempts remaining')

# a)
def add_customer():
    while attempts > 0:
        add_cust_id = input("\nnew customer id (numbers only, max. 3 characters): ")
        if add_cust_id == 'menu':
            menu()
        if add_cust_id in customers:
            print("\ncustomer id is already in use.")
            attempt()
        elif add_cust_id.isdigit() and len(add_cust_id) <=3: # requires the user to use numbers for the id and enforces the 3 character max rule
            add_cust_lastname = input("new customer's last name (letters only, max. 10 characters): ")
            if add_cust_lastname.isalpha() and len(add_cust_lastname) <= 10: # only lets you use letters
                add_cust_firstname = input("new customer's first name (letters only, max. 10 characters): ")
                if add_cust_firstname.isalpha() and len(add_cust_lastname) <= 10:
                    add_cust_contact = input("new customer's contact number (xxx-xxx-xxxx): ")
                    if len(add_cust_contact) == 12: # ensures the user follows the template for the phone number
                        customers[add_cust_id] = {'lastName': add_cust_lastname, 'firstName': add_cust_firstname, 'contact': add_cust_contact, 'orders': [], 'total_spent': 0} # adds a new customer to the dictionary using the information entered by the user
                        print('\ncustomer successfully added.')
                        menu() # returns to the menu
                    else:
                        attempt()
                else:
                    attempt()
            else:
                attempt()
        else:
            attempt()
    else:
        sys.exit() # exits the program after too many invalid inputs

# b)
def place_order():
    while attempts > 0:
        try: 
            cust_id = input('\ncustomer id (whole numbers only): ')
            if cust_id == 'menu':
                menu()
            if cust_id.isdigit() and cust_id in customers:
                product_name = str(input('product name: '))
                unit_price = float(input('unit price: '))
                unit_quantity = int(input('quantity: '))
                total_cost = unit_price * unit_quantity # calculates the total cost of the order
                    
                order = { # the new order dictionary
                    'order_id': len(customers[cust_id]['orders']) + 1,
                    'product_name': product_name,
                    'quantity': unit_quantity,
                    'total_cost': total_cost
                } 
                customers[cust_id]['orders'].append(order) # adds the order to the dicitonary
                total_spent = customers[cust_id]['total_spent'] # takes the previous value from the dictionary
                total_spent += total_cost # updates the value
                customers[cust_id]['total_spent'] = total_spent #returns the value to the dictionary. without adding this line the new total spent value would be applied to all customers
                print(f'\ntotal cost: {round(total_cost, 2)}')
                print('\norder placed successfully.')
                menu()
            else:
                attempt()
        except ValueError:
            attempt()
    else:
        sys.exit()

# c)
def generate_customer_report():
    while attempts > 0:
        cust_id = input("enter customer id: ")
        if cust_id == 'menu':
            menu()
        if cust_id in customers:
            print(f"\ncustomer report for {customers[cust_id]['firstName']} {customers[cust_id]['lastName']}: \ncontact: {customers[cust_id]['contact']} \norders: {customers[cust_id]['orders']} \ntotal spent: {customers[cust_id]['total_spent']}" ) # "\n" indicates a line breeak
            menu()
        else: # takes an attempt away if the entered id isn't in the dictionary
            attempt()
    else:
        sys.exit()

# d)
def generate_all_reports():
    for cust_id in customers: # iterates through the dictionary
        print(f"\ncustomer report for {customers[cust_id]['firstName']} {customers[cust_id]['lastName']}: \ncontact: {customers[cust_id]['contact']} \norders: {customers[cust_id]['orders']} \ntotal spent: {customers[cust_id]['total_spent']}" )
    menu()

# menu
def menu():
    while True:
        while attempts > 0:
            try:
                print(f"\norder and customer management system \nmain menu:\n \n1) add customer \n2) place order \n3) generate customer report \n4) generate all customer reports \n5) exit \ntype 'menu' into any of the first inputs if you need to return to the menu.")
                user_input = int(input('\nwhat would you like to do? ')) # lets the user pick the function they want to use by entering the corresponding number
                if user_input >=1 and user_input <= 5: # onlt lets the user choose between 1 and 5
                    if user_input == 1:
                        add_customer()
                    elif user_input == 2:
                        place_order()
                    elif user_input == 3:
                        generate_customer_report()
                    elif user_input == 4:
                        generate_all_reports()
                    elif user_input == 5:
                        exit_input = input("\nare you sure? ('n' to return to menu, or press enter to close)")
                        if exit_input == "n":
                            break #returns to the menu
                        else: #exits the system
                            sys.exit()
                    else:
                        attempt()                        
                elif user_input < 1 or user_input > 5:
                    attempt()
            except ValueError:
                attempt()
        else:
            sys.exit()
# main program
menu() #runs the main program