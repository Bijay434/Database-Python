import pymysql
db = pymysql.connect("localhost","root","","dbpython")
cursor = db.cursor()
print("Enter username ")
username = input()
print("Enter password")
password = input()
print("Enter Email id")
email = input()
insert = "INSERT INTO `logindetails`(`username`, `password`, `email`) VALUES (%s,%s,%s)"
ins = (username, password, email) #data to be inserted1

try:
	cursor.execute(insert,ins)
	db.commit()
	print("Successful")
except:
	db.rollback()
	print(TypeError)
	print(ValueError)
	print("Exception Occured ")
finally:
	db.close()
