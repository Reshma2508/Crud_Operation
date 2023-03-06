import mysql.connector

class DBconn:
    def __init__(self):

        try:
            self.conn = mysql.connector.connect(host="localhost",user="root",password="",database="person")

            self.mycursor = self.conn.cursor()
        except:
            print("Unable to establish Connection ")
        else:
            print("DB connection succesfull")

    def register(self,name,email,password):
        try:
            self.mycursor.execute("""
            INSERT INTO `student_info` (`id`, `name`, `email`, `password`) VALUES (NULL, '{}', '{}', '{}')
            """.format(name,email,password))
            self.conn.commit()
        except:
            return -1
        else:
            return 1
    def login(self,email,password):
        try:
            self.mycursor.execute("""
            select * from student_info where email like '{}' and password like '{}'
             """.format(email,password))
            info=self.mycursor.fetchall()
            return info




        except:
            print("Invalid password/ email ")






