# Terminal Record: Cloudstep Software

## 1. Building the project

Commands used to create the project and initialize Git:

cd ~/Documents
mkdir ism3232-midterm
cd ism3232-midterm
git init
python3 -m -venv .venv
source .venv/bin/activate
python3 -m pip install pytest ruff
python3 -m pip freeze > requirements.txt
which python3
touch business_rules.py
touch main.py
touch commands.md
touch README.md
mkdir tests
touch tests/__init__.py
touch tests/test_business_rules.py
touch .gitignore
code .
tree -L 2
git status
git add .
ruff format .
ruff check .
pytest -v
git commit -m "Set up midterm project structure and environment"
git rm -r --cached .venv
git add .gitignore
git commit --amend --no-edit
git ls-files
git status
git check-ignore -v tests/__pycache__/
git status
git add .gitignore
git commit --amend --no-edit
git status
git remote add origin https://github.com/breannaramirez/ism3232-midterm.git
git remote -v
ruff format .
ruff check .
pytest -v
git push -u origin main

## 2. The virtual environment
which python3 

/Users/breannaramirez/Documents/ism3232-midterm/.venv/bin/python3

The path includes .venv/bin/python3, confirming that the project's virtual environment is active.

## 3. The project structure
tree -L 2
.
├── __pycache__
│   └── business_rules.cpython-312.pyc
├── business_rules.py
├── commands.md
├── main.py
├── README.md
├── requirements.txt
└── tests
    ├── __init__.py
    ├── __pycache__
    └── test_business_rules.py

4 directories, 8 files

The __pyache__ folder exists locally but is not in the GitHub repositroy because Git ignores these automatically generated Python files.

## 4. Every function and test
rg 'def '
main.py
11:def main():

business_rules.py
18:def calculate_license_cost(seat_price: float, seats: int) -> float:
23:def get_seat_discount(seats: int, education: bool = False) -> float:
35:def calculate_license_total(
49:def needs_contract_review(total: float) -> bool:
54:def gets_trainer(seats: int, total: float) -> bool:
59:def total_licensed(orders: list) -> float:
73:def largest_license(orders: list) -> str:
92:def format_license_line(

tests/test_business_rules.py
13:def test_license_cost():
17:def test_license_cost_zero_seats():
21:def test_discount_below_ten():
25:def test_discount_at_ten():
29:def test_discount_at_forty_nine():
33:def test_discount_education_at_fifty():
37:def test_discount_regular_at_fifty():
41:def test_license_total_with_onboarding_fee():
45:def test_license_total_without_onboarding_fee():
49:def test_license_total_education_discount():
53:def test_license_total_with_discount_and_fee():
57:def test_license_total_above_fee_threshold():
61:def test_license_total_exact_fee_threshold():
65:def test_contract_review_below_threshold():
69:def test_contract_review_at_threshold():
73:def test_contract_review_above_threshold():
77:def test_trainer_below_both_thresholds():
81:def test_trainer_at_seat_threshold():
85:def test_trainer_at_total_threshold():
89:def test_trainer_above_total_threshold():
93:def test_total_licensed_multiple_orders():
101:def test_total_licensed_empty():
105:def test_largest_license():
113:def test_largest_license_empty():
117:def test_largest_license_tie():
125:def test_format_license_line():
132:def test_format_license_line_review():
139:def test_discount_education_just_below_fifty():
143:def test_discount_above_fifty_education():
147:def test_format_license_line_no_services():

commands.md
76:rg 'def '
78:11:def main():
81:13:def test_license_cost():
82:17:def test_license_cost_zero_seats():
83:21:def test_discount_below_ten():
84:25:def test_discount_at_ten():
85:29:def test_discount_at_forty_nine():
86:33:def test_discount_education_at_fifty():
87:37:def test_discount_regular_at_fifty():
88:41:def test_license_total_with_onboarding_fee():
89:45:def test_license_total_without_onboarding_fee():
90:49:def test_license_total_education_discount():
91:53:def test_license_total_with_discount_and_fee():
92:57:def test_license_total_above_fee_threshold():
93:61:def test_license_total_exact_fee_threshold():
94:65:def test_contract_review_below_threshold():
95:69:def test_contract_review_at_threshold():
96:73:def test_contract_review_above_threshold():
97:77:def test_trainer_below_both_thresholds():
98:81:def test_trainer_at_seat_threshold():
99:85:def test_trainer_at_total_threshold():
100:89:def test_trainer_above_total_threshold():
101:93:def test_total_licensed_multiple_orders():
102:101:def test_total_licensed_empty():
103:105:def test_largest_license():
104:113:def test_largest_license_empty():
105:117:def test_largest_license_tie():
106:125:def test_format_license_line():
107:132:def test_format_license_line_review():
110:18:def calculate_license_cost(seat_price: float, seats: int) -> float:
111:23:def get_seat_discount(seats: int, education: bool = False) -> float:
112:35:def calculate_license_total(
113:49:def needs_contract_review(total: float) -> bool:
114:54:def gets_trainer(seats: int, total: float) -> bool:
115:59:def total_licensed(orders: list) -> float:
116:73:def largest_license(orders: list) -> str:
117:92:def format_license_line(

business_rules.py defines 8 functions and tests/test_business_rules.py defines 30 tests.

## 5. Which files print
rg -l 'print'
main.py

main.py contains the print statements used to display the report, while business_rules.py does not appear because it returns values instead of printing them.

## 6. The commit history
git log --oneline
7682e47 (HEAD -> main) Build Cloudstep order report and summary
ecb8977 Add order aggregation and report formatting
b13430c (origin/main) Add license pricing, discounts, review and trainer rules
3e6f40a Set up midterm project structure and environment

There were 4 commits at the time of this check.