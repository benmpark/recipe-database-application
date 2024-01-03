# CSC6302 Week 4 Assignment
# Benjamin Park
# November 30, 2023
# Presentation Layer

import business_logic_layer as BLL
import data_access_layer as DAL
from os import getcwd, chdir, path


def display_options(is_selection=False):
    """Displays the main menu options to the user.

    If a cookbook or recipe is selected, an option to clear that selection will
    be included as well.

    Args:
        is_selection (bool): used to determine if 'clear selection' option is needed

    Returns:
        None
    """
    options = ["Clear current selection",
               "SELECT a COOKBOOK",
               "SELECT a RECIPE",
               "CHECK INGREDIENTS in a selected recipe",
               "SAVE a RECIPE to your menu",
               "DISPLAY your SHOPPING LIST",
               "DISPLAY your HOLIDAY MENU",
               "SAVE your MENU and SHOPPING LIST to disk",
               "EXIT the program"]
    output = "What would you like to do?\n"
    options_start = 1 - is_selection
    for i in range(options_start, len(options)):
        output += f"\n{i}. {options[i]}"
    print(output)


def get_user_option():
    """Gets the menu choice from the user.

    Returns
        float or bool: the user's choice, or False if not a numerical entry
    """
    try:
        return float(input("\nEnter your selection: "))
    except ValueError:
        return False


def process_option(selection, entry, database, menu):
    """Processes the main menu option selected by the user.

    Args:
        selection (str): the previously selected cookbook or recipe
        entry (float): the user's choice
        database (mysql.connector.connection_cext.CMySQLConnection): the active database connection
        menu (BLL.Menu): the holiday menu object

    Returns:
        str or None: the selected cookbook or recipe, or None
    """
    match entry:
        case 0:
            return None
        case 1:
            return select_cookbook(database)
        case 2:
            return select_recipe(database, selection)
        case 3:
            return check_ingredients(database, selection)
        case 4:
            save_recipe_to_menu(database, selection, menu)
        case 5:
            print(shopping_list(menu))
        case 6:
            display_holiday_menu(menu)
        case 7:
            save_to_disk(menu)
        case _:
            print(f"Invalid entry. Make sure your selection is an integer "
                  + f"between {1 - (selection is not None)} and 8, inclusive.")


def select_cookbook(database):
    """Prints a list of cookbooks in the database and lets the user select one.

    Args:
        database (mysql.connector.connection_cext.CMySQLConnection): the active database connection

    Returns:
        str: the selected cookbook
    """
    cookbooks = DAL.DatabaseOperations.select_cookbook(database)
    print("\nCOOKBOOKS:")
    for i in range(len(cookbooks)):
        print(f"{i + 1}. {cookbooks[i]}")
    while True:
        try:
            selection = int(input("\nSelect a cookbook (enter the corresponding number): "))
            return cookbooks[selection - 1]
        except IndexError:
            print("Make sure your selection matches one of the numbered cookbooks above.\nPlease try again.")
        except ValueError:
            print("Numerical inputs only; please try again.")


def select_recipe(database, cookbook=None):
    """Prints a list of recipes in the database and lets the user select one.

    If a cookbook is selected, the function will only list recipes in that cookbook.
    Otherwise, all recipes in the database will be listed.

    Args:
        database (mysql.connector.connection_cext.CMySQLConnection): the active database connection
        cookbook (str): the previously selected cookbook, if present

    Returns:
        str: the selected recipe
    """
    recipes = DAL.DatabaseOperations.select_recipe(database, cookbook)
    print("\nRECIPES:")
    for i in range(len(recipes)):
        print(f"{i + 1}. {recipes[i]}")
    while True:
        try:
            selection = int(input("\nSelect a recipe (enter the corresponding number): "))
            return recipes[selection - 1]
        except IndexError:
            print("Make sure your selection matches one of the numbered recipes above.\nPlease try again.")
        except ValueError:
            print("Numerical inputs only; please try again.")


def check_ingredients(database, selection):
    """Prints the ingredients in the selected recipe.

    Prints an error statement if no recipe has been selected.

    Args:
        database (mysql.connector.connection_cext.CMySQLConnection): the active database connection
        selection (str): the previously selected recipe

    Returns:
        str: the same previously selected recipe
    """
    result = DAL.DatabaseOperations.check_ingredients(database, selection)
    if result[0]:
        print(f"\nINGREDIENTS in {selection}: ")
        for i in range(len(result[1])):
            print(f"{i + 1}. {result[1][i]}")
        return selection
    else:
        print("An error occurred; please make sure you SELECT a RECIPE before trying to list ingredients.")
        return None


