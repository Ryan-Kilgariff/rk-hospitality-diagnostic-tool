import json
import os
from datetime import datetime
from colorama import Fore, Style, init
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
init()
answers = []
recommendations = []
score = 0
morale_score = 0
service_score = 0
stock_score = 0
leadership_score = 0
communaication = "no"
complaints = "no"
waste = "no"
overloaded = "no"
action_plan = []
audit_type = ""
status = "No diagnostic run yet"
def main_menu():
    print("\nRK Hospitality Studio")
    print("--------------------")
    print("1. Run diagnostic")
    print("2. View information")
    print("3. Exit")
    print("4. View operational summary")
    print("5. View previous reports")
    print("6. Read previous report")
    print("7. Search reports")
    print("8. Delete report")
    print("9. Add note to report")
    choice = input("Choose an option: ")
    return choice
def ask_menu_choice(question):
    while True:
        try:
            choice = int(input(question))
            return choice
        except ValueError:
            print("Please enter a valid number.")
def save_business_data():
    data = {
        "name": name,
        "score": score,
        "status": status,
        "recommendations": recommendations,
        "action_plan": action_plan,
        "answers": answers,
        "date": date,
        "time": time
    }
    with open("business_data.json", "w") as file:
        json.dump(data, file, indent=4)
def load_business_data():
    with open("business_data.json", "r") as file:
        data = json.load(file)
    print(data)
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
def reset_diagnostic():
    global score
    global status
    answers.clear()
    recommendations.clear()
    action_plan.clear()
    score = 0
    status = "No diagnostic run yet"
def run_staff_audit():
    global score
    global audit_type
    global morale_score
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
    if complaints == "yes":
        score += 4
    if service_score <= 4:
        recommendations.append("Focus on staff training and consistency in service delivery.")
        recommendations.append("Review leadership communication and workload balance.")
def run_stock_audit():
    global score
    global audit_type
    global stock_score
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
def add_recommendation(text):
    recommendations.append(text)
def run_diagnostic():
    global filename
    global date
    global time
    global name
    global note
    global risk
    global recommendations
    global action_plan
    answers.clear()
    recommendations.clear()
    action_plan.clear()
    score = 0
    name = input("Bussiness Name: ")
    answers.append("Bussiness Name: " + name)
    print("Choose an issue:")
    print("1. Staff")
    print("2. Service")
    print("3. Stock")
    print("4. leadership")
    choice = ask_menu_choice("Choose an option (1-4): ")
    if choice == 1:
        audit_type = "staff"
    elif choice == 2:
        audit_type = "service"
    elif choice == 3:
        audit_type = "stock"
    elif choice == 4:
        audit_type = "leadership"
    if audit_type == "staff":
        run_staff_audit()
    elif audit_type == "service":
        run_service_audit()
    elif audit_type == "stock":
        run_stock_audit()
    elif audit_type == "leadership":
        run_leadership_audit()
    else:
        q1 = input("Can you describe the issue in more detail? ")
        answers.append("Issue details: " + q1)
    recommendations = []
    if score >= 2:
        add_recommendation("Focus on improving staff communication during peak service hours.")
    if score >= 4:
        add_recommendation("Review staffing stucture and role clarity.")
    if score >= 6:
        add_recommendation("immediate operational reset reccommended within 14 days.")
    note = input("Add any additional notes or context: ")
    answers.append("Additional notes: " + note)
    date = datetime.now().strftime("%Y-%m-%d")
    time = datetime.now().strftime("%H-%M")
    filename = name + "_" + date + "_" + time + "_report.txt"
def generate_recommendations():
    recommendations.clear()
    action_plan.clear()
    if morale_score <= 4:
        recommendations.append("Review leadership communication and workload balance.")
        recommendations.append("Focus on improving staff communication during peak service hours.")
    if service_score <= 4 and complaints == "yes":
        recommendations.append("Focus on staff training and consistency in service delivery.")
        recommendations.append("Review leadership communication and workload balance.")
    if stock_score <= 4:
        recommendations.append("Review inventory management practices and supplier reliability.")
        recommendations.append("Focus on improving staff communication during peak service hours.")
    if leadership_score <= 4:
        recommendations.append("Consider leadership coaching and clearer communication of vision and expectations.")
        recommendations.append("Review leadership communication and workload balance.")
