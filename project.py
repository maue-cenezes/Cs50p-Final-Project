    ## Csv is used to save and read out the values from the databanks
import csv

    ## Variables to make it easier to change the csv files paths used as databanks
db_students = 'databank_students.csv'
db_employees = 'databank_employees.csv'
db_books = 'databank_books.csv'
db_houses = 'databank_houses.csv'

    ## Values to make easier to read the menus indexes in the code
LOGIN_MENU = -1
MAIN_MENU = 0
ASSIGNMENT_MENU = 1
MATERIALS_MENU = 2
PROFILE_MENU = 3
HOUSE_SUB_MENU = 4



##### Runs the code
def main():
    global students, employees, books, houses

    ## Imports and save the data from databank csv files
    students = load_students(db_students)
    employees = load_employees(db_employees)
    books = load_books(db_books)
    houses = load_houses(db_houses)

    ## First menu level
    menu_index = LOGIN_MENU

    ## Run the app
    while True:
        ## First menu
        if menu_index == LOGIN_MENU:
            global access, permission, access_house, edited_books
            ## Check if is a student or a employee
            access, access_house, permission = get_access()
            ## 0 is returned when the user chooses to quit
            if access == 0:
                if confirm('Are you sure you want to quit the app? '):
                    print('Quitting the aplication... ')
                    break
                else:
                    print('Returning to the menu.')
            
            else:
                edited_books = False
                menu_index = MAIN_MENU


        ## Main menu
        option = menu(menu_index)
        if menu_index == MAIN_MENU:

            if option == '1':
                menu_index = ASSIGNMENT_MENU

            elif option == '2':
                menu_index = MATERIALS_MENU
            
            elif option == '3':
                menu_index = PROFILE_MENU
        
            elif option == '0':
                ## Go back to login screen
                if confirm('Are you sure you want to exit this access?'):
                    
                    ## Save book list on databank, if it was edited
                    if edited_books:
                        save_books(db_books)
                    menu_index = LOGIN_MENU
        


        ## Assignments menu
        elif menu_index == ASSIGNMENT_MENU:
                
            ## For returning to Main menu for both students and employees
            if option == '0':
                menu_index = MAIN_MENU
                

        ########## Options for student in assigment menu
            elif permission == 0:
                hogwarts_grade = students[access]['hogwarts_grade']
                ## Show test
                if option == '1':

                        ## If it is '0', it mean that you chose to return or it already has been done
                        test_option = tests_menu(hogwarts_grade)
                        if test_option == '0':
                            pass
                        
                        ## If it is '1', you can do the test
                        elif test_option == '1':
                            hogwarts_test = start_test()

                            ## It returns '0' when you don't confirm
                            if hogwarts_test == '0':
                                pass
                            
                            ## If do the test, it will assign the grade by itself and save when you finish
                            else:
                                students[access]['hogwarts_grade'] = hogwarts_test
                                houses[access_house]['points'] = houses[access_house]['points'] + hogwarts_test
                                save_students(db_students)

                        else:
                            print('Invalid test option.')

                ## Show grade
                elif option == '2':               
                        ## Uses a list as an indicator to "Tests", excluding the need of another function
                        print(skip(30))
                        test_option = tests_menu([hogwarts_grade], name=access)
                        enter()


        ########## Options for employee in assigment menu
            elif permission == 1:
                ## Allows employes to check the test and its answers
                if option == '1':
                    print(f'Hello, {access.capitalize()}! You can see the test and check all questions.')
                    if confirm('Do you want to see the test? '):
                        teacher_test = start_test(show_answers=True)
                        print(f'Your score on this test was: {teacher_test}.')
                        enter()


                ## Prints every student grade
                elif option == '2':
                    for student in students:
                        hogwarts_grade = students[student]['hogwarts_grade']
                        tests_menu([hogwarts_grade], name=student)
                    enter()




        ## Material Menu
        elif menu_index == MATERIALS_MENU:

            ## For returning to Main menu for both students and employees
            if option == '0':
                menu_index = MAIN_MENU

            ## Show Books in general
            elif option == '1':

             ##### Book option for students
                if permission == 0:
                    ## Show list of books in students access
                    display_books()
                    enter()

             ##### Books menu for employees
                elif permission > 0:
                    book_option = menu(menu_index, permission)     

                    ## while loop for staying in this menu until employee chooses to return
                    while book_option != '0':

                        ## Add a new book
                        if book_option == '1':
                            edit_books('add')
                            add_another = input('You want to add another book? ')
                            while add_another in ['yes', 'y', 'confirm']:
                                edit_books('add')
                                add_another = input('You want to add another book? ')

                        ## Excludes an existing book
                        elif book_option == '2':
                            edit_books('delete')
                            delete_another = input('You want to remove another book? ')
                            while delete_another in ['yes', 'y', 'confirm']:
                                edit_books('delete')
                                add_another = input('You want to remove another book? ')

                        ## Displays all the books
                        elif book_option == '3':
                            display_books()
                            enter()

                        book_option = menu(menu_index, permission)


            ## Show houses options, the same for both students and employees
            elif option == '2':
                houses_options = menu(HOUSE_SUB_MENU)

                ## Option for returning to materials menu
                while houses_options != '0':

                    ## Show houses information
                    if houses_options == '1':
                        display_houses('info')
                        enter()


                    ## Show houses score
                    elif houses_options == '2':
                        display_houses('points')
                        enter()

                    houses_options = menu(HOUSE_SUB_MENU)





        elif menu_index == PROFILE_MENU:
            ## For returning to Main menu for both students and employees
            if option == '0':
                menu_index = MAIN_MENU


            elif option == '1':
                show_info(access, access_house)
                enter()

