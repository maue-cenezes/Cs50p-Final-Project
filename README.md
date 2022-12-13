# <h1 align='center'>**Hogwarts Portal**</h1>



Hogwarts Portal is a python program that simulates an aplication that allows users to access a academic-related enviroment: with  assigments such as tests, interaction with lists of materials chose by the teachers (**and also edit this materials if you are a teacher!**) and many more.

### Video Demo:  <URL HERE>  

------------  

# Contents
=========================

* [Requirements](#requirements)
* [Files](#files)
* [How to use](#how-to-use)
* [Functions](#functions)
* [Design Choices](#design-choices)
* [Tecnologies and tools used](#technologies)
* [Final considerations](#final-considerations)
* [Author](#author)

--------------

# Requirements
=========================

For this program you won't need any pip installable modules, the only module used is csv. You will only need the [`databank csv files`](#databanks) and you're ready to go!

--------------

# Files
=========================

In the project directory you will find the following files:

* [PYTHON FILES](#python-files):
    * [Project.py](#projectpy)
    * [Test_project.py](#test_projectpy)
* [DATABANKS](#databanks):  
    * [Databank_books.csv](#databank_bookscsv)
    * [Databank_employees.csv](#databank_employeescsv)
    * [Databank_houses.csv](#databank_housescsv)
    * [Databank_students.csv](#databank_studentscsv)

## Python Files

### Project.py:
In this file you will find all the code for running the program, with all the [functions](#functions). The main function will be found on top of the code, just below some constants and variables declared first to make easier to read and understand the code.  
After that, all the functions are defined after some comment section used to divide them into the following groups:

- MENU RELATED FUNCTIONS:  
    > Functions that prints a menu or interact directly with menus

- TEST RELATED FUNCTIONS:  
    > Functions used in the test that students can take for a grade

- FILE RELATED FUNCTIONS:
    > Functions used on file management

- BOOKS RELATED FUNCTIONS:  
    > Functions used to edit books

- HOUSE RELATED FUNCTIONS:  
    > Functions used on "houses" menu 

- PROFILE RELATED FUNCTIONS:  
    > Function used on "Profile" menu  
 
- GENERAL FUNCTIONS:  
    > Functions used in general, during all the program  

### Test_project.py:
In this file you will find the codings that were used to test some functions from the project. This test file is written to be runned with `Pytest`. All the test functions are inside a main function on top of the file.

--------------
## Databanks

The databanks used are `.csv` files that contain some data that will be imported as soon as the program starts.   
   
### Databank_books.csv:
In this file are stored the books following data: Title and Subject. 

    "title,subject
    Advanced studies in potios preparations,Potions"

### Databank_employees.csv:
In this file are stored the employees following data: Name, House and Permission level.  
The permission level is based on their position on a hierachy, so for example a coordinator or principal have higher permission level than a teacher, and both have higher permission than students.

    "employee_name,house,permission
    snape,slytherin,1"

### Databank_houses.csv:
In this file are stored the houses following data: House_name and Points.  
The `House_name` are one from: _Gryffindor, Hufflepuff, Ravenclaw and Slytherin_;  
The `points` will be calculated based on the average score between the students of the house.

    "house_name,points
    gryffindor,10"

### Databank_students.csv:
In this file are stored the students following data: Name, House and Grade.  
The `name` and `house` are individual (**_Following the conditions of the "Houses\_name"_**);  
The grade is calculated based on the `Hogwarts Test` that can be taken on the [assigmentAAAA](# BOTA UM LINK ) menu. 
>(If the student haven't done the test yet, a **"TODO"** will be on the hogwarts_grade value)  

    "student,house,hogwarts_grade
    harry,gryffindor,TODO
    hermione,gryffindor,10"

--------------

# How to use
=========================  
After downloading the [Project.py](#projectpy) file and all the [Databanks](#databanks) into the same directory, you just need to run the code to iniciate it.  

In general, all menus use an input system that gets the option you type in and uses that to travel from menu to menu and doing the actions on the code. If you type an invalid option, nothing will happend and the same menu and prompt for input will be printed again. (**_In some cases, a message containing "Invalid Option" will be printed out as well_**)  
   
### Get access menu: 
As soon as the program starts, you'll see the first menu `Get access menu` where you can login into the program and load your information. You can type to choose your access with:

    1) for Student
    2) for Employee
    Or press '0' to quit  
- If `1` or `2` if choosed, the program will prompt again for a user name. If the name is found in the Students/Employees databank (**depending on which you chose!**), the program will move to the `main menu` and load all the informations associated with the log in.  
 
### Main Menu:  

On the `main menu` you'll be presented with 4 more options:  

      1) Assignments
      2) Materials
      3) Profile
      Or press '0' to Logout and go back to the "get access" screen 

- If option `1` is picked, you will be transfered to the `assignments menu`, from where you can interact with the `tests` and `grades`.  

- If option `2` is picked, you will be transfered to the `materials menu`, from where you can interact with the `books` and `houses` options.  

- If option `3` is picked, you will be transfered to the `profile menu`, from where you can see your data.  

- If option `0` is picked, you will be transfered back to the `get access menu`, from where you can log in. (_If any changes on the book's list is made during your access, it will save the changes on the [Books Databank](#databank_bookscsv) now._ (**_FOR EMPLOYEES ONLY!_**))  

### Assignments menu:
 Into the assignment menu, you'll be presented with 3 options:  

    1) Hogwarts test
    2) Grades
    Or press '0' to go back to the "Main Menu" screen

- If option `1` is picked, you will be transfered to the `Test menu`, from where you can either do the test, if it's not done yet (or if you're an employee) or it will be printed a message saying that is already done.

- If option `2` is picked, the `grade` will be printed.
If the access is from a student, only it's own grade will be shown, but if its an employees access, all students grade are going to be printed.  

- If option `0` is picked, you will be transfered back to the `Main menu`.  

### Materials Menu:  
 Into the assignment menu, you'll be presented with 3 options:  

    1) Books
    2) Houses
    Or press '0' to go back to the "Main Menu" screen

- If option `1` is picked, there's two paths:
    - For students: The list of books, imported from the [Books Databank](#databank_bookscsv) is printed out.
    
    - For employees: A new `menu` with 4 more options is going to appear:

          1) Add Book
          2) Remove Book
          3) Book List
          Or press '0' to go back to the "Main Menu" screen  


        - for option `1`, a prompt asking for a book's name and subject will appear, and then, after a confirmation, you can add a new book in the list. (_If any changes on the book's list is made during your access, it will save the changes on the [Books Databank](#databank_bookscsv) when loggin off into the [main menu](#main-menu.)_)  

        - for option `2`, a prompt asking for a book's name will appear, and then, after a searching in the databank, if a matching book name is found, you can delete that book from the list. (_If any changes on the book's list is made during your access, it will save the changes on the [Books Databank](#databank_bookscsv) when loggin off into the [main menu](#main-menu.)_)  
        - for option `3`, the list of books, imported from the [Books Databank](#databank_bookscsv) is printed out.
    
    - If option `2` is picked, a new menu will appear: the `houses sub menu`.
        - From there you will have 3 more options:

              1) Houses information
              2) Houses score
              Or press '0' to go back to the "Main Menu" screen

            - If option `1` is picked, a list of informations about each of the _hogwarts houses_ will be printed;
            - If option `2` is picked, a list of the _hogwarts houses_ will be printed followed by a `points` value, that is calculated by the average grade from the students from that house.

### Profile Menu:
In this menu, a couple of informations about the user will be printed out, such as the uses house and it's email (_that is simply the user's name followed by "@hogwarts.edu"_)

--------------  

# Functions
=========================  
As mentioned before, all functions are divided by groups ( _found at [project.py](#projectpy)_ ).  
 - **main()**:  
    The `main` function does not take any parameters, it's purpose is to take control of the program's flux, and call all other functions. It also have the job to import all the data before the first prompt appear, and get everything settle up for the users to interact with everything. After the first lines run, the function enters a "while True" loop, and it keeps running until the users chooses to quit in the `get access` menu.   

- **menu(index, permission=0)**:  
The `menu` function takes 2 arguments:  
    - **index** : A int-type value, that must be used to evaluate which menu is going to be printed. The value variates from -1 to 4, and each represents a menu screen.
    - **permission=0** : An optional int-type value argument that is used to define if a menu should be printed with students or employees options. By default, the value is "0", that represents the students level permission.  

    This function is called almost  works by printing a big menu, and then prompting a input for a option. It returns the value from that option input as a string. 

 - **get_access()**:  
 The `get access` function takes no arguments, and it's called only when in the `menu` function have index = -1. This function asks if its s student or employees, and after that asks a name and searchs on the databanks correspondly. If the name is found, it returns 3 values:
    - For employees: The users name, house and permission level associated with the name.  

    - For students: The users name, house and it's grade on the hogwarts test.

    If none is found, it keeps asking for another name until a valid one is given or the users choose to return. If the users choose to quit the app, it will return a tuple with (0, 0, 0) that indicates to the `main` function to stop the program.  

 - **tests_menu(grade, name='')**:  
The `tests_menu` function takes 2 arguments:  
    - **grade** : The value, for students, of the grade in the hogwarts test. It can be a int-type value, representing the grade; a str-type with 'TODO' written, representing that the test haven't yep been done; and a list-type value, that indicates the function that the test have already been done and it should print the value of the grade. ( **This is used on the [Assigment menu](#assignments-menu) inside the main function, when the option "Grades" is chosen**)
    - **name=''** : A optional str-type argument, used when printing the grade for the student.  

    This function can return a value if the users haven't take the test yet, and just print things otherwise.  

- **start_test(show_answers=False)** :
The `start_test` function take 1 optional argument: 
    - **show_answer=False** : A bool-type value, that indicates wheter it should print the answers of each question or not.

    This function runs a little while True loop that contains 5 questions and compares the users answer with the actual answer, and sum the score if its correct. It returns a int value representing the score, or the grade, on the test.  

- **is_valid_answer(answer)** :
The `is_valid_answer` function take 1 argument: 
    - **answer** : A str-type value  

    This function analizes the argument "answer" to see if its a valid answer by the following conditions:  
    1) It's only 1 in lenght  
    2) It matches with one of this chars: "a, b, c, d, e"  
    
    It returns the **answer, if its a valid one; or returns a message saying "invalid answer".  
  

- **load_students / load_employees / load_books / load_houses(file)** :  
These functions have only 1 argument, a str-type variable that contains the name of the `.csv file` that stores the data you want to import.  
All these functions works the same, by importing the data from the [Databank](#databanks) files and saves them in a dict-type variable, that it's returned at the end of the function.  

- **save_books / save_students(file)** :  
These functions have only 1 argument, a str-type variable that contains the name of the `.csv file` that you want to save the program's data 
These functions works the same, by saving any changes in the databanks imported in the program, such as the books list and the grade of the students.  

- **display_books()** :  
This function loops for every element in the book dictionary imported from `load_students` and prints every one in a line.  
  
- **edit_books(operation)** :  
This function takes 1 argument, a str-type value. The `operation` value must be "add" or "del" to properly work, if another value is passed it will just print a message saying "invalid operation."  
This function work by editing the `book` list imported from `load_books`. It prompts for a book name and subject to add, or for a book name in "del", and searchs all the book list for a match. If any is found, you can delete it.  





- **display_houses(option)** : 
This function takes 1 argument, a str-type value. The `option` value must be "info" or "points" to properly work, if another value is passed, nothing will happen.  
    - info:  
    Prints on the screen a list of informations for each house;  
    - points:  
    Prints, in a for loop, a list of points calculated via [calculate_average](#calculate-average) function.  


- **calculate_average(house_score, n_students)** : 
This function takes 2 int-type arguments:  
    - house_score: A value imported with `load_houses` function, containing the standart points for the house;  
    - n_students: A value getted via the `get_number_of_students` function.

    This function takes the two values and calculate the average grade for each house, depending on the number of students.

- **show_info(name, house)** :  
This takes 2 str-type arguments:  
    - name: the name of the user;
    - house: the house of the user  

    This function uses the name to create an email for the user and prints the house and email, both formatted.


- **confirm(string)** :  
This function takes 1 str-type argument:  
    - string: A phrase that will be shown in the prompt of the function.

    This function uses the `string` parameter in a while True sequence of inputs, asking for a "yes" or "no", and checks if the answer is a valid (either a yes or a no). If its positive, returns True, else it returns False.  
     If a invalid answer is given, it keeps asking for a anwser.


- **enter(str='Press "enter" to continue ')** :  
 This function takes 1 optional str-type argument: 
    - str: A phrase that will be shown in the prompt of the function.  

    This function only prompt for a input with the `str` parameter. It serves to give a pause during the program so the user can just press enter to continue when they're ready to.  

- **skip(n=10)** :  
 This function takes 1 optional int-type argument: 
    - n: Represents the number of times you want to skip lines in the program.

    This function serves as a way to clear the users interface by returning a lot of new lines that can be printed withthe standart `print` function.  
    It returns a "\n" multiplicated by `n`.

- **get_number_of_students(house, databank_students)** :   
This function takes 2 arguments:  
    - house: A str-type value imported with that represents one of the houses. 
    - databank_students: A dict-type value getted via the `load_students` function.

    This function takes the [Students databank](#databank_studentscsv) and searchs for every student if it's house is the same as in the `house` parameter, and add to a count.  
    At the end, returns the total number of students found for the house.  
   

--------------  

# Design choices  
=========================  
While writting this program, I chose to only use the default `csv` module that comes with python to keep things simple and focus in the essencials and basics of python.  
For this, I did the whole program not using any other library. By doing this, I was forced to go back through many lessons during the course, such as formatting strings, manipulating .csv files, using lists and dictionaries, using the `open` command to read/write files, etc.  
Also, the choice to make the whole program in reference to the 'Harry Potter' universe was inspired by David Malan examples during the classes.  

--------------

# Technologies  
During the process of making this project, the following tools used were:  
- [Virtual Studio Code (vs-code)](https://code.visualstudio.com)
- [Code.cs50.io](https://code.cs50.io)
- [Edx platform (that hospedates Cs50p)](https://courses.edx.org/dashboard)

--------------


# Final considerations  
After spending 3 years studing for a college degree that I didn't feel confortable, I found Cs50's Introduction to Programming with Python and finally saw a way to change my life by starting studing something that really interests me.  
Writting this program demanded a lot of effort and time, and many times I thought it wasn't good enough. But after dozens and dozens hours of writting all this, I feel proud of everything, even further that english is not my first language.  
Besides every bug and problem that I faced in the way, it was one of the most enjoyable trail that I have ever made.  

--------------  

# Author
My name is Caue Menezes, and I'm 20 years old at the moment. I'm from Santo André, Brazil, and I started taking Cs50p in august of 2020.  
I look forward to continue studing programming and even intend to start a degree on Analyses and Development of Systems, and keep programming as a job.

--------------














