# ISM3232 Midterm: Cloudstep Software

- **Name:** Breanna Ramirez
- **Version:** 1.0
- **Date:** October 24th 2026

## What This Program Does
This program processes software license orders for Cloudstep Software. It calculates the cost of each order after applying discounts and any onboarding fees. It also determines which orders need contract reviews or trainers and displays a report with the individual orders and overall totals.

## Business Rules
1. License cost: The starting cost of an order is the price per seat multiplied by the number of seats purchased.

2. Seat discounts: Orders with fewer than 10 seats receive no discount. Orders with 10–49 seats receive a 7% discount. Orders with 50 or more seats receive a 16% discount for educational customers and a 7% discount for other customers.

3. Onboarding fee: A $60 onboarding fee is added when the discounted license cost is $400 or less.

4. Contract review: An order requires a contract review when its final total is greater than $5,000.

5. Trainer eligibility: An order receives a trainer if it includes at least 25 seats or its final total is greater than $3,000.

6. Order reporting: The program calculates the total value of all orders, identifies the company with the largest license total, and summarizes the orders requiring contract reviews and trainers.

## How to Run
Open a terminal in the project folder and run:

python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 main.py

## How to Test
Run the following commands from the project folder with the virtual environment activated:

ruff format .
ruff check .
pytest -v

The project contains 27 tests covering the business rules, including discount thresholds, onboarding fees, contract reviews, trainer eligibility and order calculations.

## Files in This Repository
- .gitignore — Lists local files and folders that Git should ignore.

- business_rules.py — Contains the eight functions that implement the business rules.

- main.py — Contains the sample orders and generates the report.

- commands.md — Records terminal commands, outputs, and Git history.

- README.md — Explains the project, its rules, and how to run and test it.

- requirements.txt — Lists the Python packages required for the project.

- tests/__init__.py — Marks the tests directory as a Python package.

- tests/test_business_rules.py — Contains the 27 tests for the business-rule functions.

## AI Use Statement
AI was not used in this assignment.