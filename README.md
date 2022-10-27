# CRUD-Customer Using Flask
Flask Application to perform CRUD operations on database

In this example:
 - Basic CRUD on Customer database
 - Logging 
 - Unittests
 
# Overview
  - Flask
  - Python 
  - SQLAchemy
  
# Project Layout
 
    |- logs/
    |   |- app.log                       // Logging file for app
    |- models/
    |   |- customer.py                   // Customer model SQLAlchemy ORM
    |- tests/
    |   |- test.py                       // Contains Unit tests
    |- app.py                            // Flask app
    |- table_creation.py                 // Create Database
    |- dockerfile                       
    |- .gitignore
    |- requirments.txt                  // Project Requirements
    
# Run    
## Create database
 1. Run table_creation.py 
## Run App
 1. Create .env file with reuired variables
 2. Run app.py
 ```
 python app.py
 ```
## Run Unittest
 1. Run test.py file
 
# Written by Abhilakshay Singh Pathania
