import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

def display_graph():
    plt.plot(days, cases, color = "blue")
    plt.grid(color="gray")
    plt.title("Line Graph Showing Cases/Deaths for "+u_input)
    plt.plot(days, deaths, color = "red")
    plt.legend(["Cases","Deaths"])
    plt.xlabel("Days")
    plt.ylabel("# of Cases/Deaths")
    print("Plot Loaded")
    plt.show()
    print("Plot closed")

# Import Data From csv
df = pd.read_csv(r"https://covid.ourworldindata.org/data/ecdc/full_data.csv")

u_input = input("Please Enter a Country: ").title()

# Gather the records related to the specific u_input
print("Loading info...")

country = df[df["location"] == u_input]
days, cases, deaths = country["date"], country["total_cases"], country["total_deaths"]

# Plot the trends on a line graph
display_graph()
