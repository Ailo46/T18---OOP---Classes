''' ===== OOP-Classes Task 1 ===== '''

from datetime import datetime
from tabulate import tabulate

# Create a Student class
class Email():
    ''' Create an Email class and initialise a constructor that takes in three
        arguments:
            ○ email_address - the email address of the sender.
            ○ subject_line - the subject line of the email.
            ○ email_content - the contents of the email.
            ○ email_date - I have added this one as the email date
    '''
# Constructor method
    def __init__(self, email_address, subject_line, email_content, email_date):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.email_date = email_date

    # Class variables
    has_been_read = False

    # Method to make hase_been_read to True
    def mark_as_read(self):
        self.has_been_read = True

# ============================================================================================

def populate_inbox(email_address, subject_line, email_content, email_date):
    ''' A function which creates an email object with the email address, 
        subject line, and contents, and email_date. After each creation 
        it stores it in the inbox list.
    '''
    # creates email object and appends it to the inbox list
    new_email = Email(email_address, subject_line, email_content, email_date)
    inbox.append(new_email)
    return

# ============================================================================================

def list_emails(list_order = "all"):
    ''' a function that loops through the inbox and prints each email’s
        subject_line, along with a corresponding number. I have added an
        optional parameter for making ability to list all emails or only
        list the unread emails in each call time.(default is all)
    '''
    
    # makes a clear table to be used in tabulate 
    table = []
    print("\n")

    # list inbox elements using an enumerate for loop
    if list_order == "unread":
        
        # for listing just the unread emails 
        item_number = 1
        for current_email in inbox:
            
            if not current_email.has_been_read: # only not marked-as-read object will count in the table
                table.append([item_number, current_email.subject_line, "No"])
                item_number +=1
    
    else:
        # for listing all emails using enumerate
        for item_number, current_email in enumerate(inbox, 1):
            table.append([item_number, current_email.subject_line, "Yes" if current_email.has_been_read else "No"])
    
    # in case of empty table for listing, just print the message, otherwise will be printed using tabulate
    if table == []:
        print("\n >> There is no unread email to show <<\n")

    else:
        print(f"\t\t** {list_order} email list **")
        print(tabulate(table, headers=["item","Subject Line", "Hass been read"], colalign=("center","left","center"), tablefmt="mixed_outline"), '\n')
    return

# ============================================================================================

def read_email():
    ''' This function that displays a selected email, together with the 
        email_address, subject_line, email_content, and email_date, then 
        will sets its has_been_read instance variable to True.
    '''
    
    # ask user to choose item:
    choise = (input("\nPlease enter the item number to read (0 for back to inbox): "))
        
    # Input validation if entered no numbers, or not in range of number of emails:
    if choise.isdigit():
        item_to_read = int(choise)
        
        if item_to_read == 0:
            print("\tOk, back to inbox...\n")
            return
        
        elif item_to_read > len(inbox):
            print("\tinvalid number !\n\treturned to inbox... \n")
            return
    else:
        print("\tinvalid input !\n\treturned to inbox... \n")
        return

    # taking the selected Email object from the inbox list
    selected_email = inbox[item_to_read - 1]
    
    # call mark_as_read class method to mark it as read
    selected_email.mark_as_read()
    
    # printing proper headers
    print(f"\nSubject: {selected_email.subject_line}")
    print(f"From:\t {selected_email.email_address}")
    print(f"Date:\t {selected_email.email_date}")
    print("="*60)
    
    ''' This segment arranges a print line management to convert thr longer
        contents into the proper chunks with not more than 52 cxharacters 
        to have the best readable view:
    '''
    # exctract content's words from the email object
    content = selected_email.email_content.split()

    # while upto the remained to print is longfer than 52 chars
    while len(" ".join(content)) > 52 :
    
        line_to_print = ""
        
        for index, word in enumerate(content) :
            # build the line word by word upto no more 52 chars
            if len(line_to_print + word) < 52:
                line_to_print += word + " "

            # else means that line is filled up enough, so, print it and removes
            # from the content and break the for loop to continue by while loop   
            else:
                print(f"\t {line_to_print}")
                content = content[index: ]
                break
    
    # print the last remaind line after the while loop (<52 char2)
    print(f"\t {" ".join(content)}\n")
    
    # user notification for email marked as read
    print(f"\n >> Email from {selected_email.email_address} marked as read <<\n")
    
    return


# ============================================================================================

inbox = []
# Create three initiate emails objects
now = datetime.now()
dt_string = now.strftime("%B %d, %Y %H:%M:%S")

populate_inbox("aliailo@gmail.com", "Welcome to HyperionDev!", 
               "This is the first line of the first email content. This is the second line of the first email content. This is the third line of the first email content. This is the forthd line of the first email content."
               , dt_string)

populate_inbox("aliailo@yahoo.com", "Great work on the bootcamp!", 
               "This is the first line of the second email content. This is the second line of the second email content. This is the third line of the second email content. This is the forthd line of the second email content."
               , dt_string)
populate_inbox("aliailo@yahoo.com", "Your excellent marks!", 
               "This is the first line of the third email content. This is the second line of the third email content. This is the third line of the third email content. This is the forthd line of the third email content."
               , dt_string)

show_menu = "unread"

# providing the main menu content:
menu_content =  "Select one of the following Options below:\n"
menu_content += "==========================================\n"
menu_content += "1. Read an email\n"
menu_content += "2. View unread emails\n"
menu_content += "3. Quit application\n"
menu_content += ": "

list_emails(list_order = "all")

while True:

    # presenting the menu to the user and getting the chois
    print()
    menu = input(menu_content)

    if menu == '1':
        # call the read_email function
        read_email()
        list_emails(list_order = "all")

    elif menu == '2':
        # call the list_emails function with list_order argument as unread 
        list_emails(list_order = "unread")
        # comeback to the inbox menu and list all emails list after unread
        # emails list has been displayed
        input("\n\tPress any key to back to inbox...")
        list_emails(list_order = "all")

    elif menu == '3':
        # quit the application
        print('\nGoodbye!!!\n')
        exit()

    else:
        # in case the input value is not valid:
        print("You have made a wrong choice, Please Try again")
