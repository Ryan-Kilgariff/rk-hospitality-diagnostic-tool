import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from datetime import datetime
from audits import *
from utilities import *
from audits import audit_type, score, answers, recommendations, action_plan
from utilities import ask_score, add_recommendation, calculate_risk_level
from colorama import Fore, Style
def generate_report(business_name):
    global filename
    global status
    status = calculate_risk_level(score)
    additional_notes = input("Add any additional notes or context: ")
    answers.append("Additional notes: " + additional_notes)
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
        risk = "low"
    elif score <= 6:
        risk = "moderate"
    else:
        risk = "high"
    if risk == "high":
        add_recommendation("Immediate operational reset recommended within 14 days.")
    elif risk == "moderate":
        add_recommendation("operational improvements should be scheduled within 30 days.")
    else:
        add_recommendation("operation is stable but should be monitored for any changes.")
    folder_name = "reports"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    filename = business_name + "_report.txt"
    filename = os.path.join(folder_name, filename)
    with open(filename, "w") as file:
        file.write("Business Status: ")
        file.write("\nRK Hospitality diagnostic report\n")
        file.write("-----------------------------\n\n")
        date = datetime.now().strftime("%Y-%m-%d %H:%M")
        file.write("Date: " + date + "\n")
        time = datetime.now().strftime("%H:%M")
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
        file.write("Notes: " + additional_notes + "\n")
def generate_pdf_report(business_name):
    global filename
    pdf_filename = filename.replace(".txt", ".pdf")
    c = canvas.Canvas(pdf_filename, pagesize=A4)
    y = 800
    c.drawString(50, y, "RK Hospitality diagnostic report")
    y -= 30
    c.drawString(50, y, "Business Name: " + business_name)
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