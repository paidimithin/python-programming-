
# Multi-Event Sports Scheduling and Scoring

# Each tuple contains:
# (event name, time slot, participating teams)

events = [
    ("100m Race", "9:00 AM", ["Red", "Blue"]),
    ("Long Jump", "9:00 AM", ["Green", "Red"]),
    ("Relay Race", "10:00 AM", ["Blue", "Green"])
]

# Display the event schedule
print("SPORTS EVENT SCHEDULE")
for event, time, teams in events:
    print(f"{event} - {time} - Teams: {teams}")

# Identify scheduling conflicts
print("\nSCHEDULING CONFLICTS")

conflicts = []

for i in range(len(events)):
    for j in range(i + 1, len(events)):
        event1, time1, teams1 = events[i]
        event2, time2, teams2 = events[j]

        if time1 == time2:
            common_teams = set(teams1) & set(teams2)

            if common_teams:
                conflicts.append(
                    (event1, event2, time1, common_teams)
                )

if conflicts:
    for event1, event2, time, teams in conflicts:
        print(
            f"{teams} have a conflict between "
            f"{event1} and {event2} at {time}"
        )
else:
    print("No scheduling conflicts found.")

# Points earned by teams in each event
scores = {
    "100m Race": {"Red": 10, "Blue": 8},
    "Long Jump": {"Green": 10, "Red": 6},
    "Relay Race": {"Blue": 10, "Green": 8}
}

# Aggregate total points
total_points = {}

for event_scores in scores.values():
    for team, points in event_scores.items():
        total_points[team] = (
            total_points.get(team, 0) + points
        )

# Generate final rankings
rankings = sorted(
    total_points.items(),
    key=lambda item: item[1],
    reverse=True
)

print("\nFINAL TEAM RANKINGS")

for rank, (team, points) in enumerate(rankings, start=1):
    print(f"{rank}. {team} Team - {points} points")
