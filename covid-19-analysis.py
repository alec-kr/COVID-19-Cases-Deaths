import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# Import Data From csv
try:
    df = pd.read_csv(r"https://covid.ourworldindata.org/data/ecdc/full_data.csv")

except:
    print("ERROR: The requested CSV may have been moved or deleted. Please visit https://covid.ourworldindata.org to locate a new data source.")

def get_data(u_input):
    print("Loading info...")
    country_data = df[df["location"] == u_input]
    global days, cases, deaths
    days, cases, deaths = country_data["date"], country_data["total_cases"], country_data["total_deaths"]
    print("Alec Ramdhan")

# Plot the trends
def display_graph():
    plt.plot(days, cases, color = "blue")
    plt.grid(color="gray")
    plt.title("Line Graph Showing Cases/Deaths for "+user_sel)
    plt.plot(days, deaths, color = "red")
    plt.legend(["Cases","Deaths"])
    plt.xlabel("Days")
    plt.ylabel("# of Cases/Deaths")
    print("Plot Loaded")
    plt.show()
    print("Plot closed")

user_sel = input("Please Enter a Country: ").title()

get_data(user_sel)
display_graph()
