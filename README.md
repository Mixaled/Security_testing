# Security System Testing Tool

## Introduction

Welcome to the Security System Testing Tool! This Python script is designed to help you ensure the robustness of your security systems without any harmful intent. Think of it as your trusty assistant in safeguarding your data.

## Features

- **Non-Intrusive Testing**: This script simulates a controlled environment for testing login security systems without any actual hacking attempts.

- **Intelligent Password Testing**: It uses a predefined list of possible passwords from an external file to check the strength of your security system.

- **Database Compatibility**: The tool is designed to work with PostgreSQL databases, making it easier for you to test and enhance your security measures.

## How It Works

1. **Module Imports**: The script starts by importing essential modules like Psycopg2 for database interactions and Requests for sending simulated login requests.

2. **Database Connection**: It establishes a secure connection to a local PostgreSQL database named 'students'.

3. **Student Names Query**: The script retrieves a distinct list of student full names from the database.

4. **Password Testing Loop**: For each student name, it crafts login requests with various passwords from the 'passwords' dictionary. The goal is to validate the strength of your security system.

5. **Password Update**: When the correct password is found, the script updates the student's database record with the newfound password.

6. **Failure Handling**: If the script fails to log in with any password, it will continue testing until all options are exhausted, without causing any harm.

7. **Database Cleanup**: Finally, the script gracefully closes the database cursor and connection.

## Disclaimer

This tool is intended solely for testing and improving security systems in a responsible and ethical manner. It should never be used for malicious purposes. Always ensure that you have proper authorization and consent before testing any security system.
