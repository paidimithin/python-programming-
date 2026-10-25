
# Campus Festival Registration and Financial Audit

registrations = [
    {"id": "P101", "name": "Mithin", "fee": 500},
    {"id": "P102", "name": "Rohith", "fee": 500},
    {"id": "P103", "name": "Manohar", "fee": 400},
    {"id": "P104", "name": "Shai praneeth", "fee": 500},
    {"id": "P102", "name": "Samuel", "fee": 500},
    {"id": "P105", "name": "Prem", "fee": 400}
]

sponsorships = {
    "Tech Solutions": 10000,
    "Campus Cafe": 5000,
    "Alumni Association": 8000
}

expenses = {
    "Stage decoration": 6000,
    "Sound system": 4000,
    "Food and refreshments": 5000,
    "Marketing": 2000
}

# Step 1: Detect duplicate registrations
seen_ids = set()
unique_registrations = []
duplicates = []

for participant in registrations:
    participant_id = participant["id"]

    if participant_id in seen_ids:
        duplicates.append(participant)
    else:
        seen_ids.add(participant_id)
        unique_registrations.append(participant)

# Step 2: Calculate registration fees
registration_total = sum(
    participant["fee"]
    for participant in unique_registrations
)

# Step 3: Calculate sponsorship contributions
sponsorship_total = sum(sponsorships.values())

# Step 4: Calculate total expenses
expense_total = sum(expenses.values())

# Step 5: Calculate final balance
total_income = registration_total + sponsorship_total
final_balance = total_income - expense_total

# Step 6: Display audit report
print("===== CAMPUS FESTIVAL AUDIT =====")

print("\nUnique participants:",
      len(unique_registrations))

print("Duplicate registrations:", len(duplicates))

for participant in duplicates:
    print("Duplicate ID:", participant["id"],
          "-", participant["name"])

print("\nRegistration fees: Rs.", registration_total)
print("Sponsorship contributions: Rs.", sponsorship_total)
print("Total income: Rs.", total_income)
print("Total expenses: Rs.", expense_total)
print("Final balance: Rs.", final_balance)

if final_balance > 0:
    print("Financial Status: SURPLUS")
elif final_balance < 0:
    print("Financial Status: DEFICIT")
else:
    print("Financial Status: BREAK-EVEN")