######################################################################################################
######################################################################################################








######################################################################################################
   ###############################  MENU RELATED FUNCTIONS  #######################################
######################################################################################################

    ##### Prints out all the menus, based on the "menu_index" variable on Main function,
    ####  returns a prompt for an option
def menu(index, permission=0):
    if index == MAIN_MENU:
        print(skip(30))
        print(f'''
 Main Menu:
 ――――――――――――――――――――――――――――

    1) Assignments

    2) Materials

    3) Profile


    0) Logout

            {access.capitalize()}
    ''')
        
    

    elif index == ASSIGNMENT_MENU:
        print(skip(30))
        print(f'''
 Assignment Menu
 ――――――――――――――――――――――――――――

    1) Hogwarts test

    2) Grades


    0) <-- Back to Main Menu

            {access.capitalize()}
        ''')
        
            

    elif index == MATERIALS_MENU:
        print(skip(30))
        if permission >= 1:
            print('''
 Books Menu  
 ――――――――――――――――――――――――――――――――

    1) Add Book 

    2) Remove Book
 
    3) Book List

    0) <-- Back to Materials Menu
        
        ''')


        else:
            print('''
 Materials Menu
 ――――――――――――――――――――――――――――

    1) Books

    2) Houses
 

    0) <-- Back to Main Menu
        
        ''')



    elif index == HOUSE_SUB_MENU:
        print(skip(30))
        print(f'''
 Houses Menu
 ――――――――――――――――――――――――――――

    1) Houses information

    2) Houses score


    0) <-- Back to Main Menu

            {access.capitalize()}
        ''')



    elif index == PROFILE_MENU:
        print(skip(30))
        print(f'''
  Profile Menu
 ――――――――――――――――――――――――――――

    1) Personal information


    0) <-- Back to Main Menu

            {access.capitalize()}
        ''')


    return input('Choose an option: ').lower().strip()
        



    ##### Gets a logon and check if it is valid or not, return a tuple with (name and permission level)
def get_access():
    
    while True:
        print(skip(30))
        print('''
 Welcome To Hogwarts Portal
――――――――――――――――――――――――――――
 
 What service do you want?

    1) Student

    2) Employee


    0) Quit
    ''')
        escolha = input('Choose one option ').lower().strip()
        if escolha == '1':
            name = input('What is your name? ').lower().strip()
            while name != '0':
                if name in students:
                    return (name, students[name]['house'], 0)
                else:
                    print('Name not registered, please try again.')
                    name = input('What is your name? (type "0" to return) ').lower().strip()


        elif escolha == '2':
            name = input('What is your name? ').lower().strip()
            while name != '0':
                if name in employees:
                    return (name, employees[name]['house'], int(employees[name]['permission']))
                else:
                    print('Name not registered, please try again.')
                    name = input('What is your name? (type "0" to return) ').lower().strip()


        elif escolha == '0':
            return (0, 0, 0)



    ##### Check the status of the test (completed or not) and print it out the options, might return '0' when its
    #### not possible to start the test by any reason
