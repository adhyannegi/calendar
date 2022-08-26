##########################################################################
#    Computer Project #11
#    Algorithm
#        >2 functions defined.        
#        >Main function defined which uses functions from p11_calendar
#         p11_event classes. It starts off by printing the menu and asks 
#         the user for a valid option and calls function from the two classes
#         based on user input. 
##########################################################################

from p11_calendar import P11_Calendar
from p11_event import P11_Event

CAL_TYPE = ['meeting','event','appointment','other']

MENU = '''Welcome to your own personal calender.
  Available options:
    (A)dd an event to calender
    (D)elete an event
    (L)ist the events of a particular date
    (Q)uit'''

def check_time(time,duration):
    '''
    Checks if time and duration are valid
    Parameters: String, Int
    Returns: Boolean
    '''
    if ":" not in time:    #checks for valid input
        return False
    
    time_spec = time.split(":")
    hour = int(time_spec[0])
    mins = int(time_spec[1])
    #checks if valid
    if (hour in range(6, 18)) and (mins in range(0, 60)) \
        and duration in range(1, 61):
        return True
    
    return False
        
    
def event_prompt():
    '''
    Prompts for an event until a valid event is entered
    Parameters: None
    Returns: P11_Event object
    '''
    date = input("Enter a date (mm/dd/yyyy): ")
    time = input("Enter a start time (hh:mm): ")
    duration = input("Enter the duration in minutes (int): ")
    duration = int(duration)
    cal_type = input\
        ("Enter event type ['meeting','event','appointment','other']: ")
    #creating event object 
    event = P11_Event(date, time, duration, cal_type)
    #loop goes until valid
    while (check_time(time, duration) == False) or (event.valid == False):
        print("Invalid event. Please try again.")
        date = input("Enter a date (mm/dd/yyyy): ")
        time = input("Enter a start time (hh:mm): ")
        duration = input("Enter the duration in minutes (int): ")
        duration = int(duration)
        cal_type = input\
            ("Enter event type ['meeting','event','appointment','other']: ")
        event = P11_Event(date, time, duration, cal_type)
    
    return event
        
                                   
def main():
    print(MENU)
    calendar = P11_Calendar()
    option = input("Select an option: ")
    option = option.lower()
    #checking for valid option
    while option not in ["q", "a", "d", "l"]:
        print("Invalid option. Please try again.")
        option = input("Select an option: ")
        option = option.lower()
    #loop runs until user wants to quit    
    while option != "q":
        
        if option == "a":
            event = event_prompt()
            print("Add Event")       
            #checking for validity of event
            if calendar.add_event(event):
                print("Event successfully added.")
            else:
                print("Event was not added.")
            
        elif option == "d":
            print("Delete Event")
            date = input("Enter a date (mm/dd/yyyy): ")
            time = input("Enter a start time (hh:mm): ")
            #checking if deletion is valid
            val = calendar.delete_event(date, time)
            if val:
                print("Event successfully deleted.")
            else:
                print("Event was not deleted.")
            
        elif option == "l":
            print("List Events")
            date = input("Enter a date (mm/dd/yyyy): ")            
            date_list = calendar.day_schedule(date)        
            if len(date_list) > 0:
                for event in date_list:
                    print(event)                
            else:
                print("No events to list on  {}".format(date))
                    
        print(MENU)
        option = input("Select an option: ")
        option = option.lower()
        
        while option not in ["q", "a", "d", "l"]:
            print("Invalid option. Please try again.")
            option = input("Select an option: ")
            option = option.lower()
        
            
            
if __name__ == '__main__':
    main()
