import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# Import Data From csv
df = pd.read_csv(r"https://covid.ourworldindata.org/data/ecdc/full_data.csv")

country = input("Please Enter a Country: ").title()

# Gather the records related to the specific country
print("Loading info...")

location = df[df["location"] == country]
days = location["date"]
cases = location["total_cases"]
deaths = location["total_deaths"]

# Plot the trends on a line graph
plt.plot(days, cases, color = "blue")
plt.grid(color="gray")
plt.title("Line Graph Showing Cases/Deaths for "+country)
plt.plot(days, deaths, color = "red")
plt.legend(["Cases","Deaths"])
plt.xlabel("Days")
plt.ylabel("# of Cases/Deaths")
plt.show()

print("Plot closed")
