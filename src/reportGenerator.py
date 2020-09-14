from connection import create_connection
import pandas as pd


def generatingReport():
    # connect withe the myTable database
    connection = create_connection()
    # Creating a cursor object using the cursor() method
    cursor = connection.cursor()
    # execute the command to fetch all the data from the table emp
    cursor.execute("Select  p.product_name, MIN(year) ||  '-' ||  MAX(year) as yearRange, MIN(amount), MAX(amount), AVG(amount) "
                   "FROM product p JOIN sale s "
                   "WHERE s.product_id = p.product_id "
                   "GROUP BY CAST ((year/5) AS INT),  p.product_name "
                   "Order by  product_name, yearRange desc ")

    # store all the fetched data in the ans variable
    query = cursor.fetchall()

    df = pd.DataFrame(query, columns=['Product', 'Year', 'Min', 'Max', 'Avg'])
    print(df)

    # Since we have already selected all the data entries
    # using the "SELECT *" SQL command and stored them in
    # the ans variable, all we need to do now is to print
    # out the ans variable
    return query

    cursor.close()
    connection.close()
