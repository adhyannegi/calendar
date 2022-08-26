##########################################################################
#    Computer Project #11
#    Algorithm
#        >8 functions defined in P11_Event class.         
#        >__init__() function initalizes all the values for the class,
#         get_date() and get_time() functions return the date and time 
#         respectively, get_time_range() calculates and returns the
#         start time and end time as a tuple and __str__() returns
#         data of the class as a string.
##########################################################################

CAL_TYPE = ['meeting','event','appointment','other']

class P11_Event():
    def __init__(self,date=None,time='9:00',duration=60,cal_type='meeting'):
        '''
        Initalizes all values for the object
        Parameters: Object, String, String, Int, String
        Returns: Nothing
        '''
#
        if date is not None:
            #checking validity
            if "/"  not in date:
                self.date = None
            
            else:
                #splitting into data
                date_spec = date.split("/")
                month = int(date_spec[0])
                day = int(date_spec[1])
                year = int(date_spec[2])
                
                if (((month >= 1) and month <= 12) and ((day >= 1) and \
                        (day <= 31)) and ((year >= 0) and (year <= 9999))):
                    self.date = date
                    
                else:
                    self.date = None
        
        else:
            self.date = None
        #checking for validity
        if ":" not in time:
            self.time = None
            
        else:
            #splitting into data
            time_spec = time.split(":")
            hour = int(time_spec[0])
            mins = int(time_spec[1])
    
            if (((hour >= 0) and (hour <= 23)) and ((mins >= 0) and \
                                                    (mins <= 59))):                
                self.time = time
            
            else:
                self.time = None
        #type of duration must be int
        if type(duration) != int:
            self.duration = None
        
        else:
            if duration >= 0:
                self.duration = duration
            
            else:
                self.duration = None
           
        if cal_type in CAL_TYPE:
            self.cal_type = cal_type
        
        else:
            self.cal_type = None
        #checking if all data is valid or not   
        if (self.date is not None) and (self.time is not None) and \
            (self.duration is not None) and (self.cal_type is not None):
            self.valid = True
        
        else:
            self.valid = False        
    
    def get_date(self):
        '''
        Returns date
        Parameters: Object
        Returns String
        '''
        return self.date
    
    def get_time(self):
        '''
        Returns Time
        Parameters: Object
        Returns: String
        '''
        return self.time
    
    def get_time_range(self):
        '''
        Calculates start time and end time
        Parameters: Object
        Returns: Tuple
        '''
        time_spec = self.time.split(":")
        #calculating start time and end time
        start_time = int(time_spec[0]) * 60 + int(time_spec[1])
        end_time = start_time + int(self.duration)
        return (start_time, end_time)
                      
    def __str__(self):
        '''
        Returns String based on object values
        Parameter: Object
        Returns String
        '''
        #all have to be not none to print string with data
        if (self.date is None) or (self.time is None) or \
            (self.duration is None):
            return "None"
        
        return self.date + ": start: " + self.time + "; duration: " + \
            str(self.duration)
    
    def __repr__(self):
        if self.date and self.time and self.duration:
            return self.date + ';' + self.time + '+' + str(self.duration)
        else:
            return 'None'

    def __lt__(self,e):
        '''
        Compares self object time with e object time
        Parameter: Object, Object
        Returns: Boolean
        '''
        #if data is invalid
        if (self.time is None) or (e.time is None):
            return False
        #splitiing and calcultin time for both objects
        self_time = self.time.split(":")
        self_min = (int(self_time[0])*60) + int(self_time[1])
        e_time = e.time.split(":")
        e_min = (int(e_time[0])*60) + int(e_time[1])
        return self_min < e_min
        
    def __eq__(self,e):
        '''PROVIDED'''
        return self.date == e.date and self.time == e.time and \
            self.duration == e.duration and \
                self.cal_type == e.cal_type # and self.status == e.status

        
