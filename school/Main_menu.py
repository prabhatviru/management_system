import Main_menu
import Student
import Nameofschool
import Marks
import Student_Details

def Exit():
        print('ABORT THE PROGRAMME....')

while True:
        print('\t\t\t---------WELCOME TO SCHOOL--------------')
        print('\t\t\t-----------------------------------------------')
        print('1->Student')
        print('2->Nameofschool')
        print('3->Marks')
        print('4->Student_Details')
        print('5->exit')
        choice=int(input('enter your choice'))
        if choice ==1:
                Student.STUDENT_MENU()
        if choice ==2:
                Nameofschool.SCHOOLMENU()
        if choice ==3:
                Marks.STUDENT_MARKS()
        if choice ==4:
                Student_Details.DETAILS()
        if choice ==5:
                Exit()
                break
                   
