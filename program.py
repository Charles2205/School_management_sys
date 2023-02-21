from student import Student
from system_colors import GREEN,YELLOW,RED,GREEN,WHITE

# Creating a database from a list
student_db=[]
# Creating a constant value for an id
STUDENT_ID = 's'

def welcome_screen():
    print(GREEN,'====== Welcome to Open Labs Student Managemet System =====',WHITE)
    user_input=int((input('1.Student Section\n2.About App\n3.Exit Application\nEnter a valid option from the list below: \n')))
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
    print(WHITE,'This app was developed in 2023 in OpenLabs as one of my projects.')

def exit_application():
    exit(200)

def student_session():
    """function holding the options about the students"""
    print(YELLOW,'*** Enter a valid option from the list below ')
    user_input=int(input(('1.Add Student\n2.View all student info\n3.Search for student info\n4.Update student info\n5.Delete student info\nProvide operation to perform: ')))









welcome_screen()