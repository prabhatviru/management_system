import Main_menu
import Nameofschool
import mysql.connector
def SCHOOLMENU():
        while True:
                print('\t\t\t-------------WELCOME TO SCHOOL-------------')
                print('\t\t\t---------------------------------------------------')
                print('\t\t\n-------------NAMEOFSCHOOL TABLE-------------')
                print('choice 1 for inserting the data in the Nameofschool table')
                print('choice 2 for displaying the data from Nameofschool table')
                print('choice 3 for updating the specific  data from Nameofschool table')
                print('choice 4 for selecting the updated value from Nameofschool table')
                print('choice 5 for deleting the data from the Nameofschool table from database')
                print('choice 6 for return')
                choice =int(input('Enter  a number of your choice'))
                if choice==1:
                        Nameofschool.insert()
                elif choice==2:
                        Nameofschool.display()
                elif choice ==3:
                        Nameofschool.update()
                elif choice==4:
                        Nameofschool.select()
                elif choice==5:
                        Nameofschool.delete()
                elif choice==6:
                        exit()
                        break

# insering the value in the NAMEOFSCHOOL table
def insert():
        n=int(input('Enter any number of your choice-:'))
        print('\t\t\t-----------------------------------------')
        while n<=10:
                mysql.connector.connect(host='localhost',
                                        user='root',
                                        password='Prabhat2908',
                                        database='school')
                mycursor=mysql.cursor()
                Stud_id=int(input('Enter a Stud_id:-'))
                Nameofschool=input('Enter a nameof school:-')
                Location_of_School=input('Enter the location of your school:-')
                Phone_No=int(input('enter the phone no. of your school:-'))
                my="insert into NAMEOFSCHOOL value({},'{}','{}',{})".format(Stud_id,Nameofschool,Location_of_school,Phone_No)
                cursor.execute(my)
                mysql.commit()
                print(cursor.rowcount,'record has inserted')
                print('record saved')
                n+=1
                mycursor.close()

#displaying the vlaue from the NAMEOFSCHOOL table
def display():
         sql=mysql.connector.connect(host='localhost',
                                    user='root',
                                    password='Prabhat2908',
                                    database='school')
         mycursor=sql.cursor()
         my='Select * from NAMEOFSCHOOL'
         mycursor.execute(my)
         for i in mycursor:
                 print(i)
         mycursor.close()        

#
def update():
        sql=mysql.connector.connect(host='localhost',
                                    user='root',
                                    password='Prabhat2908',
                                    database='school')
        mycursor=sql.cursor()
        a=int(input('Enter a Phone no:'))
        b=int(input('Enter a Stud_id:'))
        my='update NAMEOFSCHOOL set Phone_No={} where Stud_id={}'.format(a,b)
        mycursor.execute(my)
        sql.commit()
        mycursor.close()

#
def delete():
       sql=mysql.connector.connect(host='localhost',
                                    user='root',
                                    password='Prabhat2908',
                                    database='school')
       mycursor=sql.cursor()
       Stud_id=int(input('Enter a Stud_id :'))
       my='delete from NAMEOFSCHOOL where Stud_id={}'.format(Stud_id)
       mycursor.execute(my)
       sql.commit()
       print('1 record deleted')
       mycursor.close()
#
def select():
        sql=mysql.connector.connect(host='localhost',
                                user='root',
                                password=D,
                                database='school')
        mycursor=sql.cursor()
        Phone_no=int(input('Enter the class-:'))
        my="select  Stud_id,Nameofschool, Location_Of_School,Phone_No from NAMEOFSCHOOL where class='{}'".format(Phone_no)
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
        my='delete from NAMEOFSCHOOL where Stud_id={}'.format(Stud_id)
        mycursor.execute(my)
        sql.commit()
        print('1 record deleted')
        mycursor.close()
       

# return to the main menu
def exit():
        print('RETURN TO MAIN_MENU.....')
