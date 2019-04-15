from database.mydatabase import MyDatabase, SQLITE
import classmodule


dbms = MyDatabase(SQLITE, dbname='database')

# =============================================================================
#  Option 1 - Add new location to database
# =============================================================================

def new_location():
    new_loc = classmodule.Location()
    new_loc.insert_longitude()
    new_loc.insert_latitude()
    new_loc.insert_loc_name()
    new_loc.calc_elevation()
    new_loc.save_loc()

# =============================================================================
# Option 2 - Check nearest locations from the user (requires registration - user name and location)
# =============================================================================
def user_menu():
    new_user = classmodule.User()
    new_user.add_new_user()
    new_user.loc_choose()
    new_user.loc_assign()
    dbms.add_user_to_db(new_user.first_name, new_user.last_name, new_user.id_loc)
    condition = False
    while condition == False:
        s = input("Please choose 1 or 2: \n 1. Find all locations in range \n 2. Find nearest location \n Your choice: ")
        if s == "1":
            range_l = input("Please specify the range in miles: ")
            range_l = int(range_l)
            dbms.range_loc(new_user.location[0], new_user.location[1], new_user.id_loc, range_l)
            condition = True
        elif s == "2":
            range_l = 12450 #the largest distance possible in miles
            nearest = dbms.range_loc(new_user.location[0], new_user.location[1], new_user.id_loc, range_l)
            print("The nearest location /name,longitude,latitude,distance/ found: \n", nearest)
            condition = True       
    return new_user

# =============================================================================
# Program entry point  - Dashboard
# =============================================================================
 
def main():
    condition = False
    while condition == False:
        print("\n\n Welcome to dashboard!\n Options: \n 1. Add new location \n 2. Check nearest locations \n 3. Quit")
        a = input("What to do? Please type 1, 2 or 3: ")
        if a == "1":
            new_location()
        elif a == "2":
            user_menu()
        elif a== "3":
            condition = True
        else: print("Wrong number! Please type again: ")

if __name__ == "__main__": main()

