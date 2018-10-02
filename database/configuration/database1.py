import psycopg2
import flask

class Databaseconnection:
    def __init__(self):

        # try:
            
            def create_tables(self):

                """ create tables in the PostgreSQL database"""

                commands = (
                    """
                    CREATE TABLE MENU (
                        Item_id SERIAL PRIMARY KEY,
                        Item VARCHAR(255) NOT NULL,
                        Price VARCHAR(255) NOT NULL
                    )
                    """,
                    """CREATE TABLE UserHistory(
                            user_id SERIAL PRIMARY KEY,
                            order_quantity VARCHAR(255) NOT NULL,
                            order_status VARCHAR(255) NOT NULL
                            
                            )
                    """,
                    """
                    CREATE TABLE userhistory (
                            part_id SERIAL PRIMARY KEY,
                            file_extension VARCHAR(5) NOT NULL,
                            drawing_data BYTEA NOT NULL
                  E
                    )
                    """,
                    """
                    CREATE TABLE vendor_parts (
                            vendor_id SERIAL NOT NULL,
                            part_id SERIAL NOT NULL,
                            PRIMARY KEY (vendor_id )
                            
                    )
                    """)
            conn = None
        except:
           print("its okay")
    
        for command in commands:
                cur.execute(command)
        # close communication with the PostgreSQL database server
                cur.close()
        # commit the changes
                conn.commit()
        else:
            print("error")     
  
if __name__ == '__main__':
    create_tables()

