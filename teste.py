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

def menu():
    while True:
        print("\n--- CRM Menu ---")
        print("1. Add Contact")
        print("2. Update Contact")
        print("3. Remove Contact")
        print("4. List Contacts")
        print("5. Add Appointment")
        print("6. Update Appointment")
        print("7. Remove Appointment")
        print("8. List Appointments")
        print("9. Exit")
        
        choice = input("Choose an option (1-9): ")

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
            title = input("Enter appointment title: ")
            date_time = input("Enter appointment date and time (YYYY-MM-DD HH:MM): ")
            description = input("Enter description (optional): ")
            add_appointment(title, date_time, description)
        elif choice == '6':
            title = input("Enter the title of the appointment to update: ")
            new_date_time = input("Enter new date and time (YYYY-MM-DD HH:MM) or press Enter to skip: ")
            new_description = input("Enter new description or press Enter to skip: ")
            update_appointment(title, new_date_time if new_date_time else None, new_description if new_description else None)
        elif choice == '7':
            title = input("Enter the title of the appointment to remove: ")
            remove_appointment(title)
        elif choice == '8':
            list_appointments()
        elif choice == '9':
            print("Exiting CRM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

menu()
