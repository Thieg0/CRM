from datetime import datetime

contacts = []

def add_contact(name, phone, email):
    contact = {
        'name': name,
        'phone': phone,
        'email': email
    }
    contacts.append(contact)
 
def update_contact(name, new_phone = None, new_email = None):
    for contact in contacts:
        if contact['name'] == name:
            if new_phone:
                contact['phone'] = new_phone
            if new_email:
                contact['email'] = new_email
            return True
    return False

def remove_contact(name):
    for contact in contacts:
        if contact['name'] == name:
            contacts.remove(contact)
            return True
    return False

def list_contacts():
    if not contacts:
        print('No contacts found')
    else:
        for contact in contacts:
            print(f'Name: {contact["name"]}, Phone: {contact["phone"]}, Email: {contact["email"]}')

appointments = []

def add_appointment(title, date_time, description =""):
    try:
        date_time_formatted = datetime.strptime(date_time, "%Y-%m-%d %H:%M")
    except ValueError:
        print('Invalid date and time format. Use YYYY-MM-DD HH:MM')
        return

    appointment = {
        'title': title,
        'date_time': date_time_formatted,
        'description': description
    }
    appointments.append(appointment)
    print(f'Appointment added: {title} at {date_time}')

def update_appointment(title, new_date_time = None, new_description = None):
    for appointment in appointments:
        if appointment['title'] == title:
            if new_date_time:
                try:
                    date_time_formatted = datetime.strptime(new_date_time, "%Y-%m-%d %H:%M")
                except ValueError:
                    print('Invalid date and time format. Use YYYY-MM-DD HH:MM')
                    return
                appointment['date_time'] = date_time_formatted
            if new_description:
                appointment['description'] = new_description
            print(f'Appointment updated: {title}')
            return True
    print(f'appointment not found: {title}')
    return False

def remove_appointment(title):
    for appointment in appointments:
        if appointment['title'] == title:
            appointments.remove(appointment)
            print(f'Appointment removed: {title}')
            return True
    print(f'appointment not found: {title}')
    return False

def list_appointments():
    if not appointments:
        print('No appointments found')
    else:
        sorted_appointments = sorted(appointments, key=lambda k: k['date_time'])
        for appointment in sorted_appointments:
            print(f'Title: {appointment["title"]}, Date and time: {appointment["date_time"]}, Description: {appointment["description"]}')

sales_pipeline = {
    "Leads": [],
    "Proposal sent": [],
    "Negotiation": [],
    "Closed": []
}

def add_deal():
    name = input("Enter the name of the deal: ")
    value = float(input("Enter the value of the deal: "))
    stage = input("Enter the stage of the deal (Leads, Proposal sent, Negotiation, Closed): ")
    if stage not in sales_pipeline:
        print("Invalid stage. Deal not added.")
        return
    deal = {"name": name, "value": value, "stage": stage}
    sales_pipeline[stage].append(deal)
    print(f"Deal added: {name} in stage {stage}")

def move_deal():
    name = input("Enter the name of the deal to move: ")
    new_stage = input("Enter the new stage of the deal (Leads, Proposal sent, Negotiation, Closed): ")
    if new_stage not in sales_pipeline:
        print("Invalid stage. Deal not moved.")
        return

    for stage in sales_pipeline:
        for deal in sales_pipeline[stage]:
            if deal["name"] == name:
                sales_pipeline[stage].remove(deal)
                deal["stage"] = new_stage
                sales_pipeline[new_stage].append(deal)
                print(f"Deal moved: {name} to stage {new_stage}")
                return
    print(f"Deal not found: {name}")

def remove_deal():
    name = input("Enter the name of the deal to remove: ")
    for stage in sales_pipeline:
        for deal in sales_pipeline[stage]:
            if deal["name"] == name:
                sales_pipeline[stage].remove(deal)
                print(f"Deal removed: {name}")
                return
    print(f"Deal not found: {name}")

def list_deals():
    for stage, deals in sales_pipeline.items():
        print(f"\nStage: {stage}")
        if not deals:
            print("No deals found")
        else:
            for deal in deals:
                print(f"Name: {deal['name']}, Value: {deal['value']}")

def contacts_menu():
    while True:
        print("\n--- Contacts Menu ---")
        print("1. Add Contact")
        print("2. Update Contact")
        print("3. Remove Contact")
        print("4. List Contacts")
        print("5. Back to Main Menu")
        
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            add_contact(name, phone, email)
        elif choice == '2':
            name = input("Enter the name of the contact to update: ")
            new_phone = input("Enter new phone (or press Enter to skip): ")
            new_email = input("Enter new email (or press Enter to skip): ")
            update_contact(name, new_phone if new_phone else None, new_email if new_email else None)
        elif choice == '3':
            name = input("Enter the name of the contact to remove: ")
            remove_contact(name)
        elif choice == '4':
            list_contacts()
        elif choice == '5':
            print("Returning to Main Menu")
            break
        else:
            print("Invalid choice. Please try again.")

def appointments_menu():
    while True:
        print("\n--- Appointments Menu ---")
        print("1. Add Appointment")
        print("2. Update Appointment")
        print("3. Remove Appointment")
        print("4. List Appointments")
        print("5. Back to Main Menu")
        
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            title = input("Enter appointment title: ")
            date_time = input("Enter appointment date and time (YYYY-MM-DD HH:MM): ")
            description = input("Enter description (optional): ")
            add_appointment(title, date_time, description)
        elif choice == '2':
            title = input("Enter the title of the appointment to update: ")
            new_date_time = input("Enter new date and time (YYYY-MM-DD HH:MM) or press Enter to skip: ")
            new_description = input("Enter new description or press Enter to skip: ")
            update_appointment(title, new_date_time if new_date_time else None, new_description if new_description else None)
        elif choice == '3':
            title = input("Enter the title of the appointment to remove: ")
            remove_appointment(title)
        elif choice == '4':
            list_appointments()
        elif choice == '5':
            print("Returning to Main Menu")
            break
        else:
            print("Invalid choice. Please try again.")

def deals_menu():
    while True:
        print("\n--- Deals Menu ---")
        print("1. Add Deal")
        print("2. Move Deal")
        print("3. Remove Deal")
        print("4. List Deals")
        print("5. Back to Main Menu")
        
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            add_deal()
        elif choice == '2':
            move_deal()
        elif choice == '3':
            remove_deal()
        elif choice == '4':
            list_deals()
        elif choice == '5':
            print("Returning to Main Menu")
            break
        else:
            print("Invalid choice. Please try again.")

def menu():
    while True:
        print("\n--- Main Menu ---")
        print("1. Contacts")
        print("2. Appointments")
        print("3. Deals")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            contacts_menu()
        elif choice == '2':
            appointments_menu()
        elif choice == '3':
            deals_menu()
        elif choice == '4':
            print("Exiting program")
            break
        else:
            print("Invalid choice. Please try again.")
menu()
