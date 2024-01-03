-- CSC6302 Week 4 Assignment
-- Benjamin Park
-- November 30, 2023
-- SQL Script to use with Application Architecture


-- Database Schema Setup
DROP DATABASE IF EXISTS MealPlanning;

CREATE DATABASE MealPlanning;

USE  MealPlanning;

CREATE TABLE IF NOT EXISTS Cookbook (
    CookbookName varchar(200)  not null,
    IsBook bool not null,
    Website varchar(200),
    PRIMARY KEY (CookbookName)
);

CREATE TABLE IF NOT EXISTS Recipe (
    RecipeName varchar(100) not null,
    CookbookName varchar (200) not null,
    TotalServings int,
    PRIMARY KEY (RecipeName),
    FOREIGN KEY (CookbookName) REFERENCES Cookbook (CookbookName) on update cascade on delete cascade
);

CREATE TABLE IF NOT EXISTS Ingredients (
    Id int not null auto_increment,
    IngredientName varchar(100) not null,
    IngredientType varchar (100),
    PRIMARY KEY (Id)
);

CREATE TABLE IF NOT EXISTS Meal (
    RecipeName varchar(100) not null,
    IngredientId int not null,
    PRIMARY KEY (RecipeName, IngredientId),
    FOREIGN KEY (RecipeName) REFERENCES Recipe (RecipeName) on update cascade on delete cascade,
    FOREIGN KEY (IngredientId) REFERENCES Ingredients (Id) on update cascade on delete cascade
);


-- Populate the tables
INSERT INTO Cookbook (CookbookName, IsBook) VALUES ("Dude Diet", true);
INSERT INTO Cookbook (CookbookName, IsBook) VALUES ("Dude Diet Dinner", true);
INSERT INTO Cookbook (CookbookName, IsBook, Website) VALUES ("Domesticate Me", false, "http://domesticate-me.com");
INSERT INTO Cookbook (CookbookName, IsBook) VALUES ("How to Cook Everything Vegetarian", true);
INSERT INTO Cookbook (CookbookName, IsBook) VALUES ("Ben's Recipes", true);

INSERT INTO Recipe (RecipeName, CookbookName, TotalServings) VALUES ("Fajitas", "Dude Diet", 6);
INSERT INTO Recipe (RecipeName, CookbookName, TotalServings) VALUES ("Stir Fry", "Dude Diet Dinner", 3);
INSERT INTO Recipe (RecipeName, CookbookName, TotalServings) VALUES ("Stuffing", "Domesticate Me", 8);
INSERT INTO Recipe (RecipeName, CookbookName, TotalServings) VALUES ("Chicken Stew", "Dude Diet", 4);
INSERT INTO Recipe (RecipeName, CookbookName, TotalServings) VALUES ("Braised Spanish Lentils", "How to Cook Everything Vegetarian", 4);
INSERT INTO Recipe (RecipeName, CookbookName, TotalServings) VALUES ("Scrambled Eggs", "Ben's Recipes", 2);
INSERT INTO Recipe (RecipeName, CookbookName, TotalServings) VALUES ("Challah", "Ben's Recipes", 16);

