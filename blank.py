#!/use/bin/python
import sqlite3 

def create_table(db_Name,table_name, sql):
    with sqlite3.connect(db_Name) as db: 
        cursor = db.cursor()
        cursor.execute("select name from sqlite_master where name=?", (table_name,))
        result = cursor.fetchall()
        keep_table = True
        if len(result) == 1:
            response = input("The table {0} already exists, do you wish to recreate it (y/n): ".format(table_name))
            if response == "y":
                print 3
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
        sql = "insert into Clothing (Style, Top, Bottom, Hair, Shoes ,Colors, Notes)  values (?,?,?,?,?,?,?)"
        cursor.execute(sql, values)
        db.commit()
        

if __name__ == "__main__":
    db_Name = "ex.db"
    sql = """create table Clothing(ClothingID text,Style text,Color text, size text,primary key(ClothingID))"""
    create_table(db_Name, "Clothing",sql)
    clothing = ("Shirt", "Pink", "Small")
    insert_data(db_Name, clothing)





