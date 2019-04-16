from database.mydatabase import MyDatabase
from funcmodule import elevation

# =============================================================================
# User creation with user data and user location
# =============================================================================

class User(MyDatabase):
           
    def __init__(self):
        self.first_name = None
        self.last_name = None
        self.id_loc = None
        self.location = None
        
    def add_new_user(self):
        self.first_name =input('Your first name: ')
        self.last_name = input('Your last name: ')
        return None
             
    def assign_new_loc(self):  
        #  Assigning new location to the user
        condition = False
        while condition == False:
            long = input('Insert your location. Your location longitude: ')
            try:
                long = float(long)
                if -180.0 <= long <= 180.0: 
                    condition = True
                else: print("Longitude must be number in range (-180,180)")
            except:
                print("Longitude must be number in range (-180,180)")
        condition = False        
        while condition == False:
            lati = input('Insert your location latitude: ')
            try:
                lati = float(lati)
                if -180.0 <= lati <= 180.0:  
                    condition = True
                else: print("Latitude must be number in range (-90,90)")
            except:
                print("Latitude must be number in range (-90,90)")
        
        loc_name = input('Your location name: ')
        elev = elevation(long, lati)
        s = MyDatabase()
        s.save_location(loc_name,long,lati,elev)
        self.id_loc = s.last_id()
        
        return self.id_loc
    
    def loc_choose(self): 
        # Choosing existing location from database and assigning to the user
        condition = False
        while condition == False:
            choice = input('Add your location. New or Existing location (N/E): ')
            if choice is 'E':
                t = MyDatabase()
                t.show_locs()              
                self.id_loc = t.assign_exist_loc()
                condition = True
                return self.id_loc
            elif choice is 'N':
                self.assign_new_loc()
                condition = True
            else: 
                print ('Wrong selection! Type letter N or E:') 
                
                
    def loc_assign(self):
         s = MyDatabase()
         self.location=s.loc_params(self.id_loc)
         return self.location

# =============================================================================
# New location creation and saving on database
# =============================================================================
          
class Location(MyDatabase):
    
    def __init__(self):
        self.name = None
        self.latitude = None
        self.longitude = None
        self.elevation = None
    
    def insert_longitude(self):
        condition = False
        while condition == False:
            long = input('Insert new location. The location longitude: ')
            try:
                self.longitude = float(long)
                if -180.0 <= self.longitude <= 180.0: 
                    condition = True
                else: print("Longitude must be number in range (-180,180)")
            except:
                print("Longitude must be number in range (-180,180)")
        return self.longitude

    def insert_latitude(self):              
        condition = False        
        while condition == False:
            lati = input('Insert new location latitude: ')
            try:
                self.latitude = float(lati)
                if -90.0 <= self.latitude <= 90.0 : 
                    condition = True
                else: print("Latitude must be number in range (-90,90)")
            except:
                print("Latitude must be number in range (-90,90)")
        return self.latitude
        
    def insert_loc_name(self):         
        self.name = input('Insert new location name: ')
        return self.name
    
    def calc_elevation(self): 
        self.elevation = elevation(self.longitude, self.latitude)
        return self.elevation
        
    def save_loc(self):
        try:
            s = MyDatabase()
            s.save_location(self.name,self.longitude,self.latitude,self.elevation)
        except:
            print("Something went wrong with saving new location")
    
    