def tests_menu(grade, name=''):
    if grade == 'TODO':
        print(skip(30))
        print(f'''
    You have a pendent test.
    ――――――――――――――――――――――――――――

    1) Start now

    0) Return

        ''')
        return input('Choose an option: ')


    ## It will be a list for checking if you need to just printing it out or if its already done
    elif type(grade) == list:
        hogwarts_grade = grade[0]
        print(f'''
     Grades
    ――――――――――――――――――――――――――――――――――――
{name.capitalize()}: {hogwarts_grade}
――――――――――――――――――――――――――――――――――――
''')


    ## for when the test is already done and you try to do it again, returns a '0' to indicate it
    else:
        print(skip(30))
        print(f'''
     You already did the test.
    ――――――――――――――――――――――――――――
        ''')
        enter()
        print(skip(30))
        return '0'

######################################################################################################
######################################################################################################








######################################################################################################
   ##############################  TEST RELATED FUNCTIONS  #######################################
######################################################################################################

    ##### Runs the Hogwarts test, printing every question, checking if it's correct and add the score, 
    ####  return the score
def start_test(show_answers=False):
    answer = ''
    print(skip(30))
    print(f'''
    ――――――――――――――――――――――――――――――――――――――――――――
        You can now start the test.

    This test is composed by 5 questions,
    each one with 2 points value.
    
    ''')
    if not confirm('Are you sure you want to start this test? '):
        return '0'


    score = 0

        ### Question 1
    if show_answers == True:
        answer = '(b)'
    print(skip(30))
    print(f'''
――――――――――――――――――――――――――――――――――――――――――――

(01) What alternative does not contain the
    name of a House?

a) Gryffindor
b) Patronum
c) Hufflepuff
d) Slytherin
e) Ravenclaw
                {answer}
    ''')
    resposta = is_valid_answer(input('What is your anwser? ').lower().strip())
    while resposta == None:
        resposta = is_valid_answer(input('What is your anwser? ').lower().strip())
    if resposta == 'b':
        print('Correct! ')
        enter()
        score += 2
    else:
        print('Incorrect =( ')
        enter()

        ### Question 2
    if show_answers == True:
        answer = '(c)'
    print(skip(30))
    print(f'''
――――――――――――――――――――――――――――――――――――――――――――

(02) What animals are allowed in Hogwarts 
 as pets?

a) Snakes, birds and fishs
b) Dogs, cats and hamsters
c) Owls, frogs and cats 
d) Rabbits, guinea pigs and mices 
e) Animals are not allowed in Hogwarts
                {answer}
    ''')
    resposta = is_valid_answer(input('What is your anwser? ').lower().strip())
    while resposta == None:
        resposta = is_valid_answer(input('What is your anwser? ').lower().strip())
    if resposta == 'c':
        print('Correct! ')
        enter()
        score += 2
    else:
        print('Incorrect =( ')
        enter()

        ### Question 3
    if show_answers == True:
        answer = '(c)'
    print(skip(30))
    print(f'''
――――――――――――――――――――――――――――――――――――――――――――

(03) What are the three unforgivable 
 curses?

a) Expelliarmus, expecto patronum and incendio
b) Impedimenta, incarcerous and alohomora
c) Avada kedavra, crucio and imperio
d) Diffindo, wingardium leviosa and alohomora
e) There are no unforgivable curses
                {answer}
    ''')
    resposta = is_valid_answer(input('What is your anwser? ').lower().strip())
    while resposta == None:
        resposta = is_valid_answer(input('What is your anwser? ').lower().strip())
    if resposta == 'c':
        print('Correct! ')
        enter()
        score += 2
    else:
        print('Incorrect =( ')
        enter()

        ### Question 4
    if show_answers == True:
        answer = '(e)'
    print(skip(30))
    print(f'''
――――――――――――――――――――――――――――――――――――――――――――

(04) What is the founder's first name of Ravenclaw house?

a) Helga
b) Salazar
c) Louis
d) Godric
e) Rowena
                {answer}
    ''')
    resposta = is_valid_answer(input('What is your anwser? ').lower().strip())
    while resposta == None:
        resposta = is_valid_answer(input('What is your anwser? ').lower().strip())
    if resposta == 'e':
        print('Correct! ')
        enter()
        score += 2
    else:
        print('Incorrect =( ')
        enter()

        ### Question 5
    if show_answers == True:
        answer = '(b)'
    print(skip(30))
    print(f'''
――――――――――――――――――――――――――――――――――――――――――――

(05) Which house is the house for intelligence and wit?

a) Hufflepuff
b) Ravenclaw 
c) Slytherin
d) Gryffindor
e) None of them
                {answer}
    ''')
    resposta = is_valid_answer(input('What is your anwser? ').lower().strip())
    while resposta == None:
        resposta = is_valid_answer(input('What is your anwser? ').lower().strip())
    if resposta == 'b':
        print('Correct! ')
        enter()
        score += 2
    else:
        print('Incorrect =( ')
        enter()


    ##### Final message
    print('You finished your test successfully')
    enter()
    return score


    ##### Keeps asking the user for an answer while it's not one of the test options, return the answer
