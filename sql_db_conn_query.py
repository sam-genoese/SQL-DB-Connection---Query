#   import modules
import sqlite3
import pandas as pd
import os
import os.path
#   create variable for database files' parent directory
db_root = r"C:\Users\...\Databases" #   Update to appropriate directory
#   create an empty dictionary
db_dict = {}
#   create function to populalate the dictionary
def create_db_dict():
    #   walks the database files' children directories
    for root, dir, files in os.walk(db_root):
        for db in files:
            #   if a file ends with ".db"...
            if db.endswith(".db"):
                #   add the file name (key) and directory path (value) to the dictionary
                db_dict[db] = root
    return db_dict
create_db_dict()
db_dict
#   define function that will connect to SQL database file (.db)
def connect_db(name):
    #   "name" is concatenation of user input and ".db"
    name = str(name + ".db")
    #   variable created to reference correct working directory for database file acquired from database dictionary with user input
    db_directory = str(db_dict[name])
    #   change the directory to "db_directory" variable
    os.chdir(db_directory)
    #   define variable "connection" as global so it will be recognized when closing database connection later
    global connection
    #   if file indicated exists in the directory defined above...
    if os.path.exists(name):
        #   connect to database file and print "CONNECTION SUCCESSFUL"
        connection = sqlite3.connect(name)
        print("CONNECTION SUCCESSFUL")
    else:
        print("CONNECTION FAILED")
connect_db("northwind")
#   define function to query database as "query"
def query():
    #   define user input SQLite query as "q"
    q = input()
    #   user input "q" is run via established database connection and converted to a DataFrame
    df = pd.read_sql_query(q, connection)
    #   print user input SQLite query
    print(q)
    #   retun SQLite query output
    return df
#   will display a text box when "query()" is run
#   input SQLite query into text box, ex:
    #   SELECT * FROM artists LIMIT 10
query()
#   define function to close the connection to SQLite database
def close(connection):
    connection.close()
    print("CONNECTION TERMINATED")
close(connection)