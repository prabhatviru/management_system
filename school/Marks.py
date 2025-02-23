import Main_menu
import Marks
import mysql.connector
def STUDENT_MARKS():
    while True:
                print('\t\t\t-------------WELCOME TO SCHOOL-------------')
                print('\t\t\t---------------------------------------------------')
                print('\t\t\n-------------MARKS TABLE---------------------')
                print('choice 1 for inserting the data in the Marks table')
                print('choice 2 for displaying the data from Marks table')
                print('choice 3 for updating the specific  data from Marks table')
                print('choice 4 for selecting the updated value from Marks table')
                print('choice 5 for deleting the data from the Marks table from database')
                print('choice 6 for return')
                choice =int(input('Enter  a number of your choice'))
                if choice==1:
                        Marks.insert()
                if choice==2:
                        Marks.display()
                if choice ==3:
                        Marks.update()
                if choice==4:
                        Marks.select()
                if choice==5:
                        Marks.delete()
                if choice==6:
                        exit()
                        break

# insering the value in the MARKS table
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
                english=int(input('Enter  your English marks:-'))
                maths=int(input('Enter  your Maths marks:-'))
                science=int(input('Enter your Science marks'))
                total=sum([English,Maths,Science])
                my="insert into NAMEOFSCHOOL value({},'{}','{}',{})".format(Stud_id,English,Maths,Science,Total)
                cursor.execute(my)
                mysql.commit()
                print(cursor.rowcount,'record has inserted')
                print('record saved')
                n+=1
                mycursor.close()

#displaying the vlaue from the MARKS table
def display():
         sql=mysql.connector.connect(host='localhost',
                                    user='root',
                                    password='Prabhat2908',
                                    database='school')
         mycursor=sql.cursor()
         my='Select * from MARKS'
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
        a=int(input('Enter a English marks:'))
        b=int(input('Enter a Stud_id:'))
        my='update MARKS set English={} where Stud_id={}'.format(a,b)
        mycursor.execute(my)
        sql.commit()
        mycursor.close()



        
def select():
        sql=mysql.connector.connect(host='localhost',
                                user='root',
                                password=D,
                                database='school')
        mycursor=sql.cursor()
        English=int(input('Enter a English marks:'))
        my="select   Stud_id,English,Maths,Science,Total from MARKS where class='{}'".format(English)
        mycursor.execute(my)
        for i in mycursor:
                print(i)
        print('record selected')
        

#deleting the specific data form the MARKS table
def delete():
        sql=mysql.connector.connect(host='localhost',
                                    user='root',
                                    password=D,
                                    database='school')
        mycursor=sql.cursor()
        Stud_id=int(input('Enter a Stud_id :'))
        my='delete from MARKS where Stud_id={}'.format(Stud_id)
        mycursor.execute(my)
        sql.commit()
        print('1 record deleted')
        mycursor.close()
       

# return to the main menu
def exit():
        print('RETURN TO MAIN_MENU.....')
