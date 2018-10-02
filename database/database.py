import flask
import psycopg2 #driver that helps python communicate with postgres
from pprint import pprint


class DatabaseConnection:
    def __init__(self):
        try:
            self.connection= psycopg2.connect("dbname='api_database' user='postgres' host='localhost' password='admin123'")
            self.autocommit=True #allows you to autoquantity commit.
            self.cursor=self.connection.cursor()
        except:
            pprint("try Again")

    def table_creation(self):
        table_creation_command= "CREATE TABLE Menu(order_id INT PRIMARY KEY,item_ordered TEXT NOT NULL,quantity_ordered INT NOT NULL ,price INT NOT NULL )"
        self.cursor.execute(table_creation_command)

    def create_record(self):
        new_rec=(1,"burger","34","3400")
        command_insertion="INSERT INTO Menu(order_id,item_ordered,quantity_ordered,price) VALUES("'+new_rec[0]+'",""'+new_rec[1]+'" "'+new_rec[2]+'" "'+new_rec[3]+'")"

    def query_all(self,order_id):
        self.order_id = order_id
        self.cursor.fetchall()
        for m in ms:
            pprint ("user_id:{0}".format(m))

    def update(self):
        update_cmd="UPDATE Menu set price=400 where quantity_ordered>2"
        self.cursor.execute(update_cmd)



            
if __name__== '__main__':

    db_connection= DatabaseConnection()
    tbl_creation=DatabaseConnection.table_creation
    rcd_creation=DatabaseConnection.create_record
    qry_all=DatabaseConnection.query_all()
    DatabaseConnection.update()




