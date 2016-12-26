#!/use/bin/python
import sqlite3

####FUNCTIONS DEFINED 
##create table
##insert data
##update look
##remove look 
##show all looks 

def create_table(db_Name,table_name, sql):
    with sqlite3.connect(db_Name) as db: 
        cursor = db.cursor()
        cursor.execute("select name from sqlite_master where name=?", (table_name,))
        result = cursor.fetchall()
        keep_table = True
        if len(result) == 1:
            response = input("The table {0} already exists, do you wish to recreate it (y/n): ".format(table_name))
            if response == "y":
                keep_table = False
                print ("The {0} table will be recreated - all existing data will be lost.".format(table_name))
                cursor.execute("drop table if exists {0}".format(table_name))
                db.commit()
            else:
                print("The existing table was kept.")
        else:
            keep_table = False
        if not keep_table:
            cursor.execute(sql)
            db.commit

def insert_data(db_Name, values):
    with sqlite3.connect(db_Name) as db:
        cursor = db.cursor()
        sql = "insert into Looks (Style, Top, Bottom, Shoes, Hair ,Colors, Notes)  values (?,?,?,?,?,?,?)"
        cursor.execute(sql, values)
        db.commit()
        
def update_look(db_Name, data):
    with sqlite3.connect(db_Name) as db:
        cursor = db.cursor()
        sql = "update Looks set Style = ?, Top = ?, Bottom = ?, Shoes = ?, Hair = ?, Colors = ?, Notes = ?"
        cursor.execute(sql, data)
        db.commit() 

def remove_look(db_Name, data):
    with sqlite3.connect(db_Name) as db:
        cursor = db.cursor()
        sql ="delete from Looks where Style = ?"
        cursor.execute(sql,data)
        db.commit()

def query(db_name, sql, data):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute("PRAGMA Foreign_Keys = ON")
        cursor.execute(sql, data)
        result = cursor.fetchall()
        db.commit()
        return result

def show_all_looks(db_Name, table_name):
    "show all the data of table from db"
    sql = "SELECT * FROM {0}".format(table_name)
    return query(db_Name, sql, ())


def print_table(result):
    "show the data in a table"
    print("""
        |{0:^5s}|{1:^13s}|{2:^10s}|{3:^10s}|{4:^10s}|{5:^12s}|{6:^20s}|{7:^20s}|
        """.format("Outfit ID",
                   "Style",
                   "Top",
                   "Bottom",
                   "Shoes",
                   "Hair",
                   "Colors",
                   "Notes"))
    for entry in result:
        outfitID, Style, Top, Bottom, Shoes, Hair, Colors, Notes = entry
        print("""
        {0:^5d} {1:^13s} {2:^10s} {3:^10s} {4:^10s} {5:^12s} {6:^20s} {7:^20s}
            """.format(outfitID,
                       Style,
                       Top,
                       Bottom,
                       Shoes,
                       Hair,
                       Colors,
                       Notes))


if __name__ == "__main__":
    db_Name = "looks_inventory.db"
    sql = """create table Looks(outfitID integer,Style text, Top text, Bottom text, Shoes text, Hair text, Colors text, Notes text, primary key(outfitID))"""
    create_table(db_Name, "Looks",sql)
    look = ("Casual", "Black Turtle Neck Elbow Length", "Brown Cargo Style", "Black Roshe Nikes", "Bun", "Black, Brown", "Safari look")
    insert_data(db_Name, look)
    data = ("Casual Attire", "Black Turtle Neck Elbow Length", "Brown Cargo Style", "Black Roshe Nikes", "Bun", "Black, Brown", "Safari look")
    update_look(db_Name, data)
    result = show_all_looks(db_Name, "Looks")
    print_table(result)







