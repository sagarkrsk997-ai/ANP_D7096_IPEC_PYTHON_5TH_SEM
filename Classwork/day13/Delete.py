import mysql.connector
# To establish the connection with mysql
dataconnection=mysql.connector.connect(
    host='localhost',user='root',password='sagar2004',database='StudentManagement'
)
#To check whether it is connected or not 
print("Connected")

#Take input of student id
std_id=input("Enter Student ID :")

#to create a cursor object
cursorobj=dataconnection.cursor()

#Writing update query
sql_query='delete from Student where StdId=%s'

#put the values to be inserted on tuple
values=(std_id,)

#to execute the query
cursorobj.execute(sql_query,values)

#To commit the changes
dataconnection.commit()

#-----------------------------------------

#To close the cursor connection
cursorobj.close()

#--------------------
#To close the connection object
dataconnection.close()

# -------------------------
'''
Enter Student ID: std103

mysql> select *
    -> from Student;
+--------+---------+----------+-----+
| StdId  | StdName | Standard | age |
+--------+---------+----------+-----+
| std101 | Anil    | 11       |  16 |
| std102 | Amit    | 11th     |  16 |
| std104 | Mohit   | 12th     |  17 |
| std105 | Rohit   | 8th      |  13 |
+--------+---------+----------+-----+
4 rows in set (0.01 sec)
'''