def categorize_recipe(menu, recipe):
    """Method to put a recipe into a category (i.e., select a course to serve at)

    Args:
        recipe (Recipe): the recipe object to categorize

    Returns:
        str: the name of the course to which the recipe will be added
    """
    print("\nCURRENT COURSES:")
    courses = menu.get_courses()
    courses_list = []
    i = 0
    for course in courses:
        courses_list.append(course)
        print(f"{i + 1}. {course.capitalize()}")
        i += 1
    print(f"When would you like to serve {recipe.name}?")
    selection = input("Enter the corresponding number or hit ENTER to create a new category. ")
    if selection:
        while True:
            try:
                selection = int(selection)
                return courses_list[selection - 1]
            except IndexError:
                print("Make sure your selection matches one of the numbered courses above.\nPlease try again.")
            except ValueError:
                print("Numerical inputs only; please try again.")
    else:
        return input("What is the name of your new course? ").strip().lower()


def save_recipe_to_menu(database, recipe, menu):
    """Saves a recipe to a menu, under the course prompted from the user.

    Args:
        database (mysql.connector.connection_cext.CMySQLConnection): the active database connection
        recipe (str): the selected recipe to be saved
        menu (BLL.Menu): the menu object into which the recipe will be saved

    Returns:
        None
    """
    recipe_to_add = DAL.DataToBusiness.convert_recipe(database, recipe)
    if recipe_to_add:
        course = categorize_recipe(menu, recipe_to_add)
        menu.add_recipe(recipe_to_add, course)
    else:
        print("An error occurred; please make sure you SELECT a RECIPE before trying to add one to your menu.")


def shopping_list(menu):
    """Prints a list of all ingredients in all recipes stored in the menu.
    Any ingredients that appear in multiple recipes are only printed once.

    Args:
        menu (BLL.Menu): the menu object being used to generate the shopping list

    Returns:
        str: the shopping list
    """
    the_list = menu.get_shopping_list()
    output = "\nSHOPPING LIST:\n==============\n"
    for item in the_list:
        output += f"•{item}\n"
    return output[:-1]


def display_holiday_menu(menu):
    """Prints the holiday menu.

    Args:
        menu (BLL.Menu): the menu object

    Returns:
        None:
    """
    print(menu)


def get_valid_directory():
    """
    Gets a valid directory on the local machine from the user.

    Returns:
        str: the path of the directory
    """
    while True:
        print(f"The current working directory is {getcwd()}")
        print("Hit ENTER to use this directory, or enter a new directory: ")
        filepath = input()
        if filepath:
            try:
                chdir(filepath)
                return filepath
            except FileNotFoundError as e:
                print(e, "Please try again.")
        else:
            return getcwd()


def save_to_disk(menu):
    """Saves the text of the menu and shopping list to a text file.
    Assumes the filepath argument has already been checked for validity.

    Args:
        menu (BLL.Menu): the menu object

    Returns:
        None
    """
    print(f"Where would you like to save a text copy of '{menu.name}'?")
    filepath = get_valid_directory()

    filename = path.join(filepath, f"{menu.name.replace(' ', '_')}.txt")
    with open(filename, "w") as fh:
        output = str(menu) + "\n\n" + shopping_list(menu)
        fh.write(output)


def main():
    """Driver function for the application."""
    print("Welcome to your holiday meal planner!\n")

    # initialize a menu object
    holiday_menu = BLL.Menu("2023 Holiday Menu")

    # Get user credentials to pass to the Data Access Layer
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")

    # try to connect to the database; abort if unsuccessful
    cnx = DAL.DatabaseOperations.connect_to_db(username, password)
    if not cnx:
        return

    # main menu functionality
    selection = None
    while True:
        print(f"\nCurrent Selection: {selection}")
        display_options(selection is not None)
        option = get_user_option()
        if option == 8:
            DAL.DatabaseOperations.disconnect_from_db(cnx)
            print("\nHappy holidays!\n")
            break
        elif option or option == 0:
            selection = process_option(selection, option, cnx, holiday_menu)
        else:
            print(f"Invalid entry. Make sure your selection is an integer "
                  + f"between {1 - (selection is not None)} and 8, inclusive.")


if __name__ == "__main__":
    main()
