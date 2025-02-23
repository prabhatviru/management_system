import Main_menu
import Student
import mysql.connector
import random as rd
D="Prabhat2908"
def STUDENT_MENU():
        while True:
                print('\t\t\t-------------WELCOME TO SCHOOL-------------')
                print('\t\t\t---------------------------------------------------')
                print('\t\t\n-------------STUDENT TABLE---------------------')
                print('choice 1 for inserting the data in the student table')
                print('choice 2 for displaying the data from student table')
                print('choice 3 for updating the specific  data from student table')
                print('choice 4 for selecting the updateed value from the saql database')
                print('choice 5 for deleting the data from the student table from database')
                print('choice 6 for return')
                choice =int(input('Enter  a number of your choice'))
                if choice==1:
                        Student.insert()
                elif choice==2:
                        Student.display()
                elif choice ==3:
                        Student.update()
                elif choice==4:
                        Student.select()
                elif choice==5:
                        Student.delete()
                elif choice==6:
                        exit()
                        break
#inserting the value in the STUDENT table
def insert():
        n=int(input('Enter Any Number of your choice-:'))
        print('\t\t\t-.-.-.-.-.-.-.-.-.-.-.-.-.-.-')
        while n<=10:
                sql=mysql.connector.connect(host='localhost',
                                        user='root',
                                        password='Prabhat2908',
                                        database='school')
                mycursor=sql.cursor()
                Stud_id=int(input('Enter a Stud_id :'))
                NameofStudent=input('Enter a name :')
                Class=int(input('Enter a Class :'))
                Rollno=int(input('Enter a Rollno :'))
                Section=input('Enter a Letter :')    
                Address=input('Enter a  Address :')
                my="insert into STUDENT value({},'{}',{},{},'{}','{}')".format(Stud_id,NameofStudent,Class,Rollno,Section,Address)
                mycursor.execute(my)
                sql.commit()
                print(mycursor.rowcount,'record has inserted')
                print('record saved')
                n=+1

# displaying the value from the STUDENT table
def display():
        sql=mysql.connector.connect(host='localhost',
                                    user='root',
                                    password=D,
                                    database='school')
        mycursor=sql.cursor()
        my='Select * from STUDENT'
        mycursor.execute(my)
        for i in mycursor:
                print(i)
        mycursor.close()
        

# updateing the value form the STUDENT table
def update():
        sql=mysql.connector.connect(host='localhost',
                                user='root',
                                password=D,
                                database='school')
        mycursor=sql.cursor()
        address=input('Enter your Address :')
        Stud_id=int(input('Enter a Stud_id :'))
        my="update STUDENT set Address='{} where Stud_id={}'".format(address)
        mycursor.execute(my)
        sql.commit()
        print('1 record updated')
        mycursor.close()
        

def select():
        sql=mysql.connector.connect(host='localhost',
                                user='root',
                                password=D,
                                database='school')
        mycursor=sql.cursor()
        Class=int(input('Enter the class-:'))
        my="select Nameofstudent,Class,Rollno,Address from STUDENT where class='{}'".format(Class)
        mycursor.execute(my)
        for i in mycursor:
                print(i)
        print('record selected')
        

# deleting the value from the STUDENT table
def delete():
        sql=mysql.connector.connect(host='localhost',
                                    user='root',
                                    password=D,
                                    database='school')
        mycursor=sql.cursor()
        Stud_id=int(input('Enter a Stud_id :'))
        my='delete from STUDENT where Stud_id={}'.format(Stud_id)
        mycursor.execute(my)
        sql.commit()
        print('1 record deleted')
        mycursor.close()
       

# return to the main menu
def exit():
        print('RETURN TO MAIN_MENU.....')
                
                
                
                
