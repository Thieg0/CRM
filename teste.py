from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

contacts = []

def add_contact(name, phone, email):
    contact = {
        'name': name,
        'phone': phone,
        'email': email
    }
    contacts.append(contact)
    print(f'Contact added: {name}')

    add_lead(name, email, phone, source = 'contact_added', status = "Leads")
 
def update_contact(name, new_phone = None, new_email = None):
    for contact in contacts:
        if contact['name'] == name:
            if new_phone:
                contact['phone'] = new_phone
            if new_email:
                contact['email'] = new_email
            return True
    print(f'Contact not found: {name}')
    return False

def remove_contact(name):
    for contact in contacts:
        if contact['name'] == name:
            contacts.remove(contact)
            print(f'Contact removed: {name}')
            return True
    print(f'Contact not found: {name}')
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

    list_contacts()
    contact_name = input("Enter the name of the contact to associate with this deal (or press Enter to skip): ")
    contact = nect((c for c in contacts if c['name'] == contact_name), None)
    
    deal = {"name": name, "value": value, "stage": stage, 'contact': contact}
    deals.append(deal)
    sales_pipeline[stage].append(deal)
    print(f"Deal added: {name} in stage {stage}")

def move_deal():
    list_deals()
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
    list_deals()
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
                print(f"Name: {deal['name']}, Email: {deal['email']}, Phone: {deal['phone']}, Value: {deal['value']}")
                if deal.get('contact'):
                    print(f"    Associated Contact: {deal['contact']['name']}")

activities = []

def contact_exists(contact_name):
    return any(contact['name'] == contact_name for contact in contacts)

def add_activity(contact_name, activity_type, date_time, description = ""):
    if not contact_exists(contact_name):
        print(f"Contact not found: {contact_name}")
        return

    try:
        date_time_formatted = datetime.strptime(date_time, "%Y-%m-%d %H:%M")
    except ValueError:
        print('Invalid date and time format. Use YYYY-MM-DD HH:MM')
        return

    activity = {
        'contact_name': contact_name,
        'activity_type': activity_type,
        'date_time': date_time_formatted,
        'description': description
    }
    activities.append(activity)
    print(f'Activity added: {activity_type} with {contact_name} at {date_time}')

def update_activity(contact_name, activity_type, new_date_time = None, new_description = None):
    for activity in activities:
        if activity['contact_name'] == contact_name and activity['activity_type'] == activity_type:
            if new_date_time:
                try:
                    date_time_formatted = datetime.strptime(new_date_time, "%Y-%m-%d %H:%M")
                except ValueError:
                    print('Invalid date and time format. Use YYYY-MM-DD HH:MM')
                    return
                activity['date_time'] = date_time_formatted
            if new_description:
                activity['description'] = new_description
            print(f'Activity updated: {activity_type} with {contact_name}')
            return True
    print(f'Activity not found: {activity_type} with {contact_name}')
    return False

def remove_activity(contact_name, activity_type):
    for activity in activities:
        if activity['contact_name'] == contact_name and activity['activity_type'] == activity_type:
            activities.remove(activity)
            print(f'Activity removed: {activity_type} with {contact_name}')
            return True
    print(f'Activity not found: {activity_type} with {contact_name}')
    return False

def list_activities(contact_name):
    contact_activities = [activity for activity in activities if activity['contact_name'] == contact_name]
    if not contact_activities:
        print(f'No activities found for {contact_name}')
    else:
        sorted_activities = sorted(contact_activities, key=lambda k: k['date_time'])
        for activity in sorted_activities:
            print(f'Activity: {activity["activity_type"]} with {activity["contact_name"]} at {activity["date_time"]}, Description: {activity["description"]}')

email_campaigns = []

def send_email_campaign(subject, content, recipients):
    # Solicitar o email e senha do usuario'
    sender_email = input("Enter your email: ")
    sender_password = input("Enter your password (use an app password if you have 2FA enabled): ")

    # Configuracao do servidor SMTP (exemplo para o Gmail)
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            
            message = MIMEMultipart()
            message["From"] = sender_email
            message["Subject"] = subject
            message.attach(MIMEText(content, "plain"))

            for recipient in recipients:
                message["To"] = recipient
                server.sendmail(sender_email, recipient, message.as_string())
            print(f'Email campaign sent successfully to {recipient}')
    
    except Exception as e:
        print(f'Error sending email: {e}')

def create_email_campaign(subject, content, recipients):
    campaign = {
        'subject': subject,
        'content': content,
        'recipients': recipients,
        'status': 'draft', # draft, sending, sent
        'emails_sent': 0,
        'emails_opened': 0,
        'emails_clicked': 0
    }
    email_campaigns.append(campaign)
    print(f'Email campaign created: {subject}')