def generate_action_plan():
    action_plan.clear()
    if score <= 3:
        action_plan.append("Week 1: Maintain current standards and review basic routines.")
        action_plan.append("Week 2: Check staff feedback and guest experience consistency.")
        action_plan.append("Week 3: Tighten small gaps before they become habits.")
        action_plan.append("Week 4: Review progress and keep monitoring.")
    elif score <= 6:
        action_plan.append("Week 1: Identify the 2 biggest operational pressure points.")
        action_plan.append("Week 2: Clarify ownership, roles, and daily standards.")
        action_plan.append("Week 3: Review service flow and staff communication.")
        action_plan.append("Week 4: Measure improvement and adjust weak areas.")
    else:
        action_plan.append("Week 1: Stabilise the operation and reduce immediate pressure.")
        action_plan.append("Week 2: Reset leadership routines and role clarity.")
        action_plan.append("Week 3: Fix service bottlenecks and staff communication gaps.")
        action_plan.append("Week 4: Review performance, morale, and guest experience.")
def calculate_risk_level(score):
    if score <= 3:
        return "Stable"
    elif score <= 6:
        return "Monitoring required"
    elif score <= 9:
        return "At risk"
    else:
        return "Critical"
def generate_report():
    global filename
    global status
    status = calculate_risk_level(score)
    print("\nGenerating report...")
    if status == "Stable":
        print(Fore.GREEN + "\nBusiness Status: Stable" + Style.RESET_ALL)
    elif status == "Monitoring required":
        print(Fore.YELLOW + "\nBusiness Status: Monitoring required" + Style.RESET_ALL)
    elif status == "At risk":
        print(Fore.RED + "\nBusiness Status: At risk" + Style.RESET_ALL)
    else:
        print(Fore.RED + "\nBusiness Status: Critical" + Style.RESET_ALL)
    if score <= 2:
        risk = "Low"
    elif score <= 6:
        risk = "Moderate"
    else:
        risk = "High"
    if risk == "high":
        add_recommendation("Immediate operational reset recommended within 14 days.")
    elif risk == "moderate":
        add_recommendation("operational improvements should be scheduled within 30 days.")
    else:
        add_recommendation("operation is stable but should be monitored for any changes.")
    folder_name = "reports"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    filename = os.path.join(folder_name, filename)
    with open(filename, "w") as file:
        file.write("Business Status: ")
        file.write("\nRK Hospitality diagnostic report\n")
        file.write("-----------------------------\n\n")
        file.write("Date: " + date + "\n")
        file.write("Time: " + time + "\n")
        file.write("--------------------\n\n")
        file.write("Bussiness information:\n")
        file.write("--------------------\n")
        file.write("Audit Type: " + audit_type + "\n")
        for answer in answers:
            file.write(answer + "\n")
        file.write("\nOperational Risk\n")
        file.write("--------------------\n")
        file.write("\nOperational Risk Score: " + str(score) + "\n")
        file.write("Operational Risk Level: " + risk + "\n\n")
        file.write("Business Status: " + status + "\n")
        file.write("\nRecommendations:\n")
        file.write("--------------------\n")
        for recommendation in recommendations:
            file.write("- " + recommendation + "\n")
        file.write("\n4-week action plan:\n")
        file.write("---------------------\n")
        for step in action_plan:
            file.write("- " + step + "\n")
        file.write("\nConsultant Notes:\n")
        file.write("--------------------\n")
        file.write(note + "\n")
def generate_pdf_report():
    global business_name
    pdf_filename = filename.replace(".txt", ".pdf")
    c = canvas.Canvas(pdf_filename, pagesize=A4)
    y = 800
    c.drawString(50, y, "RK Hospitality diagnostic report")
    y -= 30
    c.drawString(50, y, "Business Name: " + name)
    y -= 20
    c.drawString(50, y, "Risk Score: " + str(score))
    y -= 20
    c.drawString(50, y, "Status: " + status)
    y -= 40
    c.drawString(50, y, "Recommendations:")
    y -= 20
    for recommendation in recommendations:
        c.drawString(60, y, "- " + recommendation)
        y -= 20
    c.save()
    print("\nPDF report generated successfully.")
