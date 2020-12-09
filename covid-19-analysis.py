import pandas as pd
from matplotlib import pyplot as plt
import mplcursors
 
# Import data from an online CSV file
try:
    df = pd.read_csv(r"https://covid.ourworldindata.org/data/ecdc/full_data.csv")

# If no connection can be established, run the visualization on an old data set, and notify the user.
except:
    print("ERROR: The requested CSV may have been moved or deleted. Please visit https://covid.ourworldindata.org to locate a new data source.")

# Gather the cases/deaths for the country
def get_data(u_input):
    print("Loading info...")
    country_data = df[df["location"] == u_input]
    global days, cases, deaths
    days, cases, deaths = country_data["date"], country_data["total_cases"], country_data["total_deaths"]

# Plot the trends
def display_graph():
    plt.figure(figsize=(15,8))
    plt.rcParams.update({'font.size': 9})
    plt.plot(days, cases, color = "blue")
    plt.xticks(rotation=90)
    plt.grid(color="gray")
    plt.title("Line Graph Showing Cases/Deaths for "+user_sel)
    plt.plot(days, deaths, color = "red")
    plt.legend(["Cases","Deaths"])

    plt.xlabel("Days")
    plt.ylabel("# of Cases/Deaths")
    print("Plot Loaded")

    mplcursors.cursor(hover = True) # Add hovering cursor
    plt.show()

    # Print a messgage after the plot window is closed
    print("Plot closed")

# Ask for an input, and set the first letter to uppercase
user_sel = input("Please Enter a Country: ").title()

get_data(user_sel)
display_graph()
