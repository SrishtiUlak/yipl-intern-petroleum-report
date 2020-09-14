from connection import create_connection
from sqlite3 import Error


def createTable():
    # SQL command to create a table in the database

    product = """CREATE TABLE IF NOT EXISTS product (
                                            product_id integer PRIMARY KEY ,
                                            product_name text NOT NULL
                                        ); """

    sale = """CREATE TABLE IF NOT EXISTS sale (
                                        product_id integer ,
                                        amount decimal NOT NULL,    
                                        year integer NOT NULL,   
                                        PRIMARY KEY (product_id, year) ,                                                                     
                                        FOREIGN KEY (product_id) REFERENCES projects (product_id)
                                    );"""
    deleteProduct = """DELETE FROM product"""
    deleteSale = """DELETE FROM sale"""

    try:
        # read the connection parameters
        conn = create_connection()
        # Creating a cursor object using the cursor() method
        c = conn.cursor()
        # execute the statement for creating a table called product
        c.execute(product)
        print("Product Table created successfully in Database")
        # execute the statement for creating a table called sale
        c.execute(sale)
        print("Sale Table created successfully in Database")
        # execute the statement for deleting the table which is  already existed in database
        c.execute(deleteProduct)
        c.execute(deleteSale)

        # Commit to save the changes in the database
        conn.commit()


    except Error as e:
        print(e)


