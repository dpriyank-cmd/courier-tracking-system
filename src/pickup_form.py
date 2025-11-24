def create_pickup_form():
    print("Pickup Request Form")
    name = input("Enter your name: ")
    address = input("Enter pickup address: ")
    date = input("Enter pickup date: ")
    
    print("\nPickup Request Created Successfully!")
    print(f"Name: {name}, Address: {address}, Date: {date}")

# Run Test
create_pickup_form()
