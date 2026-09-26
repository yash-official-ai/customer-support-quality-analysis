
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load Data
tickets = pd.read_csv("data/raw/tickets.csv")
teams = pd.read_csv("data/raw/teams.csv")

# Step 2: Remove Duplicate
tickets = tickets.drop_duplicates()

# Step 3: Merge Both Tables
merged = pd.merge(tickets, teams, on="team_id", how="left")

# Step 4: Check Data
print("Total Tickets:", len(merged))

# Step 5: Create Breach Flag
merged["breach_flag"] = (merged["resolution_hours"] > 24).astype(int)

# Step 6: Department Summary
dept_summary = merged.groupby("department").agg({
    "ticket_id": "count",
    "breach_flag": "sum"
})

dept_summary.columns = ["total_tickets", "breached_tickets"]

dept_summary["sla_breach_rate"] = (
    dept_summary["breached_tickets"] /
    dept_summary["total_tickets"] * 100
)

print("\nDepartment Summary:")
print(dept_summary)

# Step 7: Team Breach Rate
team_summary = merged.groupby("team").agg({
    "ticket_id": "count",
    "breach_flag": "sum"
})

team_summary.columns = ["total_tickets", "breached_tickets"]

team_summary["breach_rate"] = (
    team_summary["breached_tickets"] /
    team_summary["total_tickets"] * 100
)

print("\nTeam Summary:")
print(team_summary)

# Step 8: Monthly Average Resolution Hours
monthly = merged.groupby("month")["resolution_hours"].mean()

monthly = monthly.reindex(["Jan", "Feb", "Mar"])

monthly.plot(kind="bar")

plt.title("Monthly Average Resolution Hours")
plt.xlabel("Month")
plt.ylabel("Average Resolution Hours")
plt.tight_layout()
plt.savefig("outputs/python_chart.png")
plt.show()

# Step 9: Export Clean Data
merged.to_csv("outputs/clean_data.csv", index=False)

# Step 10: Export Department Summary
dept_summary.to_csv("outputs/python_summary.csv")

print("\nAll Files Saved Successfully!")