INSERT INTO Ingredients (IngredientName, IngredientType) VALUES ("Red Pepper", "produce");
INSERT INTO Ingredients (IngredientName, IngredientType) VALUES ("Green Pepper", "produce");
INSERT INTO Ingredients (IngredientName, IngredientType) VALUES ("Yellow Onion", "produce");
INSERT INTO Ingredients (IngredientName, IngredientType) VALUES ("Chicken", "meat");
INSERT INTO Ingredients (IngredientName, IngredientType) VALUES ("Enchillada Sauce", "pantry");
INSERT INTO Ingredients (IngredientName, IngredientType) VALUES ("Shredded Cheese", "dairy");
INSERT INTO Ingredients (IngredientName, IngredientType) VALUES ("Garlic", "produce");
INSERT INTO Ingredients (IngredientName, IngredientType) VALUES ("Soy Sauce", "condiment");
INSERT INTO Ingredients (IngredientName, IngredientType) VALUES ("Butter", "dairy");
INSERT INTO Ingredients (IngredientName, IngredientType) VALUES ("Sausage", "meat");
INSERT INTO Ingredients (IngredientName, IngredientType) VALUES ("Golden Delicious Apple", "produce");
INSERT INTO Ingredients (IngredientName, IngredientType) VALUES ("Thyme", "spice");
INSERT INTO Ingredients (IngredientName, IngredientType) VALUES ("Chicken broth", "pantry");
INSERT INTO Ingredients (IngredientName, IngredientType) VALUES ("Stale bread crumbs", "pantry");
INSERT INTO Ingredients (IngredientName, IngredientType) VALUES ("Extra Virgin Olive Oil", "pantry");
INSERT INTO Ingredients (IngredientName, IngredientType) VALUES ("Celery", "produce");
INSERT INTO Ingredients (IngredientName, IngredientType) VALUES ("Carrot", "produce");
INSERT INTO Ingredients (IngredientName, IngredientType) VALUES ("Saffron", "spice");
INSERT INTO Ingredients (IngredientName, IngredientType) VALUES ("Pimenton", "spice");
INSERT INTO Ingredients (IngredientName, IngredientType) VALUES ("Bay Leaf", "spice");
INSERT INTO Ingredients (IngredientName, IngredientType) VALUES ("Dry Red Wine", "pantry");
INSERT INTO Ingredients (IngredientName, IngredientType) VALUES ("Vegetable Stock", "pantry");
INSERT INTO Ingredients (IngredientName, IngredientType) VALUES ("Brown Lentils", "pantry");
INSERT INTO Ingredients (IngredientName, IngredientType) VALUES ("Salt", "spice");
INSERT INTO Ingredients (IngredientName, IngredientType) VALUES ("Black Pepper", "spice");
INSERT INTO Ingredients (IngredientName, IngredientType) VALUES ("Eggs", "dairy");
INSERT INTO Ingredients (IngredientName, IngredientType) VALUES ("Whole Milk", "dairy");
INSERT INTO Ingredients (IngredientName, IngredientType) VALUES ("All-Purpose Flour", "baking");
INSERT INTO Ingredients (IngredientName, IngredientType) VALUES ("Yeast", "baking");
INSERT INTO Ingredients (IngredientName, IngredientType) VALUES ("Sugar", "baking");
INSERT INTO Ingredients (IngredientName, IngredientType) VALUES ("Canola Oil", "pantry");
INSERT INTO Ingredients (IngredientName, IngredientType) VALUES ("Water", "elemental");

INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Fajitas", 1);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Fajitas", 2);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Fajitas", 3);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Fajitas", 4);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Fajitas", 5);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Fajitas", 6);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Stir Fry", 1);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Stir Fry", 2);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Stir Fry", 3);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Stir Fry", 4);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Stir Fry", 7);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Stir Fry", 8);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Stir Fry", 9);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Stuffing",3 );
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Stuffing", 10);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Stuffing", 11);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Stuffing", 12);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Stuffing", 13);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Stuffing", 14);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Chicken Stew", 1);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Chicken Stew", 4);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Chicken Stew", 14);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Chicken Stew", 13);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Chicken Stew", 3);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Braised Spanish Lentils", 15);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Braised Spanish Lentils", 16);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Braised Spanish Lentils", 17);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Braised Spanish Lentils", 18);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Braised Spanish Lentils", 19);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Braised Spanish Lentils", 20);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Braised Spanish Lentils", 21);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Braised Spanish Lentils", 22);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Braised Spanish Lentils", 23);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Braised Spanish Lentils", 24);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Braised Spanish Lentils", 25);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Scrambled Eggs", 9);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Scrambled Eggs", 26);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Scrambled Eggs", 27);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Challah", 32);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Challah", 31);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Challah", 26);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Challah", 28);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Challah", 30);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Challah", 24);
INSERT INTO Meal (RecipeName, IngredientId) VALUES ("Challah", 29);


-- Necessary Functions / Stored Procedures
DELIMITER $$
CREATE PROCEDURE GetCookbooks ()
BEGIN
    SELECT CookbookName
    FROM Cookbook
    ORDER BY CookbookName;
END $$

CREATE PROCEDURE GetRecipesFromCookbook (parentCookbook varchar(200))
BEGIN
    SELECT RecipeName
    FROM Recipe
    WHERE CookbookName = parentCookbook
    ORDER BY RecipeName;
END $$

CREATE PROCEDURE GetAllRecipes ()
BEGIN
    SELECT RecipeName
    FROM Recipe
    ORDER BY RecipeName;
END $$

CREATE PROCEDURE ListIngredients (desiredRecipeName varchar(100))
BEGIN
    SELECT IngredientName
    FROM Ingredients INNER JOIN Meal on Id = IngredientId
    WHERE RecipeName = desiredRecipeName
    ORDER BY IngredientName;
END $$

CREATE PROCEDURE RecipeCookbookInfo (desiredRecipeName varchar(100))
BEGIN
    SELECT RecipeName, R.CookbookName, IsBook, Website
    FROM Recipe as R INNER JOIN Cookbook as C on R.CookbookName = C.CookbookName
    WHERE RecipeName = desiredRecipeName;
END $$
DELIMITER ;
