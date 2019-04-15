from database.mydatabase import MyDatabase, SQLITE, USERS, LOCATION


import classmodule
dbms = MyDatabase(SQLITE, dbname='database')



def add_new():
    new_user = classmodule.User()
    new_user.add_new_user()
    new_user.loc_choose()
    #new_user.save_db()
    dbms.add_user_to_db(new_user.first_name, new_user.last_name, new_user.id_loc)

    return new_user
        

def new_location():
    new_loc = classmodule.Location()
    new_loc.insert_longitude()
    new_loc.insert_latitude()
    new_loc.insert_loc_name()
    new_loc.calc_elevation()
    new_loc.save_loc()

# Program entry point   
def main():
    condition = False
    while condition == False:
        print("\n\n Welcome to dashboard!\n Options: \n 1. Add new location \n 2. Check nearest locations \n 3. Quit")
        a = input("What to do? Please type 1, 2 or 3: ")
        if a == "1":
            new_location()
        elif a == "2":
            add_new()
        elif a== "3":
            condition = True
        else: print("Wrong number! Please type again: ")

if __name__ == "__main__": main()

