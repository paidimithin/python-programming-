# University Scholarship Allocation System

MIN_AGGREGATE = 75
MIN_SUBJECT_MARKS = 40
MIN_ATTENDANCE = 75
MAX_INCOME = 250000


def evaluate_student(student):
    # Calculate aggregate percentage
    marks = student["marks"]
    percentage = sum(marks) / len(marks)

    # Check eligibility criteria
    if percentage < MIN_AGGREGATE:
        return False, percentage, "Aggregate marks below 75%"

    if any(mark < MIN_SUBJECT_MARKS for mark in marks):
        return False, percentage, "Subject marks below 40%"

    if student["attendance"] < MIN_ATTENDANCE:
        return False, percentage, "Attendance below 75%"

    if student["income"] > MAX_INCOME:
        return False, percentage, "Family income exceeds limit"

    return True, percentage, "Eligible"


def allocate_scholarships(students):
    eligible = []
    rejected = []

    for student in students:
        status, percentage, reason = evaluate_student(student)
        student["percentage"] = percentage

        if status:
            eligible.append(student)
        else:
            rejected.append((student, reason))

    # Rank by aggregate, attendance, and lower income
    eligible.sort(
        key=lambda s: (
            -s["percentage"],
            -s["attendance"],
            s["income"]
        )
    )

    return eligible, rejected


# Sample student records
students = [
    {
        "name": "Mithin",
        "marks": [90, 85, 88],
        "attendance": 92,
        "income": 300000
    },
    {
        "name": "Shai praneeth",
        "marks": [80, 85, 85],
        "attendance": 90,
        "income": 200000
    },
    {
        "name": "Rohith",
        "marks": [90, 85, 88],
        "attendance": 95,
        "income": 150000
    },
    {
        "name": "Manohar",
        "marks": [35, 90, 95],
        "attendance": 95,
        "income": 100000
    },
    {
        "name": "Samuel",
        "marks": [85, 80, 90],
        "attendance": 80,
        "income": 180000
    }
]

eligible, rejected = allocate_scholarships(students)

print("UNIVERSITY SCHOLARSHIP ALLOCATION")
print("-" * 55)

print("\nEligible Students (Ranked)")
for rank, student in enumerate(eligible, start=1):
    print(
        f"Rank {rank}: {student['name']} | "
        f"Aggregate: {student['percentage']:.2f}% | "
        f"Attendance: {student['attendance']}% | "
        f"Income: Rs.{student['income']}"
    )

print("\nIneligible Students")
for student, reason in rejected:
    print(f"{student['name']}: {reason}")