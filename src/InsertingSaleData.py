from gettingProductData import getProductData
from connection import create_connection
from sqlite3 import Error


def insertSaleData(reportData):
    try:
        """Getting values form product data"""
        productList = getProductData()
        # establishing the connection for connecting the database
        conn = create_connection()
        # Creating a cursor object using the cursor() method
        c = conn.cursor()

        for item in reportData:
            """Getting Product ID using Product Name"""
            productId = next((x for x in productList if x[1] == item['petroleum_product']))[0]
            # Executing the SQL command for inserting values in database
            c.execute(
                f"INSERT INTO sale(product_id, amount, year)"
                f" VALUES ({productId},{float(item['sale'])}, {int(item['year'])} )")
        # Commit to save the changes in the database
        conn.commit()
        print("Sale data inserted successfully in database")

    except Error as e:
        print(e)
