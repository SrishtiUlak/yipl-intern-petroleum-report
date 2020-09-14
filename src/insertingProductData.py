from connection import create_connection

from sqlite3 import Error


def insertProductData(reportData):

    try:
        # establishing the connection for connecting the database
        conn = create_connection()
        # Creating a cursor object using the cursor() method
        c = conn.cursor()
        values = set()
        """Getting unique product names"""
        for item in reportData:
            values.add(item['petroleum_product'])
            # Preparing SQL query to INSERT a record into the database.
        for item in values:
            # Executing the SQL command for inserting values in database
            c.execute(f"INSERT INTO product(product_name) VALUES ('{item}')")

        # Commit to save the changes in the database
        conn.commit()
        print("Product data inserted successfully in database")

    except Error as e:
        print(e)

