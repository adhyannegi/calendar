##########################################################################
#    Computer Project #11
#    Algorithm
#        >5 functions defined in P11_Calendar() class.  
#        >The class has functions that initalizes the variables for the class
#         adds an evenbt to the event list, deletes an event from the 
#         event list and also creates a list for a specific date.
##########################################################################

from p11_event import P11_Event
class P11_Calendar():
    def __init__(self):
        '''
        Initializes event list
        Parameters: Object
        Returns: Nothing
        '''
        self.event_list = []
        
    def add_event(self,e):
        '''
        Tries to add event to event list
        Parameters: Object, Object
        Returns: Boolean
        '''
        #empty list, add straightaway
        if self.event_list == []:
            self.event_list.append(e)
            return True 
        
        tuple1 = P11_Event.get_time_range(e)
        #start and end time from tuple
        start1 = tuple1[0]
        end1 = tuple1[1]
        for i in self.event_list:
            tuple2 = P11_Event.get_time_range(i)
            start2 = tuple2[0]
            end2 = tuple2[1]
            #checking if time clashes
            if P11_Event.get_date(e) == P11_Event.get_date(i):
                if start1 in range(start2, end2+1) or end1 in \
                    range(start2, end2+1):
                    return False
        
        self.event_list.append(e)
        return True          
    
    def delete_event(self,date,time):
        '''
        Deletes event at specified date and time
        Parameters: Object, String, String
        Returns: Boolean
        '''
        for event in range(len(self.event_list)):
            #finding corect value to delete
            if (P11_Event.get_date(self.event_list[event]) == date) and \
                (P11_Event.get_time(self.event_list[event]) == time):
                del self.event_list[event]
                return True            
        
        return False
        
    def day_schedule(self,date):
        '''
        Returns list of events on a particular date
        Parameters: Object, String
        Returns: List
        '''
        list1 = []
        for i in self.event_list:
            #only items which have the same date
            if P11_Event.get_date(i) == date:
                list1.append(i)
        
        return sorted(list1)
                                
    def __str__(self):
        '''
        Returns a string that has an event on each line
        Parameters: Object
        Returns: String
        '''
        str1 = ""
        for i in self.event_list:
            #storing all data in a string
            str1 += "{}\n".format(str(i))
        return 'Events in Calendar:\n' + str1
    
    def __repr__(self):
        s = ''
        for e in self.event_list:
            s += e.__repr__() + ";"
        return s[:-1]
    
    def __eq__(self,cal):
        '''PROVIDED: returns True if all events are the same.'''
        if not isinstance(cal,P11_Calendar):
            return False
        if len(self.event_list) != len(cal.event_list):
            return False
        L_self = sorted(self.event_list)
        L_e = sorted(cal.event_list)
        for i,e in enumerate(L_self):
            if e != L_e[i]:
                return False
        return True
        
