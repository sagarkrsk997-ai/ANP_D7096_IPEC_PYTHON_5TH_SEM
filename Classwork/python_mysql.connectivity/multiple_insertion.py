import mysql.connector
# To establish the connection with mysql
dataconnection=mysql.connector.connect(
    host='localhost',user='root',password='sagar2004',database='StudentManagement')
#To check whether it is connected or not 
print("Connected")

#to create a cursor object
cursorobj=dataconnection.cursor()

#Writing insert query
sql_query='insert into Student values(%s,%s,%s,%s)'

#----------------------
#Inserting Multiple Records 
values=[('std102','Amit','11th',16),('std103','Rahul','9th',14),('std104','Mohit','12th',17),('std105','Rohit','8th',13)]
#-----------------------------------------
#to execute the query
cursorobj.executemany(sql_query,values)

#To commit the changes
dataconnection.commit()

#-----------------------------------
#To check data inserted or not 
if (cursorobj.rowcount>0):
    print("Data inserted Sucessfully")
else:
    print("Data not inserted")
#-----------------------------------------

#To close the cursor connection
cursorobj.close()

#--------------------
#To close the connection object
dataconnection.close()

# ----------------------

'''
mysql> select *
    -> from Student;
+--------+---------+----------+-----+
| StdId  | StdName | Standard | age |
+--------+---------+----------+-----+
| std101 | Anil    | 11       |  16 |
| std102 | Amit    | 11th     |  16 |
| std103 | Rahul   | 9th      |  14 |
| std104 | Mohit   | 12th     |  17 |
| std105 | Rohit   | 8th      |  13 |
+--------+---------+----------+-----+
5 rows in set (0.01 sec)
'''