def track_email_open(campaign_index, recipient_email):
    if campaign_index < 0 or campaign_index >= len(email_campaigns):
        print('Invalid campaign index')
        return
    
    campaign = email_campaigns[campaign_index]
    if recipient_email not in campaign['recipients']:
        print(f'Recipient {recipient_email} not found in campaign')
        return
    
    campaign['emails_opened'] += 1j
    print(f'Email opened by {recipient_email}. Total opens: {campaign["emails_opened"]}')

def track_email_click(campaign_index, recipient_email):
    if campaign_index < 0 or campaign_index >= len(email_campaigns):
        print('Invalid campaign index')
        return
    
    campaign = email_campaigns[campaign_index]
    if recipient_email not in campaign['recipients']:
        print(f'Recipient {recipient_email} not found in campaign')
        return
    
    campaign['emails_clicked'] += 1
    print(f'Email clicked by {recipient_email}. Total clicks: {campaign["emails_clicked"]}')

def list_email_campaigns():
    if not email_campaigns:
        print('No email campaigns found')
    else:
        for index, campaign in enumerate(email_campaigns):
            print(f'Index: {index}, Subject: {campaign["subject"]}, Status: {campaign["status"]}, Recipients: {len(campaign["recipients"])} \nEmails sent: {campaign["emails_sent"]}, Emails opened: {campaign["emails_opened"]}, Emails clicked: {campaign["emails_clicked"]}')

leads = []

def add_lead(name, email, phone, source, status = "new"):
    lead = {
        'name': name,
        'email': email,
        'phone': phone,
        'source': source,
        'status': status,
        'interactions': []
    }
    leads.append(lead)

    if status in sales_pipeline:
        sales_pipeline[status].append(lead)
    print(f'Lead added: {name}')

def update_lead_status(name, new_status):
    for lead in leads:
        if lead['name'] == name:
            
            if lead['status'] in sales_pipeline:
                sales_pipeline[lead['status']] = [1 for 1 in sales_pipeline[lead['status']] if 1['name'] != name]

            lead['status'] = new_status

            if new_status in sales_pipeline:
                sales_pipeline[new_status].append(lead)
            print(f'Lead status updated: {name} -> {new_status}')
            return True
    print(f'Lead not found: {name}')
    return False

def add_interaction(name, interaction_type, description = ""):
    for lead in leads:
        if lead['name'] == name:
            interaction = {
                'type': interaction_type,
                'description': description,
                'date_time': datetime.now().strftime("%Y-%m-%d %H:%M")
            }
            lead['interactions'].append(interaction)
            print(f'Interaction added: {interaction_type} with {name}')
            return True
    print(f'Lead not found: {name}')
    return False

def list_leads(filter_status = None):
    if not leads:
        print('No leads found')
    else:
        for lead in leads:
            if filter_status and lead['status'] != filter_status:
                continue
            print(f'\nName: {lead['name']}')
            print(f'Email: {lead['email']}')
            print(f'Phone: {lead['phone']}')
            print(f'Source: {lead['source']}')
            print(f'Status: {lead['status']}')
            print('Interactions:')
            for interaction in lead['interactions']:
                print(f' - {interaction['date_time']}: {interaction['type']} - {interaction['description']}')

users = {
    'seller1': {'role': 'seller', 'name': 'Joao vendedor'},
    'seller2': {'role': 'seller', 'name': 'Maria vendedora'},
    'manager1': {'role': 'manager', 'name': 'Jose gerente'},
    'admin1': {'role': 'admin', 'name': 'Ana administradora'}
}

def seller_dashboard(username):
    user = users.get(username)
    if not user or user['role'] != 'seller':
        print('Access denied. You must be a seller to access this dashboard.')
        return
    
    print(f'\n--- Seller Dashboard ---\nHello, {user['name']}')
    print('Your contacts:')
    list_contacts()
    print('Your appointments:')
    list_appointments()
    print('Your deals:')
    list_deals()
    print('Your leads:')
    list_leads()

def manager_dashboard(username):
    user = users.get(username)
    if not user or user['role'] != 'manager':
        print('Access denied. You must be a manager to access this dashboard.')
        return
    
    print(f'\n--- Manager Dashboard ---\nHello, {user['name']}')
    print('Sales pipeline Overview:')
    list_deals()
    print('\nPerfomance Metrics:')
    print(f'Total of leads: {len(leads)}')
    print(f'Total of deals: {len(deals)}')
    print(f'Total of Revenue: ${sum(deal['value'] for deal in deals)}')

def admin_dashboard(username):
    user = users.get(username)
    if not user or user['role'] != 'admin':
        print('Access denied. You must be an admin to access this dashboard.')
        return
    
    print(f'\n--- Admin Dashboard ---\nHello, {user['name']}')
    print('All contacts:')
    list_contacts()
    print('All appointments:')
    list_appointments()
    print('All deals:')
    list_deals()
    print('All leads:')
    list_leads()
    print('All Email campaigns:')
    list_email_campaigns()	

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

