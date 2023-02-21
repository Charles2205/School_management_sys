from student import Student
from system_colors import GREEN,YELLOW,RED,GREEN,WHITE
from random import randint
# Creating a database from a list
student_db=[]
# Creating a constant value for an id
STUDENT_ID = 's'

def welcome_screen():
    print(GREEN,'====== Welcome to Open Labs Student Managemet System =====',WHITE)
    user_input=int((input('1.Student Section\n2.About App\n3.Exit Application\nEnter a valid option from the list below: ')))
    user_option(user_input)

def user_option(user_input):
    """Determine what the user input"""
    if user_input==1:
        student_session()
    elif user_input ==2:
        about_app()
    elif user_input ==3:
        exit_application()
    else:
        print(RED,'Invalid option.TRY AGAIN!!')
        welcome_screen()

def about_app():
    print(GREEN,'This app was developed in 2023 in OpenLabs as one of my projects.')

def exit_application():
    exit(200)

def student_session():
    """function holding the options about the students"""
    print(YELLOW,'*** Enter a valid option from the list below *** ',WHITE)
    user_input=int(input(('1.Add Student\n2.View all student info\n3.Search for student info\n4.Update student info\n5.Delete student info\nProvide options to perform: ')))
    student_option(user_input)

def student_option(user_input):
    """Function to determine what student chooses"""
    if user_input==1:
        student_db.append(add_student())
    elif user_input==2:
        pass
    elif user_input ==3:
        pass
    elif user_input ==4:
        pass
    elif user_input ==5:
        pass
    else:
        pass

def add_student():
    print('*** ADD STUDENT INFO ***')
    first_name=input("Enter your first name: ")
    last_name=input("Enter your last name: ")
    dob=input("Enter your DOB (mm/dd/yyyy):")
    gender=input("Enter Gender: ")
    course=input("Enter your course: ")

    student_no=randint(0,5000000)
    student_id=STUDENT_ID+str(student_no)

    return Student(student_id,first_name,last_name,dob,gender,course)
    




welcome_screen()