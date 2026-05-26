from utilities import *
from audits import *
answers = []
score = 0
status = "No diagnostic run yet"
recommendations = []
action_plan = []
audit_type = ""
def run_staff_audit():
    global score
    global audit_type
    global morale_score
    global ask_score
    audit_type = "Staff"
    print("\n--- STAFF AUDIT ---")
    morale_score = ask_score("On a scale of 1-10, how would you rate staff morale? ")
    answers.append("Staff Morale Score: " + str(morale_score))
    if morale_score <= 4:
        score += 3
        add_recommendation("Review leadership communication and workload balance.")
    elif morale_score <= 7:
        score += 1
        add_recommendation("Staff morale is stable but needs monitoring.")
    communication = input("Are responsibilities and expectations clear? ")
    answers.append("Responsibilities clear: " + communication)
    if communication.lower() == "no":
        score += 5
def run_service_audit():
    global score
    global audit_type
    global service_score
    global ask_score
    audit_type = "Service"
    print("\n--- SERVICE AUDIT ---")
    service_score = ask_score("Rate service from 1 to 10: ")
    answers.append("Service Score: " + str(service_score))
    if service_score <= 4:
        score += 3
        add_recommendation("Focus on staff training and consistency in service delivery.")
    elif service_score <= 7:
        score += 1
        add_recommendation("Service quality is moderate but could be improved with better training and systems.")
    complaints = input("Are complaints happening often? (yes/no) ")
    answers.append("Complaints happening often: " + complaints)
    if complaints.lower() == "yes":
        score += 4
def run_stock_audit():
    global score
    global audit_type
    global stock_score
    global ask_score
    audit_type = "Stock"
    print("\n--- STOCK AUDIT ---")
    stock_score = ask_score("On a scale of 1-10, how would you rate your stock management? ")
    answers.append("Stock Management Score: " + str(stock_score))
    if stock_score <= 0:
        score += 5
        add_recommendation("Review inventory management practices and supplier reliability.")
    elif stock_score <= 3:
        score += 3
        add_recommendation("Stock management is poor and likely contributing to operational issues.")
    elif stock_score <= 7:
        score += 1
        add_recommendation("Stock management is moderate but could be improved.")
    waste = input("Is there high waste levels? (yes/no) ")
    answers.append("High waste levels: " + waste)
    if waste.lower() == "yes":
        score += 4
def run_leadership_audit():
    global score
    global audit_type
    global leadership_score
    global ask_score
    audit_type = "Leadership"
    print("\n--- LEADERSHIP AUDIT ---")
    leadership_score = ask_score("On a scale of 1-10, how would you rate your leadership? ")
    answers.append("Leadership Score: " + str(leadership_score))
    if leadership_score <= 0:
        score += 6
        add_recommendation("Leadership quality is critical and likely the root cause of operational issues.")
    elif leadership_score <= 4:
        score += 4
        add_recommendation("Consider leadership coaching and clearer communication of vision and expectations.")
    elif leadership_score <= 7:
        score += 1
        add_recommendation("Leadership quality is moderate but could be improved.")
    overloaded = input("Are key people overloaded? (yes/no) ")
    answers.append("Key people overloaded: " + overloaded)
    if overloaded.lower() == "yes":
        score += 4
def ask_score(question):
    while True:
        try:
            score_input = int(input(question))
            if score_input >= 1 and score_input <= 10:
                return score_input
            if score >= 2:
                add_recommendation("Focus on improving staff communication during peak service hours.")
            if score >= 4:
                add_recommendation("Review staffing stucture and role clarity.")
            if score >= 6:
                add_recommendation("immediate operational reset reccommended within 14 days.")
            else:
                print("Please enter a number between 1 and 10.")
        except ValueError:
            print("Invalid input.")