def activities_menu():
    while True:
        print("\n--- Activities Menu ---")
        print("1. Add Activity")
        print("2. Update Activity")
        print("3. Remove Activity")
        print("4. List Activities")
        print("5. Back to Main Menu")
        
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            contact_name = input("Enter the name of the contact: ")
            activity_type = input("Enter the type of activity: ")
            date_time = input("Enter date and time (YYYY-MM-DD HH:MM): ")
            description = input("Enter description (optional): ")
            add_activity(contact_name, activity_type, date_time, description)
        elif choice == '2':
            contact_name = input("Enter the name of the contact: ")
            activity_type = input("Enter the type of activity: ")
            new_date_time = input("Enter new date and time (YYYY-MM-DD HH:MM) or press Enter to skip: ")
            new_description = input("Enter new description or press Enter to skip: ")
            update_activity(contact_name, activity_type, new_date_time if new_date_time else None, new_description if new_description else None)
        elif choice == '3':
            contact_name = input("Enter the name of the contact: ")
            activity_type = input("Enter the type of activity: ")
            remove_activity(contact_name, activity_type)
        elif choice == '4':
            contact_name = input("Enter the name of the contact: ")
            list_activities(contact_name)
        elif choice == '5':
            print("Returning to Main Menu")
            break
        else:
            print("Invalid choice. Please try again.")

def email_campaigns_menu():
    while True:
        print("\n--- Email Campaigns Menu ---")
        print("1. Create Email Campaign")
        print("2. Send Email Campaign")
        print("3. Track Email Open")
        print("4. Track Email Click")
        print("5. List Email Campaigns")
        print("6. Back to Main Menu")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            subject = input("Enter the email subject: ")
            content = input("Enter the email content: ")
            recipients = input("Enter the recipients emails separated by commas: ").split(',')
            recipients = [email.strip() for email in recipients]
            create_email_campaign(subject, content, recipients)
        elif choice == '2':
            list_email_campaigns()
            campaign_index = int(input("Enter the index of the campaign to send: "))
            campaign = email_campaigns[campaign_index]
            send_email_campaign(campaign['subject'], campaign['content'], campaign['recipients'])
        elif choice == '3':
            list_email_campaigns()
            campaign_index = int(input("Enter the index of the campaign to track: "))
            recipient_email = input("Enter the recipient email to track: ")
            track_email_open(campaign_index, recipient_email)
        elif choice == '4':
            list_email_campaigns()
            campaign_index = int(input("Enter the index of the campaign to track: "))
            recipient_email = input("Enter the recipient email to track: ")
            track_email_click(campaign_index, recipient_email)
        elif choice == '5':
            list_email_campaigns()
        elif choice == '6':
            print("Returning to Main Menu")
            break
        else:
            print("Invalid choice. Please try again.")

def leads_menu():
    while True:
        print("\n--- Leads Menu ---")
        print("1. Add Lead")
        print("2. Update Lead Status")
        print("3. Add Interaction")
        print("4. List Leads")
        print("5. Back to Main Menu")
        
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            name = input("Enter name: ")
            email = input("Enter email: ")
            phone = input("Enter phone: ")
            source = input("Enter source: ")
            status = input("Enter status (optional): ")
            add_lead(name, email, phone, source, status if status else "new")
        elif choice == '2':
            name = input("Enter the name of the lead to update: ")
            new_status = input("Enter new status: ")
            update_lead_status(name, new_status)
        elif choice == '3':
            name = input("Enter the name of the lead: ")
            interaction_type = input("Enter the type of interaction (call, meeting, email, etc.): ")
            description = input("Enter description (optional): ")
            add_interaction(name, interaction_type, description)
        elif choice == '4':
            filter_status = input("Enter status to filter (optional): ")
            list_leads(filter_status if filter_status else None)
        elif choice == '5':
            print("Returning to Main Menu")
            break
        else:
            print("Invalid choice. Please try again.")

def dashboard_menu(username):
    user = users.get(username)
    if not user:
        print("User not found.")
        return

    while True:
        print(f"\n--- Dashboard Menu ({user['name']}) ---")
        print("1. View Dashboard")
        print("2. Back to Main Menu")
        
        choice = input("Choose an option (1-2): ")

        if choice == '1':
            if user['role'] == 'seller':
                seller_dashboard(username)
            elif user['role'] == 'manager':
                manager_dashboard(username)
            elif user['role'] == 'admin':
                admin_dashboard(username)
        elif choice == '2':
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
        print("4. Activities")
        print("5. Email Campaigns")
        print("6. Leads")
        print("7. Dashboards")
        print("8. Exit")

        choice = input("Choose an option (1-7): ")

        if choice == '1':
            contacts_menu()
        elif choice == '2':
            appointments_menu()
        elif choice == '3':
            deals_menu()
        elif choice == '4':
            activities_menu()
        elif choice == '5':
            email_campaigns_menu()
        elif choice == '6':
            leads_menu()
        elif choice == '7':
            username = input("Enter your username: ")
            dashboard_menu(username)
        elif choice == '8':
            print("Exiting program")
            break
        else:
            print("Invalid choice. Please try again.")
menu()
