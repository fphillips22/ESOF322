import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="user",
    passwd="password",
    database = "coldCases"
)
#cursor object
cursorObject = database.cursor()
dataTest = """CREATE TABLE TEST(
                NAME VARCHAR(20))"""
#creating our database
cursorObject.execute("CREATE DATABASE coldcases")
