# CSC6302 Week 4 Assignment
# Benjamin Park
# November 30, 2023
# Business Logic Layer

import textwrap


class Recipe:
    """Class to hold recipes from the database.

    Args:
        name (str): the name of the recipe
        cookbook (str): the name of the cookbook that holds the recipe
        ingredients (list[str]): the list of ingredients
    """
    def __init__(self, name, cookbook, ingredients):
        """Constructor method"""
        self.name = name
        self.cookbook = cookbook
        self.ingredients = ingredients

    def add_ingredient(self, ingredient):
        """Method to add an ingredient to a recipe.

        Args:
            ingredient (str): the name of the ingredient to be added
        Returns:
            None
        """
        self.ingredients.append(ingredient)

    def get_ingredients(self):
        """Yields the ingredients in the recipe.

        Returns:
            list[str]: ingredients
        """
        return self.ingredients

    def __str__(self):
        """Overrides default print output to display a detailed recipe."""
        output = f"•{self.name} (source: {self.cookbook})\n"
        wrapper = textwrap.TextWrapper(width=76)
        ingredient_output = "INGREDIENTS: "
        ingredients_needed = self.get_ingredients()
        for i in range(len(ingredients_needed)):
            ingredient_output += f"{ingredients_needed[i]}, "
        ingredient_output = ingredient_output[:-2]
        output += textwrap.indent(wrapper.fill(ingredient_output), "    ")
        return output


class Menu:
    """Class to hold the menu and all its detailed information.

    Args:
        name (str): the name of the planning menu
        *recipes list[Recipe]: an (optional) list of recipe objects

    Attributes:
        courses (dict): collection of courses and their corresponding recipes
    """
    def __init__(self, name, *recipes):
        """Constructor method"""
        self.name = name
        self.courses = {"breakfast": [], "lunch": [], "dinner": [], "snacks": []}

        # if the menu is initialized with any recipes, put them in the 'uncategorized' category
        if len(recipes) > 0:
            self.courses["uncategorized"] = recipes

    def get_courses(self):
        """Retrieves a list of courses currently set up in the menu

        Returns:
            list[str]: the list of courses
        """
        return self.courses.keys()

    def add_recipe(self, recipe, course):
        """Adds a recipe to the menu.

        Args:
            recipe (Recipe): the recipe object to be added
            course (str): the name of the course when the recipe will be served

        Returns:
            bool: True (when successful)
        """
        if course in self.courses:
            self.courses[course].append(recipe)
            return True
        else:
            self.courses[course] = [recipe]
            return True

    def remove_recipe(self, recipe, course):
        """Removes a recipe from a course (and from the menu as a whole)

        Args:
            recipe (Recipe): the recipe object to be removed
            course (str): the name of the course where the recipe is

        Returns:
            bool: True when successful, otherwise False
        """
        try:
            self.courses[course].remove(recipe)
            return True
        except ValueError:
            return False

    def move_recipe(self, recipe, new_course, old_course="uncategorized"):
        """Re-categorizes a recipe already in the menu

        Args:
            recipe (Recipe): the recipe object to be moved
            new_course (str): the name of the course where the recipe is being moved
            old_course (str): the name of the course from where the recipe is being moved

        Returns:
            bool: True when successful, False otherwise
        """
        if self.remove_recipe(recipe, old_course):
            self.add_recipe(recipe, new_course)
            return True
        else:
            return False

    def get_shopping_list(self):
        """Retrieves a shopping list covering all the items in the menu.

        Note that any ingredients that appear in multiple recipes are only printed once.

        Returns:
            set: the (alphabetized) shopping list
        """
        shopping_list = set()
        for course in self.courses:
            for recipe in self.courses[course]:
                for ingredient in recipe.get_ingredients():
                    shopping_list.add(ingredient)
        return sorted(shopping_list)

    def __str__(self):
        """Overrides default print output to display a helpful menu."""
        output = "\n" + self.name.upper()
        output += "\n" + "=" * len(self.name) + "\n"
        for course in self.courses.keys():
            if len(self.courses[course]) > 0:
                output += "\n" + course.capitalize() + ":\n" + "-" * (len(course) + 1) + "\n"
                for recipe in self.courses[course]:
                    output += str(recipe) + "\n"
        return output[:-1]


# the following class is included in my initial design but are not utilized at the moment
class Cookbook:
    """Class to hold a cookbook from the database and all its detailed information.

        Args:
            name (str): the name of the cookbook
            is_book (bool): whether the cookbook is paper (vs. online)
            website (str): the url, optional
            *recipes list[Recipe]: an (optional) list of recipe objects
        """
    def __init__(self, name, is_book=True, website=None, *recipes):
        """Constructor method"""
        self.name = name
        self.is_book = is_book
        self.website = website
        self.recipes = recipes

    def __str__(self):
        return self.name
