from connection import create_connection
from sqlite3 import Error

database = "petroReport.db"


def getProductData():
    try:
        # establishing the connection for connecting the database
        conn = create_connection()

        # Creating a cursor object using the cursor() method
        cur = conn.cursor()

        # Executing the SQL command to get product
        cur.execute("SELECT * FROM product")

        # Use fetchall()
        return cur.fetchall()

    except Error as e:
        print(e)
