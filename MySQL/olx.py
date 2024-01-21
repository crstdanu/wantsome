import mysql.connector

try:
    db = mysql.connector.connect(
        host='localhost',
        user='crstdanu',
        password='MyKey99',
        database='olx'
    )
    try:
        mycursor = db.cursor()
        query = ''
        mycursor.execute(query)
        results = mycursor.fetchall()
    except mysql.connector.Error as e:
        print(f"Error executing SQL query: {e}")
    finally:
        mycursor.close()
        print("Cursor closed")

except mysql.connector.Error as error:
    print(f"There is an error {error}")
finally:
    if 'connection' and db.is_connected():
        db.close()
