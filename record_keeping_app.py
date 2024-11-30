# Create an empty dictionary to store the records
records = {}

# Function to display records
def display_records():
    if records:
        print("\nCurrent Records:")
        for key, value in records.items():
            print(f"{key}: {value}")
    else:
        print("\nNo records found.")

# Start the application
while True:
    # Ask the user for the action they want to perform
    print("\nChoose an action:")
    print("a. Add Data")
    print("b. Delete Data")
    print("c. End")
    action = input("Enter your choice: ").lower()

    if action == 'a' or action == 'A':
        # Add Data
        key = input("Enter Key (e.g., Lastname): ")
        value = input("Enter Value: ")
        records[key] = value
        display_records()

    elif action == 'b' or action == 'B':
        # Delete Data
        key = input("Enter the key you want to delete: ")
        if key in records:
            del records[key]
            print(f"{key} has been removed.")
        else:
            print(f"{key} not found in records.")
        display_records()

    elif action == 'c' or action == 'C':
        # End the program
        print("\nTHANK YOU")
        break

    else:
        print("Invalid option. Please choose again.")
