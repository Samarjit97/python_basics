import pandas as pd
import matplotlib.pyplot as plt

# Small, fake monthly dataset to demonstrate plots (no external data needed)
data = {
    "Month": ["2020-01", "2020-02", "2020-03", "2020-04"],
    "Cases": [10, 50, 300, 500],
    "Deaths": [0, 1, 10, 30],
}
df = pd.DataFrame(data)

# Summary
print("Data Summary:\n")
print(df.describe(include="all"))

# Line
# Shows change over time; markers make points obvious
plt.figure()
plt.plot(df["Month"], df["Cases"], marker="o", label="Cases")
plt.plot(df["Month"], df["Deaths"], marker="x", label="Deaths")
plt.xlabel("Month")
plt.ylabel("Count")
plt.title("COVID Cases vs Deaths (Line)")
plt.legend()
plt.tight_layout()
plt.show()

#Bar
# Bars make it easy to compare values month-to-month
plt.figure()
plt.bar(df["Month"], df["Cases"], label="Cases")
plt.bar(df["Month"], df["Deaths"], bottom=df["Cases"], label="Deaths")  # stacked
plt.xlabel("Month")
plt.ylabel("Count")
plt.title("COVID Cases and Deaths (Stacked Bar)")
plt.legend()
plt.tight_layout()
plt.show()

#Pie

# Pie chart of total distribution across categories
totals = df[["Cases", "Deaths"]].sum()
plt.figure()
plt.pie(totals.values, labels=totals.index, autopct="%1.1f%%", startangle=90)
plt.title("Total Cases vs Deaths (Pie)")
plt.tight_layout()
plt.show()
