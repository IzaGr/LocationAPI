from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, Float, ForeignKey
from math import sqrt, radians, cos, acos, sin, pow, ceil

# Global Variables
SQLITE          = 'sqlite'

# Table Names
LOCATION        = 'locations'
USERS           = 'users'


class MyDatabase:
    DB_ENGINE = {
            SQLITE:'sqlite:///database.db',   
        }
    
    # Main DB Connection Ref Obj
    db_engine = None
    
    def __init__(self, dbtype='SQLITE', username='', password='', dbname=''):
        dbtype = dbtype.lower()
        
        if dbtype in self.DB_ENGINE.keys():
            engine_url = self.DB_ENGINE[dbtype].format(DB=dbname)
            
            self.db_engine = create_engine(engine_url)
        else:
            print("DBType is not found in DB_ENGINE")
            
    def create_db_tables(self):
        metadata = MetaData()
        location = Table(LOCATION, metadata,
                        Column('id', Integer, primary_key=True),
                        Column('name', String),
                        Column('longitude', Float, nullable=False),
                        Column('latitude', Float, nullable=False),
                        Column('elevation', Float, nullable=False),
                        )        
        users = Table(USERS, metadata,
                      Column('id', Integer, primary_key=True, autoincrement=True),
                      Column('first_name', String),
                      Column('last_name', String),
                      Column('location_id', None, ForeignKey('locations.id')),    
                      )


        try:
            metadata.create_all(self.db_engine)
            print("Tables created")
        except Exception as e:
            print("Error occurred during Table creation!")
            print(e)  
    

    def execute_query(self, query=''):
        if query == '' : return
        with self.db_engine.connect() as connection:
            try:
                connection.execute(query)
            except Exception as e:
                print(e)
 

    def show_locs(self, query=''):
        query = query if query != '' else "SELECT * FROM '{}';".format(LOCATION)
        
        with self.db_engine.connect() as connection:
            try:
                result = connection.execute(query)
            except Exception as e:
                print(e)
            else:
                for row in result:
                    print(row) 
                result.close()
        print("\n")



    def assign_exist_loc(self):            
        query = "SELECT id FROM '{}';".format(LOCATION)
        id_list=[]
        with self.db_engine.connect() as connection:
            try:
                result = connection.execute(query)
            except Exception as e:
                print(e)
            else:
                for row in result:
                    id_list.append(row[0]) 
                result.close()                                                                      
        condition = False
        while condition == False:
            id_loc = input('What is the id of your location: ')
            try: 
                id_loc = int(id_loc)
                if id_loc in id_list:
                    condition = True
                    self.loc_params(id_loc)
                    return id_loc
                else: print("Wrong id! Try again:")
            except ValueError:
                print("Wrong id! Id must be integer")
        
        
    def loc_params(self,id_loc):
        query = "SELECT longitude, latitude, elevation from {} WHERE id={id};".format(LOCATION, id=id_loc)
        loc=[]
        with self.db_engine.connect() as connection:
            try:
                result = connection.execute(query)
                for row in result:
                    loc.append(row) 
                result.close()
                location = loc[0]
                return location
            except Exception as e:
                print(e)
    
    def save_location(self, loc_name,long,lati,elev):
        query = "INSERT INTO LOCATIONS (name, longitude, latitude, elevation) "\
                "VALUES ('{}',{},{},{});".format(loc_name,long,lati,elev)
        self.execute_query(query)
        print ("New location saved")
        self.last_id()
    
        
        
    def last_id(self):  
        query = "SELECT id FROM LOCATIONS ORDER BY id DESC LIMIT 1;"       
        last_id=[]
        with self.db_engine.connect() as connection:
            try:
                result = connection.execute(query)
                for row in result:
                    last_id.append(row[0]) 
                result.close()
                id_loc = last_id[0]
                return id_loc
            except Exception as e:
                print(e)
    
    
    def add_user_to_db(self, first_n, last_n, id_loc): 
        query = "INSERT INTO USERS (first_name, last_name, location_id) VALUES ('{}','{}',{});".format(first_n, last_n, id_loc)
        with self.db_engine.connect() as connection:
            try:
                connection.execute(query)
                print("User successfully added to database")
            except Exception as e:
                print(e)
                
    def range_loc(self, user_lati, user_long, user_loc_id, range_l):           
        raw_con = self.db_engine.raw_connection()
        raw_con.create_function("cos", 1, cos)
        raw_con.create_function("acos", 1, acos)
        raw_con.create_function("sin", 1, sin)
        raw_con.create_function("radians", 1, radians)
        raw_con.create_function("sqrt", 1, sqrt)
        raw_con.create_function("pow", 2, pow)
        raw_con.create_function("ceil",1,ceil)
        
        try:
            cursor = raw_con.cursor()
            cursor.execute('SELECT name, longitude, latitude,CEIL(SQRT( '
                'POW(69.1 * (latitude - {}), 2) + '
               'POW(69.1 * ({} - longitude) * COS(latitude / 57.3), 2))) AS distance '
                'FROM LOCATIONS WHERE distance < {} AND id != {} ORDER BY distance;'.format(user_lati, user_long, range_l, user_loc_id))
            results = cursor.fetchall()
            nearest = results[0]
            print("All found locations /name,longitude,latitude,distance/ in specified range:" , results)
            cursor.close()
        finally:
            raw_con.close()
        return nearest