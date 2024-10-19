from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import pymysql

pymysql.install_as_MySQLdb()

app = Flask(__name__)

# Configure MySQL database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://myuser:mypassword@localhost/rule_engine_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define Rule model
class Rule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rule_name = db.Column(db.String(255), nullable=False)
    rule_text = db.Column(db.Text, nullable=False)
    ast_representation = db.Column(db.JSON, nullable=False)

# Create the database and tables within the app context
with app.app_context():
    db.create_all()

# Define a root route to check if the server is running
@app.route('/')
def home():
    return "Welcome to the Rule Engine API!"

# Route to serve the rule engine HTML page
@app.route('/ruleengine')
def rule_engine():
    return render_template('ruleengine.html')

# Route to create a new rule
@app.route('/create_rule', methods=['POST'])
def create_rule():
    try:
        data = request.get_json()
        if not data or 'rule' not in data:
            return jsonify({"status": "error", "message": "Missing 'rule' in request data"}), 400
        
        rule_name = data.get('rule_name', f"Rule {Rule.query.count() + 1}")
        rule_text = data['rule']

        new_rule = Rule(rule_name=rule_name, rule_text=rule_text, ast_representation={})
        db.session.add(new_rule)
        db.session.commit()

        return jsonify({"status": "success", "rule_name": rule_name})
    
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# Route to list all existing rules
@app.route('/rules', methods=['GET'])
def get_rules():
    try:
        rules = Rule.query.all()
        rules_list = [{"id": rule.id, "rule_name": rule.rule_name, "rule_text": rule.rule_text} for rule in rules]
        return jsonify({"status": "success", "rules": rules_list})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# Route to check user eligibility based on the rules
@app.route('/check_eligibility', methods=['POST'])
def check_eligibility():
    try:
        data = request.get_json()
        age = data.get('age')
        department = data.get('department')
        salary = data.get('salary')
        experience = data.get('experience')

        # Dummy eligibility check - parse rules and check if they match the user's data
        eligible = False
        rules = Rule.query.all()
        for rule in rules:
            # For simplicity, using eval. In production, you'd want to use a safer way to evaluate these rules
            try:
                if eval(rule.rule_text):
                    eligible = True
                    break
            except Exception as e:
                print(f"Error evaluating rule: {e}")

        return jsonify({"status": "success", "eligible": eligible})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
