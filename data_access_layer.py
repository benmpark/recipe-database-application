# CSC6302 Week 4 Assignment
# Benjamin Park
# November 30, 2023
# Data Access Layer

import mysql.connector
from mysql.connector import errorcode
import business_logic_layer as BLL


class DatabaseOperations:
    """Class to manage access to the database (from this DAL)."""

    @staticmethod
    def connect_to_db(username, password):
        """Connects to the database (details are hard-coded for now).

        Returns:
            mysql.connector.connection_cext.CMySQLConnection: the database connection
        """
        try:
            my_db = mysql.connector.connect(user=username,
                                            password=password,
                                            host='127.0.0.1',
                                            database='MealPlanning')
            return my_db
        except mysql.connector.Error as err:
            if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
                print("Invalid credentials; check your username or password")
            elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist.")
            else:
                print(err)
            return False

    @staticmethod
    def disconnect_from_db(database):
        """Disconnects from the database

        Args:
            database (mysql.connector.connection_cext.CMySQLConnection): the database to close

        Returns:
            None
        """
        database.close()

    @staticmethod
    def select_cookbook(connection):
        """Retrieves all cookbooks from the database.

        Args:
            connection (mysql.connector.connection_cext.CMySQLConnection): the active database connection

        Returns:
            list[str]: a list of cookbooks
        """
        cookbooks = []
        cursor = connection.cursor()
        cursor.callproc("GetCookbooks")
        for cookbook in cursor.stored_results():
            cookbook_results = cookbook.fetchall()
        for cookbook in cookbook_results:
            cookbooks.append(cookbook[0])
        cursor.close()
        return cookbooks

    @staticmethod
    def select_recipe(connection, selected_cookbook):
        """Retrieves all recipes, either from the selected cookbook,
        or from the entire database.

        Args:
            connection (mysql.connector.connection_cext.CMySQLConnection): the active database connection
            selected_cookbook (str): the name of the selected cookbook

        Returns
            list[str]: a list of recipes
        """
        recipes = []
        cursor = connection.cursor()
        if selected_cookbook:
            cursor.callproc("GetRecipesFromCookbook", (selected_cookbook,))
            for recipe in cursor.stored_results():
                recipe_results = recipe.fetchall()
            for recipe in recipe_results:
                recipes.append(recipe[0])
        else:
            cursor.callproc("GetAllRecipes")
            for recipe in cursor.stored_results():
                recipe_results = recipe.fetchall()
            for recipe in recipe_results:
                recipes.append(recipe[0])
        cursor.close()
        return recipes

    @staticmethod
    def check_ingredients(connection, recipe):
        """Retrieves all ingredients for a selected recipe.

        Args:
            connection (mysql.connector.connection_cext.CMySQLConnection): the active database connection
            recipe (str): the name of the selected recipe

        Returns:
            tuple[bool, list[str]]: boolean if there's a matching recipe and a list of ingredients
        """
        ingredients = []
        cursor = connection.cursor()
        cursor.callproc("ListIngredients", (recipe,))
        for ingredient in cursor.stored_results():
            ingredients_results = ingredient.fetchall()
        for ingredient in ingredients_results:
            ingredients.append(ingredient[0])
        cursor.close()
        return len(ingredients) > 0, ingredients


class DataToBusiness:
    """Class to manage interaction with the business logic layer."""

    @staticmethod
    def convert_recipe(connection, recipe):
        """Converts a recipe from the database to a Recipe object.

        Args:
            connection (mysql.connector.connection_cext.CMySQLConnection): the active database connection
            recipe (str): the name of the recipe to be converted

        Returns:
            BLL.Recipe: the converted recipe
        """
        cursor = connection.cursor()
        cursor.callproc("RecipeCookbookInfo", (recipe,))
        for item in cursor.stored_results():
            results = item.fetchall()

        ingredients = DatabaseOperations.check_ingredients(connection, recipe)[1]

        cursor.close()

        if results:
            return BLL.Recipe(results[0][0], results[0][1], ingredients)
        else:
            return False
