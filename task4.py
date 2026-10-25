
# Sports Tournament Ranking System

teams = {
    "Lions": {"points": 0, "gf": 0, "ga": 0},
    "Tigers": {"points": 0, "gf": 0, "ga": 0},
    "Eagles": {"points": 0, "gf": 0, "ga": 0}
}

# Match results: (Team 1, Team 2, Score 1, Score 2)
matches = [
    ("Lions", "Tigers", 2, 1),
    ("Eagles", "Lions", 1, 1),
    ("Tigers", "Eagles", 3, 0)
]

# Process match results
for team1, team2, score1, score2 in matches:
    teams[team1]["gf"] += score1
    teams[team1]["ga"] += score2
    teams[team2]["gf"] += score2
    teams[team2]["ga"] += score1

    if score1 > score2:
        teams[team1]["points"] += 3
    elif score2 > score1:
        teams[team2]["points"] += 3
    else:
        teams[team1]["points"] += 1
        teams[team2]["points"] += 1

# Calculate goal difference
for team in teams:
    teams[team]["gd"] = (
        teams[team]["gf"] - teams[team]["ga"]
    )

# Sort by points, goal difference, and goals scored
rankings = sorted(
    teams.items(),
    key=lambda item: (
        item[1]["points"],
        item[1]["gd"],
        item[1]["gf"]
    ),
    reverse=True
)

# Display leaderboard
print("SPORTS TOURNAMENT RANKINGS")
print("-" * 65)
print(f"{'Rank':<6}{'Team':<12}{'Points':<10}"
      f"{'GF':<8}{'GA':<8}{'GD':<8}")

for rank, (team, stats) in enumerate(rankings, start=1):
    print(
        f"{rank:<6}{team:<12}{stats['points']:<10}"
        f"{stats['gf']:<8}{stats['ga']:<8}"
        f"{stats['gd']:<8}"
    )
