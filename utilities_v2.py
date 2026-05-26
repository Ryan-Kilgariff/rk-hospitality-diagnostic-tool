def ask_score(question):
    while True:
        try:
            score_input = int(input(question))
            if score_input >=1 and score_input <= 10:
                return score_input
            else:
                print("Please enter a number between 1 and 10.")
        except ValueError:
            print("Invalid input. Please enter a number a valid number.")
def pause():
    input("\nPress Enter to return to the main menu...")
recommendations = []
def add_recommendation(text):
        recommendations.append(text)
def calculate_risk_level(score):
    if score <= 3:
        return "Stable"
    elif score <= 6:
        return "Monitoring required"
    elif score <= 9:
        return "At risk"
    else:
        return "Critical"