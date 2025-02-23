import Main_menu
import Student_Details
import mysql.connector
def DETAILS():
    while True:
                print('\t\t\t-------------WELCOME TO SCHOOL-------------')
                print('\t\t\t---------------------------------------------------')
                print('\t\t\n-------------STUDENT_DETAIL TABLE---------------------')
                print('choice 1 for inserting the data in the STUDENT_DETAILS table')
                print('choice 2 for displaying the data from STUDENT_DETAILS table')
                print('choice 3 for updating the specific  data from STUDENT_DETAILS table')
                print('choice 4 for selecting the updated value from STUDENT_DETAILS table')
                print('choice 5 for deleting the data from the STUDENT_DETAILS table from database')
                print('choice 6 for return')
                choice =int(input('Enter  a number of your choice'))
                if choice==1:
                        Student_Details.insert()
                if choice==2:
                        Student_Details.display()
                if choice ==3:
                        Student_Details.update()
                if choice==4:
                        Student_Details.select()
                if choice==5:
                        Student_Details.delete()
                if choice==6:
                        exit()
                        break
def insert():
    n=int(input('Enter any number of your choice-:'))
    print('\t\t\t-----------------------------------------')
    while n<=10:
        mysql.connector.connect(host='localhost',
                                user='root',
                                password='Prabhat2908',
                                database='school')
        mycursor=mysql.cursor()
        stud_id=int(input('Enter a Stud_id:-'))
        Nameofstudent=int(input('Enter  the name of student:-'))
        Fathersname=int(input('Enter  the fathersname:-'))
        Mothersname=int(input('Enter tha mothersname'))
        dateofbirth=input('insert a date of birth')
        my="insert into STUDENT_DETAILS value({},'{}','{}',{})".format( Stud_id,Nameofstudent,Fathersname,Mothersname,Dateofbirth)
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
         my='Select * from STUDENT_DETAILS'
         mycursor.execute(my)
         for i in mycursor:
                 print(i)
         mycursor.close()        


#updating the values in the MARKS table
def update():
        sql=mysql.connector.connect(host='localhost',
                                    user='root',
                                    password='Prabhat2908',
                                    database='school')
        mycursor=sql.cursor()
        a=int(input('Enter a your name:'))
        b=int(input('Enter a your date of birth:'))
        my='update STUDENt_DETAILS set English={} where Dateofbirth={}'.format(a,b)
        mycursor.execute(my)
        sql.commit()
        mycursor.close()

#selecting the from MARKS table
def select():
        sql=mysql.connector.connect(host='localhost',
                                user='root',
                                password=D,
                                database='school')
        mycursor=sql.cursor()
        English=int(input('Enter a English marks:'))
        my="select Stud_id,Nameofstudent,Fathersname,Mothersname,Dateofbirth from STUDENT_DETAILS where class='{}'".format(English)
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
        my='delete from STUDENT_DETAILS where Stud_id={}'.format(Stud_id)
        mycursor.execute(my)
        sql.commit()
        print('1 record deleted')
        mycursor.close()
       

# return to the main menu
def exit():
        print('RETURN TO MAIN_MENU.....')
