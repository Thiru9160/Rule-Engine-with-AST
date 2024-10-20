# Rule-Engine-with-AST
 A simple 3-tier rule engine application(Simple UI, API and Backend, Data) to determine user eligibility based on attributes like age, department, income, spend etc.The system can use Abstract Syntax Tree (AST) to represent conditional rules and allow for dynamic creation,combination, and modification of these rules.

API Design implementation:
1. create_rule(rule_string): This function takes a string representing a rule (as
shown in the examples) and returns a Node object representing the corresponding AST.
2. combine_rules(rules): This function takes a list of rule strings and combines them
into a single AST. It should consider efficiency and minimize redundant checks. You can
explore different strategies (e.g., most frequent operator heuristic). The function should
return the root node of the combined AST.
3. evaluate_rule(JSON data): This function takes a JSON representing the combined
rule's AST and a dictionary data containing attributes (e.g., data = {"age": 35,
"department": "Sales", "salary": 60000, "experience": 3}). The
function should evaluate the rule against the provided data and return True if the user is
of that cohort based on the rule, False otherwise


Sample Rules:

● rule1 = "((age > 30 AND department = 'Sales') OR (age < 25 ANDdepartment = 'Marketing')) AND (salary > 50000 OR experience >5)"

● rule2 = "((age > 30 AND department = 'Marketing')) AND (salary >20000 OR experience > 5)"

Test Cases performed:

1. Created individual rules from the examples using create_rule and verify their AST
representation.
2. Combined the example rules using combine_rules and ensure the resulting AST
reflects the combined logic.
3. Implemented sample JSON data and test evaluate_rule for different scenarios.
4. Explore combining additional rules and test the functionality.

Clone the repository:

git clone https://github.com/Thiru9160/Rule-Engine-with-AST.git

cd rule-engine

Set up a virtual environment (optional but recommended):

python3 -m venv venv
source venv/bin/activate (Linux/macOS)
.\venv\Scripts\activate (Windows)

Install dependencies:

pip install -r requirements.txt

Run the main application:

python main.py

To run the test cases:

python -m unittest test_cases.py
