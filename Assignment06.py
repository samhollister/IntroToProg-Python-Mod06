# ------------------------------------------------------------------------------------------ #
# Title: Assignment06_Starter
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   SHollister,5/27/25,Created Script
#   <Your Name Here>,<Date>,<Activity>
# ------------------------------------------------------------------------------------------ #
import json


# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
students: list = []  # a table of student data
menu_choice: str = ''  # Hold the choice made by the user.

# Processing --------------------------------------- #
class FileProcessor:
    """
    A collection of processing layer functions that work with JSON files.

    Changelog (Who, When, What)
    SHollister, 5/27/25, Created class.
    SHollister, 5/27/25, Added function to read initial data from file.
    SHollister, 5/27/25, Added function to write data to file.
    """
    @staticmethod
    def read_data_file(file_name: str, student_data: list):
        """
        Reads initial data from JSON file.

        :param file_name: str
        :param student_data: str
        :return: student_data
        """
        try:
            file = open(file_name, "r")
            student_data = json.load(file)
            file.close()
        except FileNotFoundError as e:
            IO.output_error_messages("File not found.", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!",e)
        finally:
            if file.closed == False:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """
        Writes stored data to JSON file.
        :param file_name: str
        :param student_data: list
        """
        try:
            file = open(file_name, "w")
            json.dump(student_data, file)
            file.close()
            print("The following data was saved to file!")
            for student in students:
                print(f'Student {student["FirstName"]} '
                      f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        except TypeError as e:
            IO.output_error_messages("Please check that the data is in a valid JSON format.", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file.closed == False:
                file.close()

# Presentation --------------------------------------- #
class IO:
    """
    A collection of presentation layer functions that manage user input and output.

    Changelog (Who, When, What)
    SHollister, 5/27/25, Created class.
    SHollister, 5/27/25, Added function to display error messages to user.
    SHollister, 5/27/25, Added functions to input data from user and output stored data.
    """
    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """
        Displays custom error message to user.

        :param message: str
        :param error: Exception
        """
        print(message)
        if error is not None:
            print("---Technical Error Message---")
            print(error, error.__doc__, type(error), sep="\n")

    @staticmethod
    def output_menu(menu: str):
        """
        Displays the program menu to user.
        :param menu: str
        """
        print()
        print(menu)
        print()

    @staticmethod
    def input_menu_choice():
        """
        Inputs the menu choice from user.
        :return: Choice selected by user as string.
        """
        choice = "0"
        try:
            choice = input("Please enter your choice: ")
            if choice not in ("1","2","3","4"):
                raise Exception("Please enter a valid option.")
        except Exception as e:
            IO.output_error_messages(e.__str__())

        return choice

    @staticmethod
    def output_student_courses(student_data: list):
        """
        Displays currently stored student courses.
        :param student_data: list
        """
        print("-" * 50)
        for student in student_data:
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list):
        """
        Inputs student enrollment data.
        param: student_data: list
        """
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            student_data = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_messages("That is not a valid student name.", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)

        return student_data

# Ending of function definitions --------------------- #

# Beginning of main body of script ------------------- #

# When the program starts, read the file data into a list of lists (table)
students = FileProcessor.read_data_file(file_name=FILE_NAME, student_data=students)

# Present and Process the data
while True:

    # Present the menu of choices
    IO.output_menu(menu=MENU)
    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        IO.input_student_data(student_data=students)
        continue

    # Present the current data
    elif menu_choice == "2":
        IO.output_student_courses(student_data=students)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop

print("Program Ended")
