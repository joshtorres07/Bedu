import mysql.connector

cnx = mysql.connector.connect(
    host='ec2-34-219-233-69.us-west-2.compute.amazonaws.com',
    port=3306,
    user= 'root',
    password='khQ9--mp6LWq97iA',
    database='movielens'
)

cursor = cnx.cursor()

cursor.execute("SHOW TABLES")

result = cursor.fetchall()

print(result)