def is_valid_answer(answer):    
    if answer in ['a', 'b', 'c', 'd', 'e'] and len(answer) == 1:
        return answer
    else:
        print('Invalid answer, try again... ')
        return None

######################################################################################################
######################################################################################################








######################################################################################################
   ##############################  FILE RELATED FUNCTIONS  #######################################
######################################################################################################

    ##### imports students list from csv databank and save, return a dict with all data
def load_students(file):
    with open(file) as csvfile:
        student_list = {}
        reader = csv.DictReader(csvfile)
        for line in reader:
            student, house, grade = line['student'], line['house'], line['hogwarts_grade']
            student_list[student] = {'house' : house, 'hogwarts_grade' : grade}
        return student_list



    ##### imports employees list from csv databank and save, return a dict with all data
def load_employees(file):
    with open(file) as csvfile:
        employee_list = {}
        leitor = csv.DictReader(csvfile)
        for line in leitor:
            employee, house, permission = line['employee_name'], line['house'], line['permission']
            employee_list[employee] = {'house' : house, 'permission' : permission}
        return employee_list



    ##### imports books from csv databank and save, return a dict with all data
def load_books(file):
    with open(file) as csvfile:
        book_list = {}
        leitor = csv.DictReader(csvfile)
        for line in leitor:
            title, subject = line['title'], line['subject']
            book_list[title] = {'subject' : subject}
        return book_list



    #### imports houses data and save, return a dict with all data
def load_houses(file):
    with open(file) as csvfile:
        house_list = {}
        reader = csv.DictReader(csvfile)
        for line in reader:
            house_name, points, = line['house_name'], int(line['points'])
            house_list[house_name] = {'points' : points}
        return house_list



    ##### Saves a possible edited list of books when exiting the access
def save_books(file):
    with open(file, 'w', encoding='UTF-8', newline='') as save_file:
        escritor = csv.DictWriter(save_file, fieldnames=['title', 'subject'])
        escritor.writeheader()
        for book in books:
            title, subject = book, books[book]['subject']
            escritor.writerow({'title' : f"{title}", 'subject' : subject})


    ##### Saves the students list when someone do the test
def save_students(file):
    with open(file, 'w', encoding='UTF-8', newline='') as save_file:
        escritor = csv.DictWriter(save_file, fieldnames=['student', 'house', 'hogwarts_grade'])
        escritor.writeheader()
        for student in students:
            name, house, grade = student, students[student]['house'], students[student]['hogwarts_grade']
            escritor.writerow({'student' : name, 'house' : house, 'hogwarts_grade' : grade}) 


######################################################################################################
######################################################################################################








######################################################################################################
   ##############################  BOOKS RELATED FUNCTIONS  #######################################
######################################################################################################

    ##### Prints whole list of books, using the dict returned by load_books()
def display_books():
    print(skip(30))
    print('LIST OF BOOKS\n―――――――――――――――\n')
    for book in books:
        subject = books[book]['subject']
        print(f'''
{book}, {subject}
――――――――――――――――――――――――――――――――――――
''')



    ##### Edit the book list, y adding or removing a book
