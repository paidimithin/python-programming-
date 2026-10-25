
# Smart Campus Incident and Maintenance Prioritization

incidents = [
    {
        "id": 101,
        "issue": "Electrical sparks in laboratory",
        "severity": "High",
        "location": "Critical",
        "frequency": 5
    },
    {
        "id": 102,
        "issue": "Broken classroom fan",
        "severity": "Medium",
        "location": "Common",
        "frequency": 3
    },
    {
        "id": 103,
        "issue": "Water leakage in corridor",
        "severity": "High",
        "location": "Common",
        "frequency": 4
    },
    {
        "id": 104,
        "issue": "Damaged garden bench",
        "severity": "Low",
        "location": "Other",
        "frequency": 1
    },
    {
        "id": 105,
        "issue": "Server room cooling failure",
        "severity": "High",
        "location": "Critical",
        "frequency": 2
    }
]

severity_points = {
    "High": 5,
    "Medium": 3,
    "Low": 1
}

location_points = {
    "Critical": 3,
    "Common": 2,
    "Other": 1
}

def calculate_priority(incident):
    score = severity_points[incident["severity"]]
    score += location_points[incident["location"]]

    if incident["frequency"] >= 5:
        score += 3
    elif incident["frequency"] >= 2:
        score += 2
    else:
        score += 1

    if score >= 9:
        priority = "High"
    elif score >= 6:
        priority = "Medium"
    else:
        priority = "Low"

    return score, priority


# Calculate scores for all incidents
for incident in incidents:
    score, priority = calculate_priority(incident)
    incident["score"] = score
    incident["priority"] = priority

# Rank incidents by score, highest first
incidents.sort(
    key=lambda item: item["score"],
    reverse=True
)

# Display ranked incidents
print("SMART CAMPUS MAINTENANCE REPORT")
print("-" * 65)

for rank, incident in enumerate(incidents, start=1):
    print(
        f"Rank {rank}: {incident['issue']} | "
        f"Score: {incident['score']} | "
        f"Priority: {incident['priority']}"
    )

# Generate priority summary
print("\nPRIORITY SUMMARY")

for level in ["High", "Medium", "Low"]:
    count = sum(
        1 for incident in incidents
        if incident["priority"] == level
    )
    print(f"{level} Priority Incidents: {count}")

print("\nRecommended action:")
if incidents:
    top = incidents[0]
    print(f"Inspect first: {top['issue']}")
    print(f"Priority: {top['priority']}")
