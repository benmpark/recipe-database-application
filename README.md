# Holiday Meal Planner
A three-layered Python application to create a holiday menu from an existing MySQL database of recipes.

## Overview
This repository has the files to create a holiday menu from an existing database of recipes (a sample meal-planning database creation script is also inclued). The (Python) database application has three layers (in separate files, as shown below): the presentation layer, the business logic layer, and the data access layer.

## Files Included
- park_project4.sql (a MySQL script that can be run to create the meal-planning database and populate it with some random recipes)
- presentation_layer.py
- business_logic_layer.py
- data_access_layer.py
- Documentation (folder containing HTML files with the documentation generated from the docstrings courtesy of [pdoc](https://pdoc3.github.io/pdoc/).

## Running the Application
1. The meal-planning database must be created first; run the SQL script (e.g., in MySQL Workbench). Note that you will need your username and password for access to the MySQL server where you are running this script.
2. Ensure that the three .py files above are all in the same directory (and, of course, that you have [Python](https://www.python.org) installed).
3. The entry point for the application is the user-facing `presentation_layer.py`; run this file from your command line (or application of your choosing).
4. You will be prompted to enter your database credentials (see step 1), after which you should be brought to the main menu, where you can perform various actions:
  1. Select a Cookbook
  2. Select a Recipe
  3. Check ingredients in a recipe
  4. Save a recipe to your menu
  5. Display your shopping list
  6. Display your menu
  7. Save your menu and shopping list to a text file
  8. Exit the Program

### Some Included Features
- Browse by cookbook or by recipe
- menu is pre-populated with breakfast, lunch, dinner, and snacks courses
- shopping list is automatically generated from ingredients in the recipes that have been added to the menu
- export the menu and shopping list to disk (as a simple text file)

### A Sample Menu & Shopping List Output
```
2023 HOLIDAY MENU
=================

Lunch:
------
•Braised Spanish Lentils (source: How to Cook Everything Vegetarian)
	INGREDIENTS: Bay Leaf, Black Pepper, Brown Lentils, Carrot, Celery, Dry Red
	Wine, Extra Virgin Olive Oil, Garlic, Pimenton, Saffron, Salt, Vegetable
	Stock, Yellow Onion
•Fajitas (source: Dude Diet)
	INGREDIENTS: Chicken, Enchillada Sauce, Green Pepper, Red Pepper, Shredded
	Cheese, Yellow Onion

Dinner:
-------
•Chicken Stew (source: Dude Diet)
	INGREDIENTS: Chicken, Chicken broth, Red Pepper, Stale bread crumbs, Yellow
	Onion
•Stuffing (source: Domesticate Me)
	INGREDIENTS: Chicken broth, Golden Delicious Apple, Sausage, Stale bread
	crumbs, Tyme, Yellow Onion

Brunch:
-------
•Stir Fry (source: Dude Diet Dinner)
	INGREDIENTS: Butter, Chicken, Garlic, Green Pepper, Red Pepper, Soy Sauce,
	Yellow Onion


SHOPPING LIST:
==============
•Bay Leaf
•Black Pepper
•Brown Lentils
•Butter
•Carrot
•Celery
•Chicken
•Chicken broth
•Dry Red Wine
•Enchillada Sauce
•Extra Virgin Olive Oil
•Garlic
•Golden Delicious Apple
•Green Pepper
•Pimenton
•Red Pepper
•Saffron
•Salt
•Sausage
•Shredded Cheese
•Soy Sauce
•Stale bread crumbs
•Tyme
•Vegetable Stock
•Yellow Onion
```

## License
MIT License

Copyright (c) 2023 Benjamin Park

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