def view_summary():
    global risk
    print("\n--- OPERATIONAL SUMMARY ---\n")
    print("Current Risk Score:", score)
    print("\nRisk Level:", status)
    print("\nRecommendations:")
    for recommendation in recommendations:
        print("- " + recommendation)
    print("\nAction Steps:")
    for step in action_plan:
        print("- " + step)
def view_previous_reports():
    folder_name = "reports"
    if not os.path.exists(folder_name):
        print("\nNo reports found.")
        return
    print("\n--- SAVED REPORTS ---\n")
    for file in os.listdir(folder_name):
        print("- ", file)
def read_report():
    folder_name = "reports"
    if not os.path.exists(folder_name):
        print("\nNo reports found.")
        return
    files = os.listdir(folder_name)
    print("\n--- SAVED REPORTS ---\n")
    for index, file in enumerate(files):
        print(str(index + 1) + ". " + file)
    choice = int(input("\nChoose report number to view: "))
    selected_file = files[choice - 1]
    file_path = os.path.join(folder_name, selected_file)
    with open(file_path, "r") as file:
        content = file.read()
        print("\n--- REPORT CONTENT ---\n")
        print(content)
def search_reports():
    folder_name = "reports"
    if not os.path.exists(folder_name):
        print("\nNo reports found.")
        return
    search = input("\nEnter business name to search: ").lower()
    found = False
    print("\n--- SEARCH RESULTS ---\n")
    for file in os.listdir(folder_name):
        if search in file.lower():
            print("- ", file)
            found = True
    if not found:
        print("No reports found matching the search criteria.")
def delete_report():
    global file_path
    folder_name = "reports"
    if not os.path.exists(folder_name):
        print("\nNo reports found.")
        return
    files = os.listdir(folder_name)
    print("\n--- DELETE REPORT ---\n")
    for index, file in enumerate(files):
        print(str(index + 1) + ". " + file)
    choice = int(input("\nChoose report number to delete: "))
    selected_file = files[choice - 1]
    file_path = os.path.join(folder_name, selected_file)
    confirm = input("Are you sure you want to delete this report? (yes/no) ")
    if confirm.lower() == "yes":
        import shutil
        backup_folder = "Backups"
        if not os.path.exists(backup_folder):
            os.makedirs(backup_folder)
            backup_path = os.path.join(backup_folder, selected_file)
            shutil.copy(file_path, backup_path)
            os.remove(os.path.join(folder_name, selected_file))
        print("\nReport deleted successfully.")
    else:
        print("\nReport deletion cancelled.")
def add_note_to_report():
    folder_name = "reports"
    if not os.path.exists(folder_name):
        print("\nNo reports found.")
        return
    files = os.listdir(folder_name)
    if len(files) == 0:
        print("\nNo reports found.")
        return
    print("\n--- ADD NOTE TO REPORT ---\n")
    for index, file in enumerate(files):
        print(str(index + 1) + ". " + file)
    choice = int(input("\nChoose report number to add note to: "))
    selected_file = files[choice - 1]
    file_path = os.path.join(folder_name, selected_file)
    note = input("Enter note: ")
    with open(file_path, "a") as file:
        file.write("\nAdditional Follow-Up Note\n")
        file.write("--------------------\n")
    print("\nNote added successfully.")
while True:
    choice = main_menu()
    if choice == "1":
        reset_diagnostic()
        run_diagnostic()
        generate_recommendations()
        generate_action_plan()
        generate_report()
        generate_pdf_report()
        save_business_data()
        pause()
        print("\nDiagnostic complete. Report generated.")
    elif choice == "2":
        print("\nOperational diagnostics system active.")
        pause()
    elif choice == "3":
        print("\nClosing system. Goodbye!")
        exit()
    elif choice == "4":
        view_summary()
        pause()
    elif choice == "5":
        view_previous_reports()
        pause()
    elif choice == "6":
        read_report()
        pause()
    elif choice == "7":
        search_reports()
        pause()
    elif choice == "8":
        delete_report()
        pause()
    elif choice == "9":
        add_note_to_report()
        pause()
    else:
        print("\nInvalid choice. Please try again.")
print(Fore.GREEN + "test successful" + Style.RESET_ALL)
print("\nReport generated successfully.")
print("saved as: " + filename)
print("\nThank you for using RK Hospitality Studio.")