def edit_books(operation):
    global edited_books
        ## Add a new book
    if operation == 'add':
        title = input('Type the book title: ').capitalize().strip()
        subject = input('Type the subject of the book: ').capitalize().strip()
        if confirm(f'Are you sure you want to add the book: {title} for {subject}? '):
            books[title] = {'subject': subject}
            edited_books = True
            print('Book added successfully')
        else:
            enter('Operation cancelled, press enter to return ')
    

    ## removes an existing book
    elif operation == 'delete':
        display_books()
        title = input('\nType the title of the book that you want to remove: ').strip().capitalize()

            ## Checks if the book already exists
        if title in books:
            print(f'Book "{title}" for "{books[title]["subject"]}" found.')
            if confirm('Are you sure you want to remove this book from the list? '):
                del books[title]
                edited_books = True
                print('Book removed successfully.')
        else:
            print('Book not registered, please try again. ')

######################################################################################################
######################################################################################################








######################################################################################################
   ##############################  HOUSE RELATED FUNCTIONS  #######################################
######################################################################################################

def display_houses(option):

    ## Just show some information about each house
    if option == 'info':
        print(f'''
        Gryffindor
    ――――――――――――――――――――――――――――
    {f'Founder':10} -----> Godric Gryffindor
    {f'Animal':10} -----> Lion
    ――――――――――――――――――――――――――――



        Ravenclaw
    ――――――――――――――――――――――――――――
    {f'Founder':10} -----> Rowena Ravenclaw
    {f'Animal':10} -----> Eagle
    ――――――――――――――――――――――――――――



        Hufflepuff
    ――――――――――――――――――――――――――――
    {f'Founder':10} -----> Helga Hufflepuff
    {f'Animal':10} -----> Badger
    ――――――――――――――――――――――――――――



        Slytherin
    ――――――――――――――――――――――――――――
    {f'Founder':10} -----> Salazar Slytherin
    {f'Animal':10} -----> Snake
    ――――――――――――――――――――――――――――
        ''')



    ## Show houses points based on average grade of students in their test, based on the houses
    elif option == 'points':
        print(skip(30))
        print('Houses Points: \n―――――――――――――――\n')
        for house in houses:
            house_score = houses[house]['points']
            number_of_students = get_number_of_students(house, students)
            average = calculate_average(house_score, number_of_students)
            print(f'''
{house.capitalize():12} ----------->   {average:.0f} points.
―――――――――――――――――――――――――――――――――――――――――
''')
            

#### Calculates the average between the grades of a house
def calculate_average(house_score, n_students):    
    if n_students != 0:
        average = (house_score / n_students)
    ## Will return the house score if none students from it are detected, for avoiding "Zero Division Error"
    else:
        return house_score
    return average


######################################################################################################
######################################################################################################








######################################################################################################
   ##############################  PROFILE RELATED FUNCTIONS  #######################################
######################################################################################################

def show_info(name, house):
    print(skip(30))
    print(f'''
  {name.capitalize()}
 ――――――――――――――――――――――――――――

{f'House':7} ----->  {house.capitalize()} 

{f'Email':7} ----->  {f"{name}@hogwarts.edu"}
    ''')





######################################################################################################
######################################################################################################








######################################################################################################
   ############################# GENERAL FUNCTIONS #######################################
######################################################################################################


    ##### For confirmations in general during the program, return Bool
def confirm(string):
    while True:
        confirmation = input(f'{string} (Yes or No) ').lower().strip()
        if confirmation in ['yes', 'y', 'confirm']:
            return True
        elif confirmation in ['no', 'n', 'ñ', 'cancel']:
            return False
        else:
            print('Please, answer only with "Yes" or "No"')



    ##### Prompts for an input to stop the program so the user can read and then press enter
def enter(str='Press "enter" to continue '):
    input(str)



    ##### Prints a lot of new blank lines to clear the program interface
def skip(n=10):
    return f'\n' * n
        


    ## Returns the number of students in a house
def get_number_of_students(house, databank_students):
    number_of_students = 0
    for student in databank_students:
        if databank_students[student]['house'] == house:
            number_of_students += 1

    return number_of_students

######################################################################################################
######################################################################################################





if __name__ == '__main__':
    main()