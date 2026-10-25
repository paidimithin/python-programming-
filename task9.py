
# Student Academic Risk Classification

# Sample student data
students = ["Mithin", "Shai praneeth", "Manohar", "Rohith", "Samuel"]
marks = [85, 35, 55, 30, 70]
attendance = [90, 60, 80, 65, 70]
lab_scores = [88, 32, 35, 25, 85]

# Risk thresholds
MARKS_LIMIT = 40
ATTENDANCE_LIMIT = 75
LAB_LIMIT = 40

low_risk = 0
moderate_risk = 0
high_risk = 0

print("STUDENT ACADEMIC RISK REPORT")
print("-" * 65)

for i in range(len(students)):
    risks = []

    # Identify risk factors
    if marks[i] < MARKS_LIMIT:
        risks.append("Low Marks")

    if attendance[i] < ATTENDANCE_LIMIT:
        risks.append("Low Attendance")

    if lab_scores[i] < LAB_LIMIT:
        risks.append("Low Lab Score")

    # Classify risk category
    risk_count = len(risks)

    if risk_count == 0:
        category = "Low Risk"
        low_risk += 1
    elif risk_count == 1:
        category = "Moderate Risk"
        moderate_risk += 1
    else:
        category = "High Risk"
        high_risk += 1

    # Display individual student report
    risk_details = ", ".join(risks) if risks else "None"

    print(f"Student: {students[i]}")
    print(f"Marks: {marks[i]}")
    print(f"Attendance: {attendance[i]}%")
    print(f"Lab Score: {lab_scores[i]}")
    print(f"Risk Factors: {risk_details}")
    print(f"Risk Category: {category}")
    print("-" * 65)

# Generate summary
print("\nACADEMIC RISK SUMMARY")
print("Total Students:", len(students))
print("Low Risk Students:", low_risk)
print("Moderate Risk Students:", moderate_risk)
print("High Risk Students:", high_risk)
print("Students Needing Support:", moderate_risk + high_risk)
