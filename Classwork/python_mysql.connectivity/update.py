import mysql.connector
# To establish the connection with mysql
dataconnection=mysql.connector.connect(
    host='localhost',user='root',password='sagar2004',database='StudentManagement'
)
#To check whether it is connected or not 
print("Connected")

#Take input of student id
std_id=input("Enter Student ID :")
stu_age=int(input("Enter age of student :"))
standard=input("Enter Standard :")

#to create a cursor object
cursorobj=dataconnection.cursor()

#Writing update query
sql_query='update Student set age=%s,Standard=%s where StdId=%s'

#put the values to be inserted on tuple
values=(stu_age,standard,std_id)

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
# -----------------------------

'''
mysql> select *
    -> from Student;
+--------+---------+----------+-----+
| StdId  | StdName | Standard | age |
+--------+---------+----------+-----+
| std101 | Anil    | 11       |  16 |
+--------+---------+----------+-----+
1 row in set (0.00 sec)'''
