
# 📊 Customer Support Quality Analysis 

**Created by:** Yash Pandey  
**Tools:** Excel | SQL | Python

## 🎯 Project Overview
This project analyzes customer support data to identify teams with resolution delays and understand service quality across different channels.

## 📂 Dataset
- `tickets.csv` — Ticket details, resolution time, channel, and satisfaction.
- `teams.csv` — Team names and departments.

## 🛠️ Tools & Tasks
- **Excel:** Data cleaning, XLOOKUP, IF, PivotTable, and charts.
- **SQL:** Joins, GROUP BY, HAVING, and analytical queries.
- **Python:** Pandas, data cleaning, merging, SLA analysis, and visualization.

## 🧹 Data Cleaning
- Removed duplicate records (13 rows → 12 unique records).
- Merged datasets using `team_id`.
- Created `breach_flag` for tickets taking more than 24 hours.
- Calculated SLA breach rates and monthly resolution trends.

## 📁 Project Structure
```text
├── data/raw/
├──python/analysis.py
├── mock_round.xlsx
├── sql/setup.sql
├── sql/queries.sql
└── README.md


## 👨‍💻 Author
**Yash Pandey**

*All work in this repository is my own